print("======== Admin Log In=======\n")
U_name="Author"
U_Password="Author123"
Username=input("Enter the Username :")
Password=input("Enter the Password :")

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
    Create Customer()
elif choice==2:
    Create Account()
elif choice==3:
    Deposit()
elif choice==4:
    Withdraw()
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
    def Deposit()
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
name=input("Enter Name :")
address=input("Enter Address:")
date_of_birth=input("Enter D.O.B :")
age=int(input("Enter Age :"))
Username=input("Enter username :")
password=input("Enter password :")

def create_customers_and_users():
    Customers=get_customer_info()
   with open('users.txt','a')
