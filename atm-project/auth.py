# Register
# - Username, password, email
# - Generate user account

# Login
# - Username, Password, email

# Bank Operations 

# Initializing the system
def init():
    print("Welcome to Bank of Python")
    haveAccount = int(input("Do you have an account with us: 1 = Yes, 2 = No"))

    if (haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected an invalid option.")

def login():
    print("This is the login function")

def register():
    print("This is the register function")

def bankOperation():
    print("some operations")

def generateAccountNumber():
    print("account number generator")
