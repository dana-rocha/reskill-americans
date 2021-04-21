# Create record
# Update record
# Read record
# Delete record
# CRUD

def create(account_number, user_details):
    print("Create a New Record")
    # Create a file
    # Name the file with the account_number.txt in the "data" folder
    # Add the user details to the file
    # Return True 
    completion_state = False

    try:
        f = open("data/user_record/" + str(account_number) + ".txt", "x")
    except FileExistsError:
        # Delete the already created file, print out error, then return False
        print("User already exists.")
    else:
        f.write(str(user_details))
        completion_state = True
    finally:
        f.close()
    return completion_state

def read(user_account_number):
    print("Read User Record")
    # Find user with account number
    # Fetch content of the file


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

def find(user_account_number):
    print("Find User")
    # Find the user with account number

#create(5154511908, ["Dana", "Rocha", "rocha.da@northeastern.edu", "password", 200])