print("======== Admin Log In=======\n")
users = {"admin": {"password": "onetime123", "role": "admin", "password_changed": False}}
#==================================================================
print("========Admin Menu========")
print("1. Create Customer")
print("2. Create Account")
print("3.Deposit")
print("4. Withdraw")
print("5. Transfer Money")
print("6. Transaction History")
print("7. Change Intrest rate")
print("8. Update Accounts Details")
print("9. Logout")


choice=("Enter a number from 1-7")
if choice==1:
    accounts = {}
    next_account_number = 1001
    def create_customer()
    username = input("Enter new customer's username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter password for new customer: ")
    users[username] = {
        "password": password,
        "role": "customer",
        "first_login": False
    }
    save_users(users)
    print(f"Customer account '{username}' created successfully.")
        create_customer()

elif choice==2:
    def create_account():
    global next_account_number
    name = input("Enter account holder name: ").strip()
    address=input("Enter account holder address: ").strip()
    d_o_b=input("Enter account holder D.O.B: DD/MM/YYYY ")
    age=int(input("Enter account holder age:"))
    try:
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    account_number = next_account_number
    next_account_number += 1

    accounts[account_number] = {
        'name': name,
        'address': address,
        'date_of_birth': d_o_b,
        'age': age,
        'balance': initial_balance,
        'transactions': [f"Account created with balance {initial_balance}"]
    }
        create_account()

elif choice==3:
    def deposit_money():
    try:
        acc_num = int(input("Enter account number: "))
        if acc_num not in accounts:
            print("Account not found.")
            return
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        accounts[acc_num]['balance'] += amount
        accounts[acc_num]['transactions'].append(f"Deposited {amount}")
        print(f"{amount} deposited successfully.")
    except ValueError:
        print("Invalid input.")
        deposit_money()
elif choice==4:
    def withdraw_money():
    try:
        acc_num = int(input("Enter account number: "))
        if acc_num not in accounts:
            print("Account not found.")
            return
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > accounts[acc_num]['balance']:
            print("Insufficient balance.")
            return
        accounts[acc_num]['balance'] -= amount
        accounts[acc_num]['transactions'].append(f"Withdrew {amount}")
        print(f"{amount} withdrawn successfully.")
    except ValueError:
        print("Invalid input.")
        withdraw_money()()
elif choice==5:
    Transfer Money()
elif choice==6:
    Transaction History()
elif choice==7:
    Change Intrest rate()
elif choice==8:
    Update Accounts Details()
elif choice==9:
    print("Thanks for using the service.")
    break
else:
    print("Invalid choice.")
'''
#====================================================================
print("========Customer Menu========")
print("1. Deposit")
print("2. Withdraw")
print("3. Transfer Money")
print("4. Transaction History")
print("5. View Interest rate")
print("6. View All Accounts")
print("7. Logout")
'''
choice=("Enter a number from 1-7")
if choice==1:
    def deposit_money():
    try:
        acc_num = int(input("Enter account number: "))
        if acc_num not in accounts:
            print("Account not found.")
            return
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        accounts[acc_num]['balance'] += amount
        accounts[acc_num]['transactions'].append(f"Deposited {amount}")
        print(f"{amount} deposited successfully.")
    except ValueError:
        print("Invalid input.")
        deposit_money()
elif choice==2:
    def Withdraw()
elif choice==3:
    def Transfer Money()
elif choice==4:
    def Transaction History()
elif choice==5:
    def View Intrest rate()
elif choice==6:
    print("Thanks for using the service.")
    break
else:
    print("Invalid choice.")
''''
#=========================================================

    
 '''
    #=======

