from expense_tracker import add_expense, view_expenses, calculate_total, delete_expense


def menu():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter description: ")

            add_expense(amount, category, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            index = int(input("Enter expense number to delete: "))
            delete_expense(index)

        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Try again.")


menu()