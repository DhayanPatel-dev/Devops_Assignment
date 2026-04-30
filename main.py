from datetime import datetime
expenses = []
budget = 0

def Add_expense():
    try:
        amt = float(input("Enter expense amount : "))
        if(amt<=0):
            print("Expense can't be less than zero..Try again..")
            return
    except:
        print("Invalid input..Try again")
        return
    
    category = input("Enter expense category(Food/travel/etc..) : ").lower()

    print("1. Use today's date")
    print("2. Enter custom date")

    choice = input("Choose option: ")

    if choice == "1":
        date = datetime.now().strftime("%Y-%m-%d")
    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except:
            print("Invalid date format!")
            return
    else:
        print("Invalid choice!")
        return
    
    expenses.append({"amount" : amt, "category" : category, "date" : date})
    print("Expense added successfully.")

def Show_expense():
    if not expenses:
        print("No expenses are there.")
        return
    else:
        for i,exp in enumerate(expenses,1):
            print(f"{i}. {exp['date']} | {exp['category'].capitalize()} : ₹{exp['amount']}")
    total = cal_total(expenses)
    print(f"Total Expenses : ₹{total}")

def Show_Cat_expense():
    total = {}
    if not expenses:
        print("No expenses are there.")
        return
    else:
        for exp in expenses:
            cat = exp['category']
            amt = exp['amount']

            if cat in total:
                total[cat] += amt
            else:
                total[cat] = amt

    print("\nHere yours category wise total.\n")

    for i,(cat,amt) in enumerate(total.items(),1):
        print(f"{i}. {cat.capitalize()} : ₹{amt}")

def Set_Budget():
    global budget
    try:
        budget = float(input("Enter monthly budget : "))

        if(budget <= 0):
            print("Budget can't be negative.")
            return
        else:
            print("Monthly budget set successfully.")
            return
    except:
        print("Invalid amount..Try again")
        return

def Show_Budget():
    total = 0
    for exp in expenses:
        total += exp['amount']

    print(f"Your total expenses : ₹{total}")

    if(budget == 0):
        print("Please set budget first.")
    elif(total>budget):
        print("Alert : Budget exceeded.")
    else:
        print("Within Budget.")

def Show_by_date():
    choice_date = input("Enter date (YYYY-MM-DD) : ")

    found = []

    for exp in expenses:
        if exp['date'] == choice_date:
            found.append(exp)

    if found:
        print(f"\nExpenses on {choice_date} are:\n")
        for exp in found:
            print(f"{exp['category'].capitalize()} : ₹{exp['amount']}")
        total = cal_total(found)
        print(f"Total Expenses : ₹{total}")
    else:
        print("No expenses found on this date.")

def cal_total(exp_list):
    total = 0
    for exp in exp_list:
        total += exp['amount']
    return total

i=0
while(i==0):
    print("\n Expense Tracker \n")
    print("1. Add Expense (food/travel/etc.)")
    print("2. View All Expenses")
    print("3. Show Category-Wise Total")
    print("4. Set Monthly Budget")
    print("5. Show Budget")
    print("6. Show Expenses by date")
    print("7. Exit")

    try:
        choice = int(input("Enter Your Choice : "))
    except:
        print("Invalid Choice..Try again.")
        continue

    if(choice == 1):
        Add_expense()
    elif(choice == 2):
        Show_expense()
    elif(choice == 3):
        Show_Cat_expense()
    elif(choice == 4):
        Set_Budget()
    elif(choice == 5):
        Show_Budget()
    elif(choice == 6):
        Show_by_date()
    elif(choice == 7):
        print("Exting...")
        i=1
    else:
        print("Something went wrong..Please try again..")