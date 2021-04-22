# Register
# - Username, password, email
# - Generate user account

# Login
# - Account Number, Password

# Bank Operations 
# Initializing the system
import random
import validation
import database
from getpass import getpass


def init():

    print("Welcome to Bank of Python! \n")

    have_account = int(input("Do you have an account with us: 1 = Yes, 2 = No \n"))
    
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected an invalid option.")
        init()

def login():
    print("**** Login ****")

    account_number_user = input("What is your Account Number? \n")
    
    # Validate the account number from user input
    is_valid_account_number = validation.account_number_validation(account_number_user)

    # If account number from user input passes, get password
    if is_valid_account_number:

        # Hiding the user's password when typing it in the commandline
        password = getpass("What is your password? \n")
        # Check if user's account number and password exist in the database
        user = database.authenticate_user(account_number_user, password)

        if user:
            # If the account number and password exist in the database, carry out bank operations
            bank_operations(user)

        print("Invalid Account Number or Password")
        login()

    else:
        # Account number from user input didn't pass validation
        print("Account Number Invalid: Check that you have up to 10 digits.")
        init()

def register():
    print("**** Registration ****")
    # Get new user's information
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    
    # Hiding the user's password when typing it in the commandline
    password = getpass("Create a password. \n")
    
    # Generate a random 10-digit number for bank account
    account_number = generate_account_number()
    
    # Use the database module to create new user record
    # Create a new file in the database
    is_user_created = database.create(account_number, first_name, last_name, email, password)

    # Login to account after account has been created
    if is_user_created:

        print("Your Account has been created.")
        print(" ======= =============== =======")
        print("Your Account Number is %d" % account_number)
        print("Make sure you keep it safe.")
        print(" ======= =============== =======")

        login()

    else:
        print("Something went wrong, please try again.")
        register()

def bank_operations(user):
    print("Welcome %s %s" % (user[0], user[1]))

    try:
        selected_option = int(input("What would you like to do? \n(1) Deposit (2) Withdrawl (3) Logout (4) Exit \n"))
    
        if (selected_option == 1):
            deposit_operation()
        elif(selected_option == 2):
            withdrawal_operation(user)
        elif(selected_option == 3):
            logout()
        elif(selected_option == 4):
            exit()
        else:
            print("Invalid option selected.")
            bank_operations(user)
    
    except ValueError:
        print("You must enter a valid option. ")
        bank_operations(user)

def withdrawal_operation(user_details):
    print("**** Withdrawal ****")

    # Get current balance
    # Get widthdrawal amount
    # Check if current balance > withdrawal amount
    # Deduct withdrawal amount from current balance
    # Display current balance
    currentBalance = user_details[4]

    try:
        withdrawalAmt = int(input("What amount would you like to withdraw? \n"))

        if currentBalance > withdrawalAmt:
            currentBalance -= withdrawalAmt
            user_details[4] = currentBalance

            # Need to actually update the database with the new account balance

            print("Current Balance: %d" % user_details[4])
        else:
            print("Insufficient funds for withdrawal transaction.")
            bank_operations(user_details)

    except ValueError:
        print("You must enter a valid number.")
        withdrawal_operation(user_details)

def deposit_operation():
    print("**** Deposit ****")

    # Get current balance
    # Get deposit amount
    # Add deposit amount to current balance
    # Display current balance

def generate_account_number():
    return random.randrange(1111111111, 9999999999)

def get_current_balance(user_details):
    return user_details[4]

def logout():
    login()

#### ACTUAL BANKING SYSTEM ####
init()
