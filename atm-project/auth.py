# Register
# - Username, password, email
# - Generate user account

# Login
# - Account Number, Password

# Bank Operations 
# Initializing the system
import random
import validation

database = {
    5154511908: ["Dana", "Rocha", "rocha.da@northeastern.edu", "password", 200]
}

def init():

    isValidOption = False
    print("Welcome to Bank of Python! \n")

    haveAccount = int(input("Do you have an account with us: 1 = Yes, 2 = No \n"))
    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected an invalid option.")
        init()

def login():
    print("**** Login ****")

    accountNumberUser = input("What is your Account Number? \n")

    is_valid_account_number = validation.account_number_validation(accountNumberUser)

    if is_valid_account_number:

        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if (accountNumber == int(accountNumberUser)):
                # Check if account number is correct
                if (userDetails[3] == password):
                    # Check if password is correct
                    # If everything is correct, go to bank operations
                    bankOperation(accountNumber, userDetails)
                else:
                    # If something is incorrect, break out of the loop and go back to Login
                    print("Invalid Account Number or Password")
                    login()
    else:
        init()

def register():
    print("**** Registration ****")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password. \n")

    try:
        accountNumber = generateAccountNumber()
    except ValueError:
        print("Account generation failed.")
        init()

    database[accountNumber] = [first_name, last_name, email, password]

    # Login to account after account has been created
    print("Your Account has been created.")
    print(" ======= =============== =======")
    print("Your Account Number is %d" % accountNumber)
    print("Make sure you keep it safe.")
    print(" ======= =============== =======")

    login()

def bankOperation(accNum, user):
    print("Welcome %s %s" % (user[0], user[1]))

    try:
        selectedOption = int(input("What would you like to do? \n(1) Deposit (2) Withdrawl (3) Logout (4) Exit \n"))
    
        if (selectedOption == 1):
            depositOperation()
        elif(selectedOption == 2):
            withdrawalOperation(accNum, user)
        elif(selectedOption == 3):
            logout()
        elif(selectedOption == 4):
            exit()
        else:
            print("Invalid option selected.")
            bankOperation(accNum, user)
    
    except ValueError:
        print("You must enter a valid option. ")
        bankOperation(accNum, user)

def withdrawalOperation(acctNumber, user_details):
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

            # Need to actually update the database dictionary with the new account balance

            print("Current Balance: %d" % user_details[4])
        else:
            print("Insufficient funds for withdrawal transaction.")
            bankOperation(acctNumber, user_details)

    except ValueError:
        print("You must enter a valid number.")
        withdrawalOperation(user_details)

def depositOperation():
    print("**** Deposit ****")

    # Get current balance
    # Get deposit amount
    # Add deposit amount to current balance
    # Display current balance

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def get_current_balance(user_details):
    return user_details[4]

def logout():
    login()

#### ACTUAL BANKING SYSTEM ####
init()
