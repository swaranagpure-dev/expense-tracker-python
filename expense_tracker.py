import csv
from datetime import date
expenses = []

def save_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "amount","category", "date"])
        writer.writeheader()
        writer.writerows(expenses)

def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "name": row["name"],
                    "amount": int(row["amount"]),
                    "category": row["category"],
                    "date": row["date"]
                })
    except FileNotFoundError:
        pass

def add_expenses():
    print("Add Expense Selected")
    expense_name = input("Enter Expense Name:")
    while True:
        try:
            amount = int(input("Enter amount:"))

            if amount > 0:
                break
            else:
                print("Invalid amount! Please enter a positive number.")

        except ValueError:
            print("Invalid amount! Please enter a valid number.")
    category = input("Enter category:").strip().title()
    expense_date = date.today().strftime("%d/%m/%Y")

    expense_data={"name":expense_name,
    "amount":amount, "category": category,  "date": expense_date}

    expenses.append(expense_data)
    save_expenses()

def view_expenses():
       
        if not expenses:
            print("No expenses found")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['name']} - ₹{expense['amount']} - {expense['category']} - {expense['date']}")

def view_total_expenses():
        print("View Total Selected")
        total=0
        for expense in expenses:
            total+=expense['amount']
        print("====== Total Expense ======")
        print("Total Expense:", total)

def view_summary():
    if not expenses:
        print("No expenses found")
    else:
        summary = {}

        for expense in expenses:
            category = expense["category"]
            amount = expense["amount"]

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

        print("====== Expense Summary ======")

        for category, total in summary.items():
            print(f"{category}: ₹{total}")

        print("-----------------------------")
        print("Total Expense:", sum(summary.values()))

def delete_expenses():
        if not expenses:
            print("No expenses!")
        else: 
            view_expenses()
            while True:
                try:
                    delete_expense = int(input("Enter expense number:"))

                    if 1 <= delete_expense <= len(expenses):
                        break
                    else:
                        print(f"Invalid number! Please enter a number between 1 and {len(expenses)}.")

                except ValueError:
                    print("Invalid input! Please enter a number.")
            deleted=expenses.pop(delete_expense - 1)
            save_expenses()
            print("Expense Deleted Successfully!" )
            print("Deleted Expenses:")
            print(f"{deleted['name']} - ₹{deleted['amount']} - {deleted['category']} - {deleted['date']}")
            print("Remaining expenses:")
            view_expenses()

load_expenses()
while True:
    print("======Expense Tracker======\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. View Summary")
    print("5. Delete Expense")
    print("6. Exit")
    while True:
        try:
            choice = int(input("Enter your choice:"))

            if 1 <= choice <= 6:
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input! Please enter a number.")
    if choice == 1:
        add_expenses()

    elif choice == 2:
        print("View Expenses Selected")
        view_expenses()

    elif choice == 3:
        view_total_expenses()

    elif choice == 4:
        view_summary()

    elif choice == 5:
        print("====== Delete expenses ======")
        delete_expenses()

    elif choice == 6:
        print("Thank You! Exiting...")
        break


