import os
from utils import validate_date

EXPENSE_FILE = "expenses.txt"

def add_expense(username):
    category = input("Enter category: ")
    amount = input("Enter amount: ")
    date = input("Enter date (YYYY-MM-DD): ")
    if not validate_date(date):
        print("Invalid date format.")
        return
    with open(EXPENSE_FILE, "a") as f:
        f.write(f"{username},{category},{amount},{date}\n")
    print("Expense added successfully!")

def view_expenses_by_category(username):
    from collections import defaultdict
    data = defaultdict(list)
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            u, cat, amt, d = line.strip().split(",")
            if u == username:
                data[cat].append((amt, d))
    for cat, items in data.items():
        print(f"{cat}:")
        for amt, d in items:
            print(f"  Amount: {amt} - Date: {d}")
        print()

def edit_category(username):
    old_cat = input("Enter category to rename: ")
    new_cat = input("Enter new category name: ")
    updated = []
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            u, cat, amt, date = line.strip().split(",")
            if u == username and cat == old_cat:
                cat = new_cat
            updated.append(f"{u},{cat},{amt},{date}")
    with open(EXPENSE_FILE, "w") as f:
        for line in updated:
            f.write(line + "\n")
    print("Category updated successfully.")

def delete_category(username):
    del_cat = input("Enter category to delete: ")
    updated = []
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            u, cat, amt, date = line.strip().split(",")
            if not (u == username and cat == del_cat):
                updated.append(f"{u},{cat},{amt},{date}")
    with open(EXPENSE_FILE, "w") as f:
        for line in updated:
            f.write(line + "\n")
    print("Category deleted successfully.")