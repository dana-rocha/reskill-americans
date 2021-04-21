def account_number_validation(account_number):
    # Check if account_number is not empty
    # Check if account_number if 10 digits
    # Check if account_number is an integer

    if account_number:

        try: 
            int(account_number)
            if len(str(account_number)) == 10:
                return True
        
        except ValueError:
            # print("Invalid Account number. The account number should only be integers. \n")
            return False
        
        except TypeError:
            # print("Invalid Account type. \n")
            return False
    
    return False

def validation_registration_input(input):
    # Check if input is a list
    # Check each item in the list and make sure they are the correct data types
    pass