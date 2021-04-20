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
                print("Invalid Account number. The account number should only be integers. \n")
            except TypeError:
                print("Invalid Account type. \n")
                return False

        else:
            print("Account number cannot be more than or less than 10 digits. \n")
            return False
    else:
        print("Account Number is a required field. \n")
        return False

def validation_registration_input(input):
    # Check if input is a list
    # Check each item in the list and make sure they are the correct data types
    pass