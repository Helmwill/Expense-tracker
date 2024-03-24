import tkinter as tk
from tkinter import Entry, Label, Button, END
import expense_tracker as expense_tracker

root = tk.Tk()
root.title("Expense Tracker")


def add_expense_category_button_clicked():
    expense_tracker.add_expense_category(category_name_entry.get())
    category_name_entry.delete(0, tk.END)

def delete_expenseCat_button_clicked():
    expense_tracker.delete_expense_category(category_id_entry.get())
    category_id_entry.delete(0, tk.END)

def add_expense_button_clicked():
    expense_tracker.add_expense(date_entry.get(), description_entry.get(), amount_entry.get(), category_id_entry.get())
    date_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_id_entry.delete(0, tk.END)

def view_expenses_button_clicked():
    expenses_text.delete(1.0, tk.END)
    expenses = expense_tracker.view_expenses()
    for expense in expenses:
        expenses_text.insert(tk.END, f"{expense['amount']} - {expense['date']} - {expense['description']}\n")

def add_income_category_button_clicked():
    expense_tracker.add_income_category(income_category_name_entry.get())
    income_category_name_entry.delete(0, tk.END)

def delete_income_category_button_clicked():
    expense_tracker.delete_income_category(income_category_id_entry.get())
    income_category_id_entry.delete(0, tk.END)

def add_income_button_clicked():
    expense_tracker.add_income(date_entry.get(), description_entry.get(), amount_entry.get(), category_id_entry.get())
    date_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_id_entry.delete(0, tk.END)
    
def view_expense_categories_button_clicked():
    expense_categories_text.delete(1.0, tk.END)
    expense_categories = expense_tracker.view_expense_categories()
    for category in expense_categories:
        expense_categories_text.insert(tk.END, f"{category['category_id']} - {category['category_name']}\n")

def view_income_categories_button_clicked():
    income_categories_text.delete(1.0, tk.END)
    income_categories = expense_tracker.view_income_categories()
    for category in income_categories:
        income_categories_text.insert(tk.END, f"{category['category_id']} - {category['category_name']}\n")

def calculate_budget_button_clicked():
    budget_text.delete(1.0, tk.END)
    budget = expense_tracker.calculate_budget()
    budget_text.insert(tk.END, f"Budget: {budget}")

def view_expenses_button_clicked():
    expenses_text.delete(1.0, tk.END)
    expenses = expense_tracker.view_expenses()
    for expense in expenses:
        expenses_text.insert(tk.END, f"{expense['amount']} - {expense['date']} - {expense['description']}\n")

def view_incomes_button_clicked():
    income_text.delete(1.0, tk.END)
    incomes = expense_tracker.view_incomes()
    for income in incomes:
        income_text.insert(tk.END, f"{income['amount']} - {income['date']} - {income['description']}\n")

def set_financial_goal_button_clicked():
    expense_tracker.set_financial_goal(financial_goal_entry.get())
    financial_goal_entry.delete(0, tk.END)

def view_expense_financial_goal_button_clicked():
    financial_goal_text.delete(1.0, tk.END)
    financial_goal = expense_tracker.view_expense_financial_goal()
    financial_goal_text.insert(tk.END, f"Financial Goal: {financial_goal}")

def view_income_financial_goal_button_clicked():
    financial_goal_text.delete(1.0, tk.END)
    financial_goal = expense_tracker.view_income_financial_goal()
    financial_goal_text.insert(tk.END, f"Financial Goal: {financial_goal}")

def set_budget_button_clicked():
    expense_tracker.set_budget(budget_entry.get())
    budget_entry.delete(0, tk.END)

def view_category_budget_button_clicked():
    budget_text.delete(1.0, tk.END)
    budget = expense_tracker.view_category_budget()
    budget_text.insert(tk.END, f"Budget: {budget}")

