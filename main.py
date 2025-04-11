import auth
import expense_manager as em
import summary
import excel_exporter

def main():
    print("Welcome to Expense Tracker!")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            auth.register_user()
        elif choice == "2":
            user = auth.login_user()
            if user:
                user_menu(user)
        else:
            break

def user_menu(username):
    while True:
        print("\n1. Add Expense\n2. View by Category\n3. Edit Category\n4. Delete Category")
        print("5. Monthly Summary\n6. Summary by Date Range\n7. Export to Excel\n8. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            em.add_expense(username)
        elif choice == "2":
            em.view_expenses_by_category(username)
        elif choice == "3":
            em.edit_category(username)
        elif choice == "4":
            em.delete_category(username)
        elif choice == "5":
            summary.monthly_summary(username)
        elif choice == "6":
            summary.summary_by_date_range(username)
        elif choice == "7":
            excel_exporter.export_to_excel(username)
        elif choice == "8":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()