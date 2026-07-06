from contextlib import asynccontextmanager
from datetime import date
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db import connect, init_db

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

TIERS = [("essential", "Essential"), ("important", "Important"), ("bonus", "Bonus")]


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title="Expense Tracker v2", lifespan=lifespan)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

templates = Jinja2Templates(directory=TEMPLATES_DIR)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    conn = connect()
    try:
        goals = conn.execute(
            "SELECT id, name, tier, target_amount, icon_path FROM goals ORDER BY id"
        ).fetchall()
        saved = dict(
            conn.execute(
                "SELECT goal_id, COALESCE(SUM(amount), 0) FROM contributions GROUP BY goal_id"
            ).fetchall()
        )
    finally:
        conn.close()

    tiers = []
    for key, label in TIERS:
        tier_goals = []
        for g in goals:
            if g["tier"] != key:
                continue
            amount_saved = saved.get(g["id"], 0.0)
            target = g["target_amount"]
            amount_remaining = max(target - amount_saved, 0.0)
            percent = min(int(amount_saved / target * 100), 100) if target > 0 else 0
            tier_goals.append(
                {
                    "id": g["id"],
                    "name": g["name"],
                    "target_amount": target,
                    "amount_saved": amount_saved,
                    "amount_remaining": amount_remaining,
                    "percent": percent,
                    "icon_path": g["icon_path"],
                }
            )
        tiers.append({"key": key, "label": label, "goals": tier_goals})

    return templates.TemplateResponse(request, "index.html", {"tiers": tiers})


@app.get("/goals/new", response_class=HTMLResponse)
def goals_new(request: Request):
    return templates.TemplateResponse(request, "goals_new.html")


@app.post("/goals")
def create_goal(
    name: str = Form(...),
    tier: str = Form(...),
    target_amount: float = Form(...),
):
    conn = connect()
    try:
        conn.execute(
            "INSERT INTO goals (name, tier, target_amount, icon_path, created_at) "
            "VALUES (?, ?, ?, ?, ?)",
            (name, tier, target_amount, None, date.today().isoformat()),
        )
        conn.commit()
    finally:
        conn.close()
    return RedirectResponse("/", status_code=303)


@app.post("/goals/{goal_id}/contributions")
def add_contribution(
    goal_id: int,
    amount: float = Form(...),
    note: str = Form(default=""),
    date_value: str = Form(default="", alias="date"),
):
    conn = connect()
    try:
        conn.execute(
            "INSERT INTO contributions (goal_id, amount, note, date) VALUES (?, ?, ?, ?)",
            (goal_id, amount, note or None, date_value or date.today().isoformat()),
        )
        conn.commit()
    finally:
        conn.close()
    return RedirectResponse("/", status_code=303)


@app.post("/goals/{goal_id}/delete")
def delete_goal(goal_id: int):
    conn = connect()
    try:
        conn.execute("DELETE FROM contributions WHERE goal_id = ?", (goal_id,))
        conn.execute("DELETE FROM goals WHERE id = ?", (goal_id,))
        conn.commit()
    finally:
        conn.close()
    return RedirectResponse("/", status_code=303)
