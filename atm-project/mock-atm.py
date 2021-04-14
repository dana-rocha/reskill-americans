#! /usr/bin/env python3

# Created by Dana Rocha 3/31/21
# Last updated 3/31/21

from datetime import datetime
import random

database = {0000000000:["Dana", "passwordDana"]}

def init():
    print("Would you like to Login or Register?")
    userIN = int(input("(1) Login (2) Register \n"))

    if userIN == 1:
        login()
    elif userIN == 2:
        register()
    else:
        # If no valid options selected, show options again
        print("Invalid option selected.")
        init()

def login():
    print("**** Login ****")
    print("Welcome to the Bank!")

    accountNumberUser = int(input("What is your Account Number? \n"))
    password = input("What is your password? \n")

    # Check user info in the database
    for accountNum, userDetails in database.items():
        if (accountNum == accountNumberUser):
            if (userDetails[1] == password):
                print(" =============================")
                print("Welcome " + userDetails[0])
                currentDateTime = datetime.now()
                formattedDateTime = currentDateTime.strftime("%m/%d/%y %H:%M:%S")
                print("Last login at %s \n" % formattedDateTime)
                
                bankOperations(userDetails)
            else:
                print("Login Failed. Username or Password is incorrect.")
                print("Try again or Create an Account.")
                init()

def bankOperations(user):
    option = ""
    currentBalance = 0

    while option != "x":
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        print("4. Update Your Password")
        print("Enter x to Log Out.")
        print(" =============================")
        selectedOption = input("Please select an option \n")
        print(" =============================")
        
        if (selectedOption == "1"):
            withdrawInput = int(input("How much would you like to withdraw? \n"))
            print("Take your cash. \n")
            currentBalance -= withdrawInput
            print("Your current balance is: %s \n" % currentBalance)
        elif(selectedOption == "2"):
            depositInput = int(input("How much would you like to deposit? \n"))
            currentBalance += depositInput
            print("Your current balance is: %s \n" % currentBalance)
        elif(selectedOption == "3"):
            complaintInput = input("What issue would you like to report? \n")
            print("Thank you for contacting us. Your complaint will be reported. \n")
        elif(selectedOption == "4"):
            updatePassword()
        elif(selectedOption == "x"):
            option = "x"
            print("Logging out of ATM.")
        else:
            print("Invalid option selected, please try again.")

def register():
    # Create new user
    print("**** Registration ****")
    new_first_name = input("What is your first name? \n")
    new_password = input("Create a password \n")

    accountNumber = generateAccountNumber()

    # Add new user to the database
    database[accountNumber] = [new_first_name, new_password]

    # Login to account after account has been created
    print(" =============================")
    print("Your Account has been created.")
    print(" =============================")
    print("Your Account Number is %d" % accountNumber)
    print("Make sure you keep it safe.")
    print(" =============================")
    login()

def generateAccountNumber():
    # Generate a random 10-digit number for the Bank Account
    return random.randrange(1111111111, 9999999999)

def updatePassword():
    # Update a user's password
    print("**** Update Your Password ****")
    accountIN = int(input("What is your Account Number? \n"))
    usernameIN = input("What is your name? \n")
    passwordOLD = input("What is your old password? \n")
    passwordNEW = input("What is your new password? \n")

    # Double check user info before updating user's password
    for acctNum, userInfo in database.items():
        if (acctNum == accountIN and userInfo[0] == usernameIN):
            if (userInfo[1] == passwordOLD):
                print(" =============================")
                # Update the second element in the dictionary key
                userInfo[1] = passwordNEW
                database[acctNum] = [usernameIN, userInfo[1]]
                # Confirm new password to user
                print("Hi, %s! Your new password is: %s" % (usernameIN, passwordNEW))

init()