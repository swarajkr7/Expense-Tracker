import pandas as pd

EXPENSE_FILE = "expenses.txt"

def export_to_excel(username):
    data = []
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            u, cat, amt, date = line.strip().split(",")
            if u == username:
                data.append({"Category": cat, "Amount": amt, "Date": date})
    df = pd.DataFrame(data)
    filename = f"{username}_expenses.xlsx"
    df.to_excel(filename, index=False)
    print(f"Exported to {filename}")