def view_all_categories_button_clicked():
    all_categories_text.delete(1.0, tk.END)
    all_categories = expense_tracker.view_all_categories()
    for category in all_categories:
        all_categories_text.insert(tk.END, f"{category['category_id']} - {category['category_name']}\n")
    


# Create expense category elements


category_name_label = tk.Label(root, text="Expense Category Name")
category_name_label.grid(row=0, column=0, pady=(10, 0))
category_name_entry = tk.Entry(root, width=30)
category_name_entry.grid(row=0, column=1, padx=20, pady=(10, 0))

add_expense_category_button = tk.Button(root, text="Add Expense Category", command=add_expense_category_button_clicked)
add_expense_category_button.grid(row=0, column=2, padx=10)

# Create expense category deletion elements

category_id_label = tk.Label(root, text="Expense Category ID")
category_id_label.grid(row=1, column=0, pady=(10, 0))
category_id_entry = tk.Entry(root, width=30)

category_id_entry.grid(row=1, column=1, padx=20, pady=(10, 0))
delete_expenseCat_button = tk.Button(root, text="Delete Expense Category", command=delete_expenseCat_button_clicked)
delete_expenseCat_button.grid(row=1, column=2, padx=10)


# Create expense elements
amount_label = tk.Label(root, text="Amount")

amount_label.grid(row=2, column=0, pady=(10, 0))
amount_entry = tk.Entry(root, width=30)




amount_entry.grid(row=2, column=1, padx=20, pady=(10, 0))
date_label = tk.Label(root, text="Date")
date_label.grid(row=3, column=0, pady=(10, 0))
date_entry = tk.Entry(root, width=30)
date_entry.grid(row=3, column=1, padx=20, pady=(10, 0))
description_label = tk.Label(root, text="Description")

description_label.grid(row=4, column=0, pady=(10, 0))
description_entry = tk.Entry(root, width=30)
description_entry.grid(row=4, column=1, padx=20, pady=(10, 0))
add_expense_button = tk.Button(root, text="Add Expense", command=add_expense_button_clicked)

add_expense_button.grid(row=4, column=2, padx=10)

# Create view expenses button

view_expenses_button = tk.Button(root, text="View Expenses", command=view_expenses_button_clicked)
view_expenses_button.grid(row=5, column=0, columnspan=3, pady=10)


# Create income category elements
income_category_name_label = tk.Label(root, text="Income Category Name")

income_category_name_label.grid(row=6, column=0, pady=(10, 0))
income_category_name_entry = tk.Entry(root, width=30)
income_category_name_entry.grid(row=6, column=1, padx=20, pady=(10, 0))

add_income_category_button = tk.Button(root, text="Add Income Category", command=add_income_category_button_clicked)
add_income_category_button.grid(row=6, column=2, padx=10)


# Create income category deletion elements
income_category_id_label = tk.Label(root, text="Income Category ID")

income_category_id_label.grid(row=7, column=0, pady=(10, 0))
income_category_id_entry = tk.Entry(root, width=30)

income_category_id_entry.grid(row=7, column=1, padx=20, pady=(10, 0))
delete_income_category_button = tk.Button(root, text="Delete Income Category", command=delete_income_category_button_clicked)
delete_income_category_button.grid(row=7, column=2, padx=10)

# Create income elements
income_amount_label = tk.Label(root, text="Amount")
income_amount_label.grid(row=8, column=0, pady=(10, 0))
income_amount_entry = tk.Entry(root, width=30)
income_amount_entry.grid(row=8, column=1, padx=20, pady=(10, 0))
income_date_label = tk.Label(root, text="Date")
income_date_label.grid(row=9, column=0, pady=(10, 0))
income_date_entry = tk.Entry(root, width=30)
income_date_entry.grid(row=9, column=1, padx=20, pady=(10, 0))
income_description_label = tk.Label(root, text="Description")
income_description_label.grid(row=10, column=0, pady=(10, 0))
income_description_entry = tk.Entry(root, width=30)
income_description_entry.grid(row=10, column=1, padx=20, pady=(10, 0))
add_income_button = tk.Button(root, text="Add Income", command=add_income_button_clicked)
add_income_button.grid(row=10, column=2, padx=10)

