# Create record
# Update record
# Read record
# Delete record
# CRUD

import os
import validation

user_db_path = "data/user_record/"

def create(user_account_number, first_name, last_name, email, password):
    print("Create a New Record")
    # Create a file
    # Name the file with the account_number.txt in the "data" folder
    # Add the user details to the file
    # Return True 
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)


    if does_account_number_exist(user_account_number):
        # Return False if account number exists already 
        return False

    if does_email_exist(email):
        # If email is already being used, return Ralse 
        print("User already exists.")
        return False

    # If code reaches to this point, the account number and email are not being used yet
    completion_state = False
    
    try:
        # Create a new text file with the account number
        f = open(user_db_path + str(User_account_number) + ".txt", "x")

    except FileExistsError:
        # If this filename already exists, delete the already created file, print out an error, then return False
        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")

        # Check contents of file before deleting
        if not does_file_contain_data:
            # If the file doesn't contain anything, delete the file
            delete(user_account_number)
    
    else:
        # If filename doesn't exist yet, create the file and write the user data to the file
        f.write(str(user_data))
        completion_state = True
    finally:
        f.close()
        return completion_state

def read(user_account_number):
    # Find user with account number
    # Fetch content of the file

    # Validating the user's account number
    is_valid_account_number = validation.account_number_validation(user_account_number)
    
    try:

        if is_valid_account_number:
            # If the account number is validated, read the text file
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            # If the account number isn't validated, read the file
            f = open(user_db_path + str(user_account_number), "r")

    except FileNotFoundError:
        print("User Not Found.")
    except FileExistsError:
        print("User doesn't exist.")
    except TypeError: 
        print("Invalid account number format.")
    else:
        return f.readline()
    
    return False


def update(user_account_number):
    print("Update User Record")
    # Find the user with account number
    # Fetch the contents of the file
    # Update the contents of the file
    # Save the file
    # Return True

def delete(user_account_number):
    print("Delete User Record")
    # Find the user with account number
    # Delete the user record (file)
    # Return True
    is_delete_successful = False

    # Check if the path exists
    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        
        try:
            # If the file path exists, remove the file
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True 
        except FileNotFoundError:
            print("User not found.")
        finally:
            return is_delete_successful

def does_email_exist(email):
    # Loop through every file in folder
    # One file = one user
    all_users = os.listdir(user_db_path)

    # Loop through all users
    for user in all_users:
        # Create list of users
        user_list = str.split(read(user), ",")

        # If the email is in the user list, then the email is already being used, return True
        if email in user_list:
            return True
    # If email is not being used, return False 
    return False

def does_account_number_exist(account_number):
    # Loop through every file in folder
    all_users = os.listdir(user_db_path)

    # If user's account number already exists, return True
    for user in all_users:
        if (user == str(account_number) + ".txt"):
            return True
    # If user's account number does not exist, return False
    return False

def authenticate_user(account_number, password):

    if does_account_number_exist(account_number):
        # If account number exists, create list of account numbers
        user = str.split(read(account_number), ",")

        if password == user[3]:
            # If password is in user's file, return the user's account number
            return user

    return False

#create(5154511908, ["Dana", "Rocha", "rocha.da@northeastern.edu", "password", 200])
#delete(1763801065)
#print(read({"One", "Two"}))
#print(does_email_exist("rocha.da@gmail.com"))
#print(does_account_number_exist(0000000000))