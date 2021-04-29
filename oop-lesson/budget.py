# Create a class "Category"
# Instantiate with different categories: Food, Clothing, Car expenses, etc
# Define the methods in the class: Deposit, Withdraw, Transfer, Check Balance

# Solution must be dynamic and re-usable to support more budgets in the future

# Dana Rocha Created 4/29/21

class Category:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount


    # methods
    def deposit(self, amount):
        
        self.amount += amount
        return "You have successfully deposited {} in {} Category".format(amount, self.category)


    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)


    def check_balance(self, amount):
        # Should return a boolean
        # Check if amount is less or greater than self.amount
        if amount <= self.amount:
            return True
        else:
            return False


    def withdraw(self, amount):

        if self.check_balance(amount):
            self.amount -= amount
            return "You have successfully withdrawn {} from {} Category".format(amount, self.category)
        else:
            return "Insufficent funds for withdrawal request."

    def transfer(self, amount, category):
        # Transfer between two instantiated Categories
        # try:
        #     transfer_amount = int(input("What amount would you like to transfer?"))
        #     if transfer_amount > self.amount:
        #         print("Insufficient funds!")
        #     else:
        #         self.amount -= transfer_amount
        #         print("Transfer initiated.")
        # except TypeError:
        #     return("A valid integer must be entered.")
        pass


food_budget = Category("Food", 200)
print(food_budget.deposit(50))
print(food_budget.budget_balance())
print(food_budget.withdraw(5000))