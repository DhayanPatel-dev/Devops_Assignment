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
    
    category = input("Enter expense category(Food/travel/etc..) : ")
    expenses.append({"amount" : amt, "category" : category})
    print("Expense added successfully.")

def Show_expense():
    if not expenses:
        print("No expenses are there.")
        return
    else:
        for i,exp in enumerate(expenses,1):
            print(f"{i}. {exp['category']} : ₹{exp['amount']}")

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
        print(f"{i}. {cat} : ₹{amt}")

def Set_Budget():
    global budget
    try:
        budget = float(input("Enter monthly budget : "))
        print("Monthly budget set successfully.")
        return
    except:
        print("Invalid amount..Try again")
        return

def Show_Budget():
    total = 0
    for exp in expenses:
        total += exp['amount']

    print(f"Your total epenses : ₹{total}")

    if(budget>0 and total>budget):
        print("Alert : Budget exceeded.")
    else:
        print("Within Budget.")

i=0
while(i==0):
    print("\n Expense Tracker \n")
    print("1. Add Expense (food/travel/etc.)")
    print("2. View All Expenses")
    print("3. Show Category-Wise Total")
    print("4. Set Monthly Budget")
    print("5. Show Budget")
    print("6. Exit")

    choice = int(input("Enter Your Choice : "))

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
        print("Exting...")
        i=1
    else:
        print("Something went wrong..Please try again..")