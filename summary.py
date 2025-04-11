import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

EXPENSE_FILE = "expenses.txt"

def monthly_summary(username):
    month = input("Enter month (1-12): ")
    year = input("Enter year (YYYY): ")
    total = 0
    by_cat = defaultdict(int)
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            u, cat, amt, d = line.strip().split(",")
            date = datetime.strptime(d, "%Y-%m-%d")
            if u == username and date.month == int(month) and date.year == int(year):
                total += float(amt)
                by_cat[cat] += float(amt)
    print(f"Monthly Summary ({year}-{month.zfill(2)}):")
    print(f"Total: {total}")
    for cat, amt in by_cat.items():
        print(f"{cat}: {amt}")
    generate_pie_chart(by_cat)

def summary_by_date_range(username):
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    total = 0
    by_cat = defaultdict(int)
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            u, cat, amt, d = line.strip().split(",")
            date = datetime.strptime(d, "%Y-%m-%d")
            if u == username and start <= date <= end:
                total += float(amt)
                by_cat[cat] += float(amt)
    print(f"Summary from {start.date()} to {end.date()}:")
    print(f"Total: {total}")
    for cat, amt in by_cat.items():
        print(f"{cat}: {amt}")
    generate_pie_chart(by_cat)

def generate_pie_chart(data):
    if not data:
        print("No data to display in chart.")
        return
    labels = data.keys()
    sizes = data.values()
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()