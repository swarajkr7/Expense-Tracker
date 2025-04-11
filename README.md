# 💰 Personal Expense Tracker (Console-Based Python Project)

A console-based application to help users manage and track personal expenses with support for multiple users, Excel export, date-based filtering, and more. This project uses **file handling**, **modular structure**, and visual enhancements using `colorama`.

---

## 📌 Project Description

This is a personal expense tracker written in Python designed for students to demonstrate file handling and object-oriented programming concepts. It allows multiple users to register, log in, add/view/edit expenses, generate monthly summaries, export to Excel, and more.

---

## 🚀 Features Implemented

- ✅ User Registration & Login (with password hashing)
- ✅ Add Expenses by Category
- ✅ View Expenses Categorically
- ✅ Edit/Delete Categories
- ✅ Monthly Summary
- ✅ Filter Expenses by Date Range
- ✅ Pie Chart of Category-wise Expenses (`matplotlib`)
- ✅ Export Expenses to Excel (`openpyxl`)
- ✅ Data persistence via `expenses.txt` & `users.txt`
- ✅ Modular code structure (auth.py, summary.py, etc.)

---

## 🛠 How to Run the Project

### 1. Clone the repository or download the ZIP
```bash
git clone https://github.com/swarajkr7/Expense-Tracker.git
cd ExpenseTracker
```

### 2. Install dependencies
Make sure you have Python 3 installed. Then install required libraries:

```bash
pip install -r requirements.txt
```

Alternatively, manually install:
```bash
pip install matplotlib openpyxl colorama
```

### 3. Run the program
```bash
python main.py
```

---

## 📦 Project Structure

```
ExpenseTracker/
├── auth.py
├── expense_manager.py
├── summary.py
├── excel_exporter.py
├── utils.py
├── main.py
├── expenses.txt
├── users.txt
├── requirements.txt
└── README.md
```

---

## 📝 Installation Notes

- Tested on **Python 3.8+**
- Compatible with Windows, Linux, and macOS terminals
- Uses only standard and popular external libraries

---


## 🙋‍♂️ Created By

**Sswaraj Kumar**  
Final Year, B.Tech in Computer Engineering  
Mizoram University  
