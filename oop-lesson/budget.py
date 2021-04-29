# Create a class "Category"
# Instantiate with different categories: Food, Clothing, Car expenses, etc
# Define the methods in the class: Deposit, Withdraw, Transfer, Check Balance

# Solution must be dynamic and re-usable to support more budgets in the future

# Dana Rocha Created 4/29/21

class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self):
        try:
            deposit_input = int(input("What amount would you like to deposit?"))
            self.amount += deposit_input
        except TypeError:
            return("You must enter a valid integer.")
    
    def check_balance(self):
        print("This is the current balance:", self.amount)

    def withdraw(self):
        try:
            withdraw_amount = int(input("How much would you like to withdraw?"))
            if withdraw_amount > self.amount:
                print("Insufficient funds.")
            else:
                self.amount -= withdraw_amount
                print("Here is your cash.")
        except TypeError:
            return("You must enter a valid integer.")

    def transfer(self):
        try:
            transfer_amount = int(input("What amount would you like to transfer?"))
            if transfer_amount > self.amount:
                print("Insufficient funds!")
            else:
                self.amount -= transfer_amount
                print("Transfer initiated.")
        except TypeError:
            return("A valid integer must be entered.")


food_budget = Budget("Food", 200)
food_budget.deposit()
food_budget.check_balance()
food_budget.withdraw()
food_budget.check_balance()
