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

        #ExpenseCategories table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExpenseCategories (
            CategoryId INTEGER PRIMARY KEY, 
            CategoryName TEXT,
            Budget INTEGER,
            FinancialGoal INTEGER
        )
    ''')
        #Expenses table
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
        #IncomeCategories table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS IncomeCategories (
            CategoryID INTEGER PRIMARY KEY,
            CategoryName TEXT,
            Budget INTEGER,
            FinancialGoal INTEGER
        )
    ''')
        #Income table
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
        #commit the changes
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
def add_expense_category(connection, category_name):
    """
    This function adds a new expense category to the ExpenseCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_name (str): The name of the expense category to be added.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO ExpenseCategories(CategoryName) VALUES (?)", (category_name,))
        connection.commit()
        print(f"Expense category '{category_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding expense category: {e}")

def delete_expense_category(connection, category_id):
    """
    This function deletes an expense category from the ExpenseCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_id (int): The ID of the expense category to be deleted.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ExpenseCategories WHERE CategoryId = ?", (category_id,))
        connection.commit()
        print("Expense category deleted successfully")
    except sqlite3.Error as e:
        print(f"Error deleting expense category: {e}")

def add_expense(connection, date, description, amount, category_id):
    """
    This function adds a new expense to the Expenses table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    date (str): The date of the expense.
    description (str): The description of the expense.
    amount (int): The amount of the expense.
    category_id (int): The ID of the expense category.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Expenses(Date, Description, Amount, CategoryID) VALUES (?,?,?,?)",
            (date, description, amount, category_id))
        connection.commit()
        print("Expense added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding expense: {e}")

def add_income_category(connection, category_name): 
    """
    This function adds a new income category to the IncomeCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_name (str): The name of the income category to be added.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO IncomeCategories(CategoryName) VALUES (?)", (category_name,))
        connection.commit()
        print(f"Income category '{category_name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding income category: {e}")

def delete_income_category(connection, category_id):
    """
    This function deletes an income category from the IncomeCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_id (int): The ID of the income category to be deleted.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM IncomeCategories WHERE CategoryID = ?", (category_id,))
        connection.commit()
        print("Income category deleted successfully.")
    except sqlite3.Error as e:
        print(f"Error deleting income category: {e}")

def add_income(connection, date, description, amount, category_id):
    """
    This function adds a new income to the Income table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    date (str): The date of the income.
    description (str): The description of the income.
    amount (int): The amount of the income.
    category_id (int): The ID of the income category.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Income(Date, Description, Amount, CategoryID) VALUES (?,?,?,?)", 
                        (date, description, amount, category_id))
        connection.commit()
        print("Income added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding income: {e}")

def view_expense_categories(connection):
    """
    This function retrieves and prints all expense categories from the ExpenseCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    None
    """
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
    """
    This function retrieves and prints all income categories from the IncomeCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    None
    """
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
    """
    This function calculates the budget by subtracting the total expenses from the total income.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    float: The calculated budget.
    """
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
    """
    This function retrieves and prints all expenses from the Expenses table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    None
    """
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
    """
    This function retrieves and prints all income from the Income table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    None
    """
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
    """
    This function sets a financial goal for a specific category in the ExpenseCategories or IncomeCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_id (int): The ID of the category.
    goal_amount (float): The financial goal amount to be set.
    goal_type (str): The type of the goal, either 'expense' or 'income'.

    Returns:
    None
    """
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
    """
    This function retrieves and prints the financial goals for all expense categories from the ExpenseCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    None
    """
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
    """
    This function retrieves and prints the financial goals for all income categories from the IncomeCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.

    Returns:
    None
    """
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
    """
    This function sets the budget for a specific expense category in the ExpenseCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_id (int): The ID of the expense category.
    budget_amount (float): The budget amount to be set.

    Returns:
    None
    """
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE ExpenseCategories SET Budget = ? WHERE CategoryId = ?", (budget_amount, category_id))
        connection.commit()
        print("Budget set successfully.")
    except sqlite3.Error as e:
        print(f"Error setting budget: {e}")


def view_category_budget(connection, category_id):
    """
    This function retrieves and prints the budget for a specific expense category from the ExpenseCategories table.

    Parameters:
    connection (sqlite3.Connection): The connection object to the SQLite database.
    category_id (int): The ID of the expense category.

    Returns:
    None
    """
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
    """
    This function is the main entry point of the program. It connects to the database, creates the necessary tables,
    and provides a menu for the user to interact with the finance tracker.

    Parameters:
    None

    Returns:
    None
    """
    #connect to the database
    connection = db_connect()
    #create the tables if they do not already exist
    create_tables(connection)
        
    while True:
        #print the menu options
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

        #Users selects what they want to do
        choice = input("Enter your choice: ")

        #perform the selected action 
        if choice == '1':
            #add new expense category
            category_name = input("Enter new expense category name: ")
            add_expense_category(connection, category_name)
        elif choice == '2':
            #delete expense category
            category_id = int(input("Enter ID of the expense category to delete: "))
            delete_expense_category(connection, category_id)
        elif choice == '3':
            #add expense
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_expense(connection, date, description, amount, category_id)
        elif choice == '4':
            #view expenses
            view_expenses(connection)
        elif choice == '5':
            #add new income category
            category_name = input("Enter new income category name: ")
            add_income_category(connection, category_name)
        elif choice == '6':
            #delete income category
            category_id = int(input("Enter ID of the income category to delete: "))
            delete_income_category(connection, category_id)
        elif choice == '7':
            #add income
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = int(input("Enter amount: "))
            category_id = int(input("Enter category ID: "))
            add_income(connection, date, description, amount, category_id)
        elif choice == '8':
            #view income
            view_income(connection)
        elif choice == '9':
            #view expense categories
            view_expense_categories(connection)
        elif choice == '10':
            #view income categories
            view_income_categories(connection)
        elif choice == '11':
            #calculate total budget
             calculate_budget (connection)
        elif choice == '12':
            #set financial goal
            goal_type = input("Enter goal type (expense or income): ")
            category_id = int(input("Enter category ID: "))
            goal_amount = float(input("Enter financial goal amount: "))
            set_financial_goal(connection, category_id, goal_amount, goal_type)
        elif choice == '13':
            #view expense financial goals
            view_expense_financial_goal(connection)
        elif choice == '14':
            #view income financial goals
            view_income_financial_goal(connection)
        elif choice == '15':
            #set budget
            category_id = int(input("Enter category ID: "))
            budget_amount = int(input("Enter budget amount: "))
            set_budget(connection, category_id, budget_amount)
        elif choice == '16':
            #view category budget
            category_id = int(input("Enter category ID: "))
            view_category_budget(connection, category_id)
        elif choice == '0':
            #exit the program
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    #close the connection to the database
    connection.close()
#call the main function
if __name__ == "__main__":
    main()