# Create view income categories button
view_income_categories_button = tk.Button(root, text="View Income Categories", command=view_income_categories_button_clicked)
view_income_categories_button.grid(row=11, column=0, columnspan=3, pady=10)

# Create budget calculation button
calculate_budget_button = tk.Button(root, text="Calculate Budget", command=calculate_budget_button_clicked)
calculate_budget_button.grid(row=12, column=0, columnspan=3, pady=10)

# Create view expenses button
view_expenses_button = tk.Button(root, text="View Expenses", command=view_expenses_button_clicked)
view_expenses_button.grid(row=13, column=0, columnspan=3, pady=10)

# Create view incomes button
view_incomes_button = tk.Button(root, text="View Incomes", command=view_incomes_button_clicked)
view_incomes_button.grid(row=14, column=0, columnspan=3, pady=10)

# Create financial goal elements
financial_goal_label = tk.Label(root, text="Financial Goal")
financial_goal_label.grid(row=15, column=0, pady=(10, 0))
financial_goal_entry = tk.Entry(root, width=30)
financial_goal_entry.grid(row=15, column=1, padx=20, pady=(10, 0))
set_financial_goal_button = tk.Button(root, text="Set Expense Financial Goal", command=set_financial_goal_button_clicked)
set_financial_goal_button.grid(row=15, column=2, padx=10)

# Create view expense financial goal button
view_expense_financial_goal_button = tk.Button(root, text="View Expense Financial Goal", command=view_expense_financial_goal_button_clicked)
view_expense_financial_goal_button.grid(row=16, column=0, columnspan=3, pady=10)

# Create view income financial goal button
view_income_financial_goal_button = tk.Button(root, text="View Income Financial Goal", command=view_income_financial_goal_button_clicked)
view_income_financial_goal_button.grid(row=17, column=0, columnspan=3, pady=10)

# Create budget elements
budget_label = tk.Label(root, text="Budget")
budget_label.grid(row=18, column=0, pady=(10, 0))
budget_entry = tk.Entry(root, width=30)
budget_entry.grid(row=18, column=1, padx=20, pady=(10, 0))
set_budget_button = tk.Button(root, text="Set Category Budget", command=set_budget_button_clicked)
set_budget_button.grid(row=18, column=2, padx=10)

# Create view category budget button
view_category_budget_button = tk.Button(root, text="View Category Budget", command=view_category_budget_button_clicked)
view_category_budget_button.grid(row=19, column=0, columnspan=3, pady=10)

# Create view all categories button
view_all_categories_button = tk.Button(root, text="View All Categories", command=view_all_categories_button_clicked)
view_all_categories_button.grid(row=20, column=0, columnspan=3, pady=10)

# Create text boxes for displaying results
expenses_text = tk.Text(root, height=10, width=50, state='normal')  # Set state to 'normal'
expenses_text.grid(row=21, column=0, columnspan=3, pady=10)
income_categories_text = tk.Text(root, height=10, width=50, state='normal')  # Set state to 'normal'
income_categories_text.grid(row=22, column=0, columnspan=3, pady=10)
budget_text = tk.Text(root, height=1, width=50, state='normal')  # Set state to 'normal'
budget_text.grid(row=23, column=0, columnspan=3, pady=10)
financial_goal_text = tk.Text(root, height=1, width=50, state='normal')  # Set state to 'normal'
financial_goal_text.grid(row=24, column=0, columnspan=3, pady=10)
all_categories_text = tk.Text(root, height=10, width=50, state='normal')  # Set state to 'normal'
all_categories_text.grid(row=25, column=0, columnspan=3, pady=10)

# Main tkinter window loop
root.mainloop()

