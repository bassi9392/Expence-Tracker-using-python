import mysql.connector
from datetime import datetime

def connect():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="Your_UserName",
        password="Your_Password",
        database="expense_tarcker"
    )

def add_expense(category, description, amount, date=None):
    db = connect()
    cursor = db.cursor()
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
        print(date)
    sql = "INSERT INTO expenses (category, description, amount, expense_date) VALUES (%s, %s, %s, %s)"
    print("\n SQL STATEMENT is ", sql);
    values = (category, description, amount, date)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()
    print("Expense added successfully.")

def view_expenses():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT id, category, description, amount, expense_date FROM expenses ORDER BY id DESC")
    records = cursor.fetchall()
    print("All Expenses:")
    for row in records:
        print(f"ID: {row} | {row[1]} | {row[2]} | Rs. {row[3]} | {row[4]}")
    cursor.close()
    db.close()

def summary():
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    records = cursor.fetchall()
    print("Expense Summary by Category:")
    for row in records:
        print(f"{row}: Rs. {row[1]:.2f}")
    cursor.close()
    db.close()

def menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            category = input("Category: ")
            description = input("Description: ")
            amount = float(input("Amount: "))
            date = input("Date (YYYY-MM-DD, optional): ")
            add_expense(category, description, amount, date if date else None)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
