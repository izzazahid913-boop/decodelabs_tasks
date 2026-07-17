import csv
from datetime import datetime


FILE_NAME = "expenses.csv"


def add_expense(amount, category, description):
    try:
        amount = float(amount)

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        if category.strip() == "" or description.strip() == "":
            print("Category and description cannot be empty!")
            return

        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, amount, category, description])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number for amount!")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            next(reader)

            print("\n" + "-" * 70)
            print("No.\tDate\t\tAmount\t\tCategory\tDescription")
            print("-" * 70)

            count = 1

            for row in reader:
                print(f"{count}\t{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")
                count += 1

            print("-" * 70)

    except FileNotFoundError:
        print("No expenses found!")


def calculate_total():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            next(reader)  # Skip CSV heading

            for row in reader:
                total += float(row[1])

        print(f"Total Expense: {total}")

    except FileNotFoundError:
        print("No expenses found!")
def delete_expense(index):
    try:
        with open(FILE_NAME, "r") as file:
            rows = list(csv.reader(file))

        if index >= len(rows) - 1 or index < 1:
            print("Invalid expense number!")
            return

        rows.pop(index)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Expense deleted successfully!")

    except FileNotFoundError:
        print("No expenses found!")