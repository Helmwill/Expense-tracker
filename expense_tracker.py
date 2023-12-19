import sqlite3 
import datetime

menu = ''
try:
    with sqlite3.connect('finance_tracker.db') as ft_db:
        cursor = ft_db.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
        Date INTEGER  
        Description TEXT
        Income INTEGER
        Expenses INTEGER
        Overall balance INTEGER)
        ''')
        ft_db.commit()

        cursor.execute("SELECT COUNT (*) FROM book")
        count = cursor.fethcone()[0]

        if count == 0:
            example_values = [
                (22/07/28, "dinner out", 0, 27,),
                (22/07/28, "monthly pay main job", 3000, 0),
                (22/07/31, "holiday paid", 0, 1279),
                (22/08/06, "weekly shop", 0, 125),
            ]
            cursor.executemany('INSERT INTO expenses(Date, Description, Income, Expenses) VALUES (?,?,?,?)', example_values)
            ft_db.commit()
            print("Expense examples added to the database")
        else:
            print("Records already exist in the database")
except Exception as e:   
        print(f"An error occurred: {e}")