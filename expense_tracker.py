import sqlite3 

#creating & enabling conection
def db_connect():
    try:
        connection = sqlite3.connect('finance_tracker.db')
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None
#create tables if they do not alrerady exist 
def create_tables(connection):
    try:
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ExpenseCategories (
                CategoryId INTEGER PRIMARY KEY, 
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
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

def add_expense_category(connection, category_name):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ExpenseCategories(CategoryName) VALUES (?)", (category_name,))
        connection.commit()
        print(f"Expense category '{category_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding expense category: {e}")

def delete_expense_category(connection, category_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ExpenseCategories WHERE CategoryId = ?", (category_id,))
        connection.commit()
        print("Expense category deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting expense category: {e}")

def add_expense(connection, date, description, amount, category_id):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Expenses(Date, Description, Amount, CategoryID) VALUES (?,?,?,?)",
            (date, description, amount, category_id))
        connection.commit()
        print("Expense added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding expense: {e}")

def add_income_category(connection, category_name): 
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO IncomeCategories(CategoryName) VALUES (?)", (category_name,))
        connection.commit()
        print(f"Income category '{category_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding income category: {e}")

def delete_income_category(connection, category_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM IncomeCategories WHERE CategoryID = ?", (category_id,))
        connection.commit()
        print("Income category deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting income category: {e}")

def add_income(connection, date, description, amount, category_id):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Income(Date, Description, Amount, CategoryID) VALUES (?,?,?,?)", 
                        (date, description, amount, category_id))
        connection.commit()
        print("Income added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding income: {e}")

def view_expense_categories(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ExpenseCategories")
        rows = cursor.fetchall()
        print("Expense Categories: ")
        for row in rows: 
            print(f"ID: {row[0]}, Name: {row[1]}")
    except sqlite3.Error as e:
        print(f"Error viewing expense categories: {e}")

def view_income_categories(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM IncomeCategories")
        rows = cursor.fetchall()
        print("Income Categories: ")
        for row in rows:
            print(f"{row[0]}, Name: {row[1]}")
    except sqlite3.Error as e:
        print(f"Error viewing income categories: {e}")

def calculate_budget(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(Amount) FROM Expenses")
        total_expenses = cursor.fetchone()[0]
        cursor.execute("SELECT SUM(Amount) FROM Income")
        total_income = cursor.fetchone()[0]

        if total_income is None:
            total_income = 0
        if total_expenses is None:
            total_expenses = 0 

        budget = total_income - total_expenses
        print(f"Total income: {total_income}")
        print(f"Total expenses: {total_expenses}")
        print(f"Budget: {budget}")
    except sqlite3.Error as e:
        print(f"Error calculating budget: {e}")


            

def main():
    connection = db_connect()
    create_tables(connection)
        
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
            add_expense_category(connection, category_name)
        elif choice == '2':
            category_id = int(input("Enter ID of the expense category to delete: "))
            delete_expense_category(connection, category_id)
        elif choice == '3':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = int(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_expense(connection, date, description, amount, category_id)
        elif choice == '4':
            category_name = input("Enter new income category name: ")
            add_income_category(connection, category_name)
        elif choice == '5':
            category_id = int(input("Enter ID of the income category to delete: "))
            delete_income_category(connection, category_id)
        elif choice == '6':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = int(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_income(connection, date, description, amount, category_id)
        elif choice == '7':
            view_expense_categories(connection)
        elif choice == '8':
            view_income_categories(connection)
        elif choice == '9':
            calculate_budget (connection)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

        connection.close()

    if __name__ == "__main__":
        main()
