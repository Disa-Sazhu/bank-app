# print("======== Admin Log In=======\n")
# users = {"admin": {"password": "onetwothreefour", "role": "admin", "password_changed": False}}
# a_name=input("Enter your Name: ")
# password=input("Enter the password: ")
# if password==

#==========================create customer function=========================
def create_customer():
        username = input("Enter new customer's username: ")
        if username in users:
            print("Username already exists.")
            return
        password = input("Enter password for new customer: ")
        customer_details=create_customer()
        print(customer_details)
#=========================create_account====================================
def create_account():
        global next_account_number
        name = input("Enter account holder name: ").strip()
        address=input("Enter account holder address: ").strip()
        d_o_b=input("Enter account holder D.O.B: DD/MM/YYYY ")
    try:
        age = int(input("Enter account holder age: "))
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return None
    except ValueError:
        print("Invalid input for age or balance.")
        return None

    account_details = {
        "account_number": next_account_number,
        "name": name,
        "address": address,
        "date_of_birth": d_o_b,
        "age": age,
        "balance": initial_balance
    }

    next_account_number += 1
    accounts.append(account_details)  
    return account_details

       
user_details = create_account()
if user_details:
    print("Account created successfully!")
    print(user_details)

#=============================deposit function============================
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

#==============================withdraw function=========================
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

#=======================money transfer function==============================
def transfer_money():
        try:
                acc_num = int(input("Enter account number: "))
                if acc_num not in accounts:
                    print("Account not found.")
                    return
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Transfer amount must be positive.")
                    return                   


#===================file handling=============================================
with open("customers.txt","a") as file:
    file.write(f"{customer_details[0]},{customer_details[1]}")

with open("users.txt","a") as file:
    file.write(f"({user_details[0]},{user_details[1]},{user_details[2]},{user_details[3]})")

#=======================================================================
print("========Admin Menu========")
print("1. Create Customer")
print("2. Create Account")
print("3.Deposit")
print("4. Withdraw")
print("5.Check Balance")
print("6. Transfer Money")
print("7. Transaction History")
print("8. Change Intrest rate")
print("9. Update Accounts Details")
print("10. Logout")

choice=("Enter a number from 1-7")
if choice==1:
    # accounts = {}
    # next_account_number = 1001
    create_customer()

elif choice==2:
    create_account()
elif choice==3:
    deposit_money()
elif choice==4:
    withdraw_money()        
elif choice==5:
    check_balance()        
elif choice==6:
    transfer_money()       
elif choice==7:
    Transaction_History()
elif choice==8:
    Change Intrest_rate()
elif choice==9:
    Update Accounts_Details()
elif choice==10:
    print("Thanks for using the service.")
    break
else:
    print("Invalid choice.")

#====================================================================
print("========Customer Menu========")
print("1. Deposit")
print("2. Withdraw")
print("3. Transfer Money")
print("4. Transaction History")
print("5. View Interest rate")
print("6. View All Accounts")
print("7. Logout")

choice=("Enter a number from 1-7")
if choice==1:
    deposit_money()
elif choice==2:
    withdraw_money()
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

#=========================================================


 


