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

    accountNumberUser = input("What is your Account Number? \n")

    is_valid_account_number = account_number_validation(accountNumberUser)

    if is_valid_account_number:

        password = input("What is your password? \n")

        for accountNumber, userDetails in database.items():
            if (accountNumber == int(accountNumberUser)):
                # Check if account number is correct
                if (userDetails[3] == password):
                    # Check if password is correct

                    # If everything is correct, go to bank operations
                    bankOperation(userDetails)
                else:
                    # If something is incorrect, break out of the loop and go back to Login
                    print("Invalid Account Number or Password")
                    login()

def account_number_validation(account_number):
    # Check if account_number is not empty
    # Check if account_number if 10 digits
    # Check if account_number is an integer

    if account_number:
        if len(str(account_number)) == 10:

            try: 
                int(account_number)
                return True 
            except ValueError:
                print("Invalid Account number. The account number should only be integers.")
            except TypeError:
                print("Invalid Account type.")
                return False

        else:
            print("Account number cannot be more than 10 digits")
            return False
    else:
        print("Account Number is a required field")
        return False


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
