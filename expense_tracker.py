expenses=[]


def add_expenses():
        print("Add Expense Selected")
        expense_name=input("Enter Expense Name:")
        amount=int(input("Enter amount:"))
        expense_data={"name":expense_name,
        "amount":amount}
        expenses.append(expense_data)
def view_expenses():
       
        if not expenses:
            print("No expenses found")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(f"{index}. {expense['name']}:{expense['amount']}")
def view_total_expenses():
        print("View Total Selected")
        total=0
        for expense in expenses:
            total+=expense['amount']
        print("====== Total Expense ======")
        print("Total Expense:", total)
def delete_expenses():
        if not expenses:
            print("No expenses!")
        else:
            view_expenses()
            delete_expense=int(input("Enter expense number:"))
            if delete_expense <= 0 or delete_expense > len(expenses):
                print("Invalid number")
            else:
                deleted=expenses.pop(delete_expense - 1)
                print("Expense Deleted Successfully!" )
                print("Deleted Expenses:")
                print(f"{deleted['name']}:{deleted['amount']}")
                print("Remaining expenses:")
                view_expenses()
while True:
    print("======Expense Tracker======\n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Delete Expense")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        add_expenses()

    elif choice == 2:
        print("View Expenses Selected")
        view_expenses()

    elif choice == 3:
        view_total_expenses()

    elif choice == 4:
        print("====== Delete expenses ======")
        delete_expenses()
    elif choice == 5:
        print("Thank You! Exiting...")
        break
    else:
        print("Invalid Choice")
        

