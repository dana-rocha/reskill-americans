#! /usr/bin/env python3

# Created by Dana Rocha 3/31/21
# Last updated 3/31/21

name = input("What is your name? \n")
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPW = ["passwordSeyi", "passwordMike", "passwordLove"]

if (name in allowedUsers): 
    password = input("What is your password? \n")
    userID = allowedUsers.index(name)

    if (password == allowedPW[userID]):
        print("Welcome, %s!" % name)
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")

        selectedOption = int(input("Please select an option"))

        if (selectedOption == 1):
            print("You selected %s" % selectedOption)
        elif(selectedOption == 2):
            print("You selected %s" % selectedOption)
        elif(selectedOption == 3):
            print("You selected %s" % selectedOption)
        else:
            print("Invalid option selected, please try again.")

    else:
        print("Password Incorrect, please try again.")
else:
    print("Name not found, please try again.")