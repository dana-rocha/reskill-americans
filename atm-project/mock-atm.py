#! /usr/bin/env python3

# Created by Dana Rocha 3/31/21
# Last updated 3/31/21

from datetime import datetime

name = input("What is your name? \n")
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPW = ["passwordSeyi", "passwordMike", "passwordLove"]

if (name in allowedUsers): 
    password = input("What is your password? \n")
    userID = allowedUsers.index(name)

    if (password == allowedPW[userID]):
        currentDateTime = datetime.now()
        formattedDateTime = currentDateTime.strftime("%m/%d/%y %H:%M:%S")

        print("Welcome, %s!" % name)
        print("Last login at %s \n" % formattedDateTime)

        option = ""

        currentBalance = 0

        while option != "x":
            print("These are the available options:")
            print("1. Withdrawal")
            print("2. Cash Deposit")
            print("3. Complaint")
            print("Enter x to Log Out.")

            selectedOption = input("Please select an option")

            if (selectedOption == "1"):
                withdrawInput = int(input("How much would you like to withdraw?"))
                print("Take your cash. \n")
                currentBalance -= withdrawInput
                print("Your current balance is: %s \n" % currentBalance)
            elif(selectedOption == "2"):
                depositInput = int(input("How much would you like to deposit?"))
                currentBalance += depositInput
                print("Your current balance is: %s \n" % currentBalance)
            elif(selectedOption == "3"):
                complaintInput = input("What issue would you like to report?")
                print("Thank you for contacting us. Your complaint will be reported. \n")
            elif(selectedOption == "x"):
                option = "x"
                print("Logging out of ATM.")
            else:
                print("Invalid option selected, please try again.")

    else:
        print("Password Incorrect, please try again.")
else:
    print("Name not found, please try again.")