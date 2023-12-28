import sqlite3 

#creating & enabling conection
def db_connect():
    connection = sqlite3.connect('finance_tracker.db')
    return connection 

#create tables if they do not alrerady exist 
def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ExpenseCategories (
            CategoryId INNTEGER PRIMARY KEY, 
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
    FOREIGN KEY (CategoryID) REFERENCES ExpenseCategories(categoryID)
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

def add_expense_category(connection, category_name):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO ExpenseCategories(CategoryName) VALUES (?)", (category_name))
    connection.commit()
    print(f"Expense category '{category_name}' added successfully.")

def delete_expense_category(connection, category_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM ExpenseCategories WHERE Category = ?", (category_id,))
    connection.commit()
    print("Expense category deleted successfully")

def add_expense(connection, date, description, amount, category_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Expenses(Date, Description, Amount, CategoryID) VALUES (?,?,?,?)",
        (date, description, amount, category_id))
    connection.commit()
    print("Expense added successfully.")

def add_income_category(connection, category_name): 
    cursor = connection.cursor()
    cursor.execute("INSERT INTO IncomeCategories(CategoryName) VALUES (?)", (category_name))
    connection.commit()
    print(f"Expense category '{category_name} added successfully.")

def delete_income_category(connection, category_id):
    cursor=connection.cursor()
    cursor.execute("DELETE FROM IncomeCategories WHERE CategoryID = ?", (category_id))
    connection.commit()
    print("Income category deleted successfully.")

def add_income(connection, date, description, amount, category_id):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Income(Date, Description, Amount, CategoryID) VALUES (?,?,?,?)", 
                    (date, description, amount, category_id))
    connection.commit()
    print("Income added successfully.")

def view_expense_categories(conne)