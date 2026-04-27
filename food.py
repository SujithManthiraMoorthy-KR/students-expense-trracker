import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

# Load existing data
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, etc): ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": date
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")

# View expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['note']} | {exp['date']}")

# Total expenses
def total_expense():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: ₹{total}")

# Filter by category
def filter_category():
    category = input("Enter category to filter: ")
    expenses = load_expenses()

    filtered = [exp for exp in expenses if exp["category"].lower() == category.lower()]

    if not filtered:
        print("No expenses found for this category.")
        return

    print(f"\n--- {category} Expenses ---")
    for exp in filtered:
        print(f"₹{exp['amount']} | {exp['note']} | {exp['date']}")

# Delete expense
def delete_expense():
    expenses = load_expenses()
    view_expenses()

    try:
        index = int(input("Enter expense number to delete: ")) - 1
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: ₹{removed['amount']} ({removed['category']})")
    except:
        print("Invalid selection!")

# Menu
def menu():
    while True:
        print("\n====== Student Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Filter by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            filter_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    menu()