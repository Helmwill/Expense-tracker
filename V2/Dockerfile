# Expense Tracker v2 — minimal FastAPI image
FROM python:3.12-slim

# Don't buffer stdout/stderr; no .pyc files
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Application code (owned by backend/frontend workers)
COPY app/ ./app/
COPY templates/ ./templates/
COPY static/ ./static/

# Run as an unprivileged user (required for read_only + no-new-privileges)
RUN useradd --create-home --uid 10001 appuser
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
