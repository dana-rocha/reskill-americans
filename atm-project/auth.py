# Register
# - Username, password, email
# - Generate user account

# Login
# - Account Number, Password

# Bank Operations 
# Initializing the system
import random

database = {}

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

    accountNumberUser = int(input("What is your Account Number? \n"))
    password = input("What is your password? \n")

    for accountNumber, userDetails in database.items():
        if (accountNumber == accountNumberUser):
            # Check if account number is correct
            if (userDetails[3] == password):
                # Check if password is correct

                # If everything is correct, go to bank operations
                bankOperation(userDetails)
            else:
                # If something is incorrect, break out of the loop and go back to Login
                print("Invalid Account Number or Password")
                login()

def register():
    print("**** Registration ****")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    # Login to account after account has been created
    print("Your Account has been created.")
    print(" ======= =============== =======")
    print("Your Account Number is %d" % accountNumber)
    print("Make sure you keep it safe.")
    print(" ======= =============== =======")

    login()

def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))

    selectedOption = int(input("What would you like to do? \n(1) Deposit (2) Withdrawl (3) Logout (4) Exit \n"))

    if (selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):
        exit()
    else:
        print("Invalid option selected.")
        bankOperation(user)

def withdrawalOperation():
    print("withdrawal")

def depositOperation():
    print("deposit")

def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)

def logout():
    login()

#### ACTUAL BANKING SYSTEM ####
init()
