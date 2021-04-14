#! /usr/bin/env python3

# Created by Dana Rocha 3/31/21
# Last updated 3/31/21

from datetime import datetime

database = {'Seyi': "passwordSeyi", "Mike": "passwordMike", "Dana":"passwordDana"}

def login():
    print("**** Login ****")
    print("Welcome to the Bank!")
    name = input("What is your name? \n")
    password = input("What is your password? \n")

    if (name in database and password == database[name]):
        if (password == database[name]):
            print("Welcome " + name)
            currentDateTime = datetime.now()
            formattedDateTime = currentDateTime.strftime("%m/%d/%y %H:%M:%S")
            print("Last login at %s \n" % formattedDateTime)
            
            bankOperations()
    else:
        print("Username or Password is incorrect.")
        print("Try again or Create an Account.")
        init()

def bankOperations():
    option = ""
    currentBalance = 0

    while option != "x":
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        print("Enter x to Log Out.")
        print(" ======= =============== =======")
        selectedOption = input("Please select an option \n")
        print(" ======= =============== =======")
        
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
        elif(selectedOption == "x"):
            option = "x"
            print("Logging out of ATM.")
        else:
            print("Invalid option selected, please try again.")

def init():
    print("Would you like to Login or Register?")
    userIN = int(input("(1) Login (2) Register \n"))

    if userIN == 1:
        login()
    elif userIN == 2:
        register()
    else:
        print("Invalid option selected.")
        init()

def register():
    print("**** Registration ****")
    new_first_name = input("What is your first name? \n")
    new_password = input("Create a password \n")

    database[new_first_name] = new_password

    # Login to account after account has been created
    print("Your Account has been created.")
    print(" ======= =============== =======")
    login()

init()