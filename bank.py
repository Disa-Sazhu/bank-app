# print("======== Admin Log In=======\n")
# name="Admin"
# password="Admin@123"
# a_name=input("Enter your Name: ")
# a_password=input("Enter the password: ")
# if a_name==name and a_password==password:
#     print("Authentification successful.Change your password for future login.")
#     user_name=input("Enter your User_ID: ")
#     new_password=input("Enter your new password :")
#     if new_password!=a_password:
#         print("Password changed successfully.")
        
#     else:
#         print("You can't use the same password given, create a diifrent password. ")
# else:
#     print("Authentification failed.Try again.")
# #==========================create customer function=========================
def create_customer():
        try:
            customer_id = input("Enter new customer_id: ")
            with open("customers.txt", "r") as file:
                existing_users = [line.split(",")[0].strip() for line in file.readlines()]
                if customer_id in existing_users:
                    print("customer_id already exists.")
                    return
        except FileNotFoundError:
            pass
        password = input("Enter password for new customer: ")
        with open("customers.txt", "a") as file:
            file.write(f"{customer_id},{password}\n")

        print(f"Customer '{customer_id}' created successfully!")
create_customer()
# #=========================create_account====================================
accounts = []
next_account_number = 1001

def create_account():
    global next_account_number
    name = input("Enter account holder name: ").strip()
    address = input("Enter account holder address: ").strip()
    date_of_birth = input("Enter account holder D.O.B (DD/MM/YYYY): ").strip()

    try:
        customer_id = input("Enter customer_id: ")
        age = int(input("Enter account holder age: "))
        initial_balance = float(input("Enter initial balance: "))
        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return None
    except ValueError:
        print("Invalid input for age or balance.")
        return None

    account_details = [
        next_account_number,
        customer_id,  
        name,
        address,
        date_of_birth,
        age,
        initial_balance
    ]

    next_account_number += 1
    accounts.append(account_details)  

    return account_details

account_details = create_account()
if account_details:
    with open("users.txt", "a") as file:
        file.write(f"({account_details[0]}, {account_details[1]}, {account_details[2]})\n")

    with open("userdetails.txt", "a") as file:
        file.write(f"({account_details[0]},{account_details[2]}, {account_details[3]}, {account_details[4]}, {account_details[5]})\n")

if account_details:
    print("Account created successfully!")
    print(f"Account Number: {account_details[0]}")
    print(f"Customer_iD: {account_details[1]}")
    print(f"Name: {account_details[2]}")
    print(f"Address: {account_details[3]}")
    print(f"D.O.B: {account_details[4]}")
    print(f"Age: {account_details[5]}")
    print(f"Balance: {account_details[6]}")
else:
    print("Account creation failed. Please try again with valid inputs.")
    

#=============================deposit function============================
def deposit(account_number, amount):
    global accounts

    if amount <= 0:
        print("Deposit amount must be positive.")
        return

    for account in accounts:
        if account[0] == account_number: 
            account[6] += amount  
            print(f"Deposit successful! New balance: {account[6]}")
            with open("userdetails.txt", "a") as file:
                file.write(f"({account[0]}, {account[2]}, {account[3]}, {account[4]}, {account[5]}, {account[6]})\n")

            return
    
    print("Account not found.")
# def deposit_money():
#     global next_account_number
#     for account_details in accounts:
#         if account_details[0] == next_account_number:
#             amount = float(input("Enter amount to deposit: "))
#             if amount <= 0:
#                 print("Deposit amount must be positive.")    
#                 account_details[6] += amount
#                 print(f"Deposit successful! New balance: {account_details[6]}")
#                 return
#     print("Account not found.")
# deposit_money()
        #     acc_num = int(input("Enter account number: "))
        #     if acc_num not in accounts:
        #         print("Account not found.")
        #         return
        #     
        #     accounts[acc_num]['balance'] += amount
        #     accounts[acc_num]['transactions'].append(f"Deposited {amount}")
        #     print(f"{amount} deposited successfully.")
        # except ValueError:
        #     print("Invalid input.")

# #==============================withdraw function=========================
# def withdraw_money():
#         try:
#             acc_num = int(input("Enter account number: "))
#             if acc_num not in accounts:
#                 print("Account not found.")
#                 return
#             amount = float(input("Enter amount to withdraw: "))
#             if amount <= 0:
#                 print("Withdrawal amount must be positive.")
#                 return
#             if amount > accounts[acc_num]['balance']:
#                 print("Insufficient balance.")
#                 return
#             accounts[acc_num]['balance'] -= amount
#             accounts[acc_num]['transactions'].append(f"Withdrew {amount}")
#             print(f"{amount} withdrawn successfully.")
#         except ValueError:
#             print("Invalid input.")

# #=======================money transfer function==============================
# def transfer_money():
#         try:
#                 acc_num = int(input("Enter your account number: "))
#                 if acc_num not in accounts:
#                     print("Account not found.")
#                     return
#                 acc_num=int(input("Enter receiver's account number: "))
#                 if acc_num not in accounts:
#                     print("Account not found.")
#                     return
#                 amount = float(input("Enter amount to transfer: "))
#                 if amount <= 0:
#                     print("Transfer amount must be positive.")
#                     return                   
#                 accounts[acc_num]['balance'] -= amount
#             accounts[acc_num]['transactions'].append(f"Transfer {amount}")
#             print(f"{amount} transfer successfully.")
#         except ValueError:
#             print("Invalid input.")

# #===================file handling=============================================
# with open("customers.txt", "a") as file:
#         file.write(f"{username},{password}\n")

# 
# #=======================================================================
# print("========Admin Menu========")
# print("1. Create Customer")
# print("2. Create Account")
# print("3.Deposit")
# print("4. Withdraw")
# print("5.Check Balance")
# print("6. Transfer Money")
# print("7. Transaction History")
# print("8. Change Intrest rate")
# print("9. Update Accounts Details")
# print("10. Logout")

# choice=("Enter a number from 1-7")
# if choice==1:
#     create_customer()
# elif choice==2:
#     create_account()
# elif choice==3:
#     deposit_money()
# elif choice==4:
#     withdraw_money()        
# elif choice==5:
#     check_balance()        
# elif choice==6:
#     transfer_money()       
# elif choice==7:
#     transaction_history()
# elif choice==8:
#     change_intrest_rate()
# elif choice==9:
#     update_account_details()
# elif choice==10:
#     print("Thanks for using the service.")
#     break
# else:
#     print("Invalid choice.")

# #====================================================================
# print("========Customer Menu========")
# print("1. Deposit")
# print("2. Withdraw")
# print("3. Transfer Money")
# print("4. Transaction History")
# print("5.Check Balance")
# print("6. View Interest rate")
# print("7. View All Accounts")
# print("8. Logout")

# choice=("Enter a number from 1-8")
# if choice==1:
#     deposit_money()
# elif choice==2:
#     withdraw_money()
# elif choice==3:
#     transfer_money()
# elif choice==4:
#     transaction_history()
# elif choice==5:
#     check_balance()
# elif choice==6:
#     view_intrest_rate()
# elif choice==7:
#     view_all_accounts()
# else choice==8:
#     print("Thanks for using the service.")
#    break
# else:
#     print("Invalid choice.")

# #=========================================================


 


