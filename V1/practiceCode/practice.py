import sqlite3

# Create or connect to the database
def create_or_connect_db():
    conn = sqlite3.connect('finance_tracker.db')
    return conn

# Create necessary tables if they don't exist
def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExpenseCategories (
            CategoryID INTEGER PRIMARY KEY,
            CategoryName TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Expenses (
            ExpenseID INTEGER PRIMARY KEY,
            Date TEXT,
            Description TEXT,
            Amount INTEGER,
            CategoryID INTEGER,
            FOREIGN KEY (CategoryID) REFERENCES ExpenseCategories(CategoryID)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS IncomeCategories (
            CategoryID INTEGER PRIMARY KEY,
            CategoryName TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Income (
            IncomeID INTEGER PRIMARY KEY,
            Date TEXT,
            Description TEXT,
            Amount INTEGER,
            CategoryID INTEGER,
            FOREIGN KEY (CategoryID) REFERENCES IncomeCategories(CategoryID)
        )
    ''')

    conn.commit()

# Function to add new expense category to database
def add_expense_category(conn, category_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO ExpenseCategories(CategoryName) VALUES (?)", (category_name,))
    conn.commit()
    print(f"Expense category '{category_name}' added successfully.")

# Function to delete an expense category
def delete_expense_category(conn, category_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ExpenseCategories WHERE CategoryID = ?", (category_id,))
    conn.commit()
    print("Expense category deleted successfully.")

# Function to add expense
def add_expense(conn, date, description, amount, category_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Expenses(Date, Description, Amount, CategoryID) VALUES (?, ?, ?, ?)",
                   (date, description, amount, category_id))
    conn.commit()
    print("Expense added successfully.")

# Function to add new income category to database
def add_income_category(conn, category_name):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO IncomeCategories(CategoryName) VALUES (?)", (category_name,))
    conn.commit()
    print(f"Income category '{category_name}' added successfully.")

# Function to delete an income category
def delete_income_category(conn, category_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM IncomeCategories WHERE CategoryID = ?", (category_id,))
    conn.commit()
    print("Income category deleted successfully.")

# Function to add income
def add_income(conn, date, description, amount, category_id):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Income(Date, Description, Amount, CategoryID) VALUES (?, ?, ?, ?)",
                   (date, description, amount, category_id))
    conn.commit()
    print("Income added successfully.")

# Function to view expense categories
def view_expense_categories(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ExpenseCategories")
    rows = cursor.fetchall()
    print("Expense Categories:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}")

# Function to view income categories
def view_income_categories(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM IncomeCategories")
    rows = cursor.fetchall()
    print("Income Categories:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}")

# Function to calculate budget
def calculate_budget(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Amount) FROM Expenses")
    total_expenses = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(Amount) FROM Income")
    total_income = cursor.fetchone()[0]

    if total_income is None:
        total_income = 0
    if total_expenses is None:
        total_expenses = 0

    budget = total_income - total_expenses
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")
    print(f"Budget: {budget}")

# Main function to execute the program
def main():
    conn = create_or_connect_db()
    create_tables(conn)

    while True:
        print("\n-- Finance Tracker --")
        print("1. Add new expense category")
        print("2. Delete expense category")
        print("3. Add expense")
        print("4. Add new income category")
        print("5. Delete income category")
        print("6. Add income")
        print("7. View expense categories")
        print("8. View income categories")
        print("9. Calculate budget")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            category_name = input("Enter new expense category name: ")
            add_expense_category(conn, category_name)
        elif choice == '2':
            category_id = int(input("Enter ID of the expense category to delete: "))
            delete_expense_category(conn, category_id)
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = int(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_expense(conn, date, description, amount, category_id)
        elif choice == '4':
            category_name = input("Enter new income category name: ")
            add_income_category(conn, category_name)
        elif choice == '5':
            category_id = int(input("Enter ID of the income category to delete: "))
            delete_income_category(conn, category_id)
        elif choice == '6':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = int(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_income(conn, date, description, amount, category_id)
        elif choice == '7':
            view_expense_categories(conn)
        elif choice == '8':
            view_income_categories(conn)
        elif choice == '9':
            calculate_budget(conn)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    conn.close()

if __name__ == "__main__":
    main()
