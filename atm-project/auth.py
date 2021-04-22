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
from datetime import datetime
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
            # Need to create file in auth_session/ here
            current_date_time = datetime.now()
            formatted_date_time = current_date_time.strftime("%m/%d/%y %H:%M:%S")
            #print("Last login at %s \n" % formatted_date_time) 
            latest_login = database.user_login_timestamp(account_number_user, formatted_date_time)
            # If the account number and password exist in the database, carry out bank operations
            bank_operations(account_number_user, user)
        else:
            print("Invalid Account Number or Password.")
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

def bank_operations(account_number_user, user):
    print("Welcome %s %s" % (user[0], user[1]))

    try:
        selected_option = int(input("What would you like to do? \n(1) Deposit (2) Withdrawl (3) Logout (4) Exit \n"))
    
        if selected_option == 1:
            deposit_operation(account_number_user, user)
        elif selected_option == 2:
            withdrawal_operation(account_number_user, user)
        elif selected_option == 3:
            logout(account_number_user)
        elif selected_option == 4:
            exit()
        else:
            print("Invalid option selected.")
            bank_operations(account_number_user, user)
    
    except ValueError:
        print("You must enter a valid option. ")
        bank_operations(account_number_user, user)

def withdrawal_operation(account_number_user, user_details):
    print("**** Withdrawal ****")
    # Get current balance
    # Get widthdrawal amount
    # Check if current balance > withdrawal amount
    # Deduct withdrawal amount from current balance
    # Display current balance

    # User details comes in as a list --> need to convert bank into a comma-separated string
    current_balance = int(user_details[4])

    try:
        withdrawal_amt = int(input("What amount would you like to withdraw? \n"))

        if current_balance > withdrawal_amt:
            # Update balance 
            current_balance -= withdrawal_amt
            # Convert bank to a comma separated string
            user_details[4] = str(current_balance)
            converted_user_details = [str(element) for element in user_details]
            joined_user_details = ",".join(converted_user_details)

            # Write the updated balance to the file
            update_user_balance = database.update_user_balance(account_number_user, joined_user_details)

            if update_user_balance:
                print("Current Balance: %d" % current_balance)
                bank_operations(account_number_user, user_details)
        else:
            print("Insufficient funds for withdrawal transaction.")
            bank_operations(account_number_user, user_details)

    except ValueError:
        print("You must enter a valid number.")
        withdrawal_operation(account_number_user, user_details)

def deposit_operation(account_num_user, user_info):
    print("**** Deposit ****")

    # Get current balance
    # Get deposit amount
    # Add deposit amount to current balance
    # Display current balance

    # user_info comes in as a list
    # need to convert bank to a comma-separated string then write to file

    current_acct_balance = int(user_info[4])

    try:
        deposit_amt = int(input("What amount would you like to deposit?"))
        # Deposit amount
        current_acct_balance += deposit_amt
        # Convert new balance to comma-separated string
        user_info[4] = str(current_acct_balance)
        convert_user = [str(ele) for ele in user_info]
        join_user = ",".join(convert_user)

        # Write the user info with updated balance to the file
        updated_balance = database.update_user_balance(account_num_user, join_user)

        # Display updated balance to the user
        if updated_balance:
            print("Current Balance: %d" % current_acct_balance)
            bank_operations(account_num_user, user_info)

    except ValueError:
        print("Please enter a valid number.")
        deposit_operation(account_num_user, user_info)

def generate_account_number():
    return random.randrange(1111111111, 9999999999)

def get_current_balance(user_details):
    return user_details[4]

def logout(account_num):
    user_logout = database.delete_user_timestamp(account_num)

    if user_logout:
        print("Logging out of bank account!")

#### ACTUAL BANKING SYSTEM ####
init()
