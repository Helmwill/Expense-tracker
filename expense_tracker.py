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
            CategoryName TEXT,
            Budget INTEGER,
            FinancialGoal INTEGER
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
            CategoryName TEXT,
            Budget INTEGER,
            FinancialGoal INTEGER
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
        connection.commit()
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
        connection.commit()
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
        connection.commit

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

def view_expenses(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Expenses")
        rows = cursor.fetchall()
        connection.commit()
        print("Expenses: ")
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Description: {row[2]}, Amount: {row[3]}, CategoryID: {row[4]}")
    except sqlite3.Error as e:
        print(f"Error viewing expenses: {e}")

def view_income(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Income")
        rows = cursor.fetchall()
        connection.commit()
        print("Income: ")
        for row in rows:
            print(f"ID: {row[0]}, Date: {row[1]}, Description: {row[2]}, Amount: {row[3]}, CategoryID: {row[4]}")
    except sqlite3.Error as e:
        print(f"Error viewing income: {e}")

def set_financial_goal(connection, category_id, goal_amount, goal_type):
    try:
        cursor = connection.cursor()
        if goal_type.lower() == 'expense':
            cursor.execute("UPDATE ExpenseCategories SET FinancialGoal = ? WHERE CategoryId = ?", (goal_amount, category_id))
        elif goal_type.lower() == 'income':
            cursor.execute("UPDATE IncomeCategories SET FinancialGoal = ? WHERE CategoryId = ?", (goal_amount, category_id))
        else:
            print("Invalid goal type. Please specify 'expense' or 'income'.")
            return
        
        connection.commit()
        print("Financial goal set successfully.")
    except sqlite3.Error as e:
        print(f"Error setting financial goal: {e}")


def view_expense_financial_goal(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT CategoryId, CategoryName, FinancialGoal FROM ExpenseCategories")
        rows = cursor.fetchall()
        connection.commit()
        print("Expense Categories:")
        for row in rows:
            category_id, category_name, goal = row
            print(f"ID: {category_id}, Category: {category_name}, Financial Goal: {goal}")
    except sqlite3.Error as e:
        print(f"Error viewing expense categories financial goals: {e}")
        
        
def view_income_financial_goal(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT CategoryID, CategoryName, FinancialGoal FROM IncomeCategories")
        rows = cursor.fetchall()
        connection.commit()
        print("Income Categories:")
        for row in rows:
            category_id, category_name, goal = row
            print(f"ID: {category_id}, Category: {category_name}, Financial Goal: {goal}")
    except sqlite3.Error as e:
        print(f"Error viewing income categories financial goals: {e}")

def set_budget(connection, category_id, budget_amount):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE ExpenseCategories SET Budget = ? WHERE CategoryId = ?", (budget_amount, category_id))
        connection.commit()
        print("Budget set successfully.")
    except sqlite3.Error as e:
        print(f"Error setting budget: {e}")


def view_category_budget(connection, category_id):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT CategoryName, Budget FROM ExpenseCategories WHERE CategoryId = ?", (category_id,))
        row = cursor.fetchone()
        if row:
            category_name, budget = row
            print(f"Category: {category_name}, Budget: {budget}")
        else:
            print("Category not found.")
    except sqlite3.Error as e:
        print(f"Error viewing category budget: {e}")


            

def main():
    connection = db_connect()
    create_tables(connection)
        
    while True:
        print("\n-- Finance Tracker --")
        print("1. Add new expense category")
        print("2. Delete expense category")
        print("3. Add expense")
        print("4. view expenses")
        print("5. Add new income category")
        print("6. Delete income category")
        print("7. Add income")
        print("8. View Income")
        print("9. View expense categories")
        print("10. View income categories")
        print("11. Calculate total budget")
        print("12. Set financial goal")
        print("13. view expense fincancial goals")
        print("14. View income financial goals")
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
            amount = float(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_expense(connection, date, description, amount, category_id)
        elif choice == '4':
            view_expenses(connection)
        elif choice == '5':
            category_name = input("Enter new income category name: ")
            add_income_category(connection, category_name)
        elif choice == '6':
            category_id = int(input("Enter ID of the income category to delete: "))
            delete_income_category(connection, category_id)
        elif choice == '7':
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = int(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_income(connection, date, description, amount, category_id)
        elif choice == '8':
            view_income(connection)
        elif choice == '9':
            view_expense_categories(connection)
        elif choice == '10':
            view_income_categories(connection)
        elif choice == '11':
             calculate_budget (connection)
        elif choice == '12':
            goal_type = input("Enter goal type (expense or income): ")
            category_id = int(input("Enter category ID: "))
            goal_amount = float(input("Enter financial goal amount: "))
            set_financial_goal(connection, category_id, goal_amount, goal_type)
        elif choice == '13':
            view_expense_financial_goal(connection)
        elif choice == '14':
            view_income_financial_goal(connection)
        elif choice == '15':
            category_id = int(input("Enter category ID: "))
            budget_amount = int(input("Enter budget amount: "))
            set_budget(connection, category_id, budget_amount)
        elif choice == '16':
            category_id = int(input("Enter category ID: "))
            view_category_budget(connection, category_id)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    connection.close()

if __name__ == "__main__":
    main()
