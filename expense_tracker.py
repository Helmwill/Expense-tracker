import sqlite3 

def db_connect():
    connection = sqlite3.connect('finance_tracker.db')
    return connection 

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
    FOREIGN KEY (CATEGORYID) REFERENCES ExpenseCategories(categoryID)
        )
    ''')

    cursor.execute('''
        CREATE TEABLE IF NOT EXISTS IncomeCategories (
            CategoryID INTEGER PRIMARYKEY,
            CategoryName TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Income (
            IncomeID INTEGER PRIMARY KEY,
            Date TEXT,
            Description TEXT<
            Amount INTEGER,
            CategoryID INTEGER,
            FOREIGN KEY (CategoryID) REFERENCES IncomeCategories(CategoryID)
                )
            ''')
        connection.commit()


        cursor.execute("SELECT COUNT (*) FROM expenses")
        count = cursor.fetchone()[0]

        if count == 0:
            example_values = [
                ('22-07-28', "dinner out", 0, 27,),
                ('22-07-28', "monthly pay main job", 3000, 0),
                ('22-07-31', "holiday paid", 0, 1279),
                ('22-08-06', "weekly shop", 0, 125),
            ]
            cursor.executemany('INSERT INTO expenses(Date, Description, Income, Expenses) VALUES (?,?,?,?)', example_values)
            ft_db.commit()
            print("Expense examples added to the database")
        else:
            print("Records already exist in the database")
