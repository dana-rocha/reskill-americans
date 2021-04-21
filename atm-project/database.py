# Create record
# Update record
# Read record
# Delete record
# CRUD

import os
import validation

user_db_path = "data/user_record/"

def create(account_number, first_name, last_name, email, password):
    print("Create a New Record")
    # Create a file
    # Name the file with the account_number.txt in the "data" folder
    # Add the user details to the file
    # Return True 
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)


    if does_account_number_exist(account_number):
        return False

    if does_email_exist(email):
        print("User already exists.")
        return False

    completion_state = False

    try:
        f = open(user_db_path + str(account_number) + ".txt", "x")

    except FileExistsError:
        # Delete the already created file, print out error, then return False
        does_file_contain_data = read(user_db_path + str(account_number) + ".txt")

        # Check contents of file before deleting
        # delete(account_number)
        if not does_file_contain_data:
            delete(account_number)
    
    else:
        f.write(str(user_data))
        completion_state = True
    finally:
        f.close()
    return completion_state

def read(user_account_number):
    #print("Read User Record")
    # Find user with account number
    # Fetch content of the file
    is_valid_account_number = validation.account_number_validation(user_account_number)
    
    try:

        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + str(user_account_number), "r")

    except FileNotFoundError:
        print("User Not Found.")
    except FileExistsError:
        print("User doesn't exist.")
    except TypeError: 
        print("Invalid account number format.")
    else:
        return f.readline()


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

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True 
        except FileNotFoundError:
            print("User not found.")
        finally:
            return is_delete_successful

def does_email_exist(email):
    # Loop through every file in folder
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ",")

        if email in user_list:
            return True

    return False

def does_account_number_exist(account_number):
    # Loop through every file in folder
    all_users = os.listdir(user_db_path)

    for user in all_users:
        if (user == str(account_number) + ".txt"):
            return True

    return False

def authenticate_user(account_number, password):

    if does_account_number_exist(account_number):

        user = str.split(read(account_number), ",")

        if password == user[-1]:
            return user

    return False

#create(5154511908, ["Dana", "Rocha", "rocha.da@northeastern.edu", "password", 200])
#delete(1763801065)
#print(read({"One", "Two"}))
#print(does_email_exist("rocha.da@gmail.com"))
#print(does_account_number_exist(0000000000))