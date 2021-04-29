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
        return "You have successfully deposited {} in {} Category.".format(amount, self.category)


    def budget_balance(self):
        return "This is the current balance: {}".format(self.amount)


    def check_balance(self, amount):
        # Should return a boolean
        # Check if amount is less than or greater than self.amount
        if amount >= self.amount:
            return True
        else:
            return False


    def withdraw(self, amount):

        if self.check_balance(amount):
            return "Insufficent funds for withdrawal request."
        else:
            self.amount -= amount
            return "You have successfully withdrawn {} from {} Category.".format(amount, self.category)


    def transfer(self, amount, category):
        # Transfer between two instantiated Categories
        if self.check_balance(amount) != True:
            self.amount -= amount
            category.amount += amount
            return "Transfer successful from {} Category to {} Category".format(self.category, category)
        else:
            return "Insufficient funds. Transfer cannot be initiated."


food_budget = Category("Food", 200)
#print(food_budget.deposit(50))
#print(food_budget.budget_balance())
#print(food_budget.withdraw(5000))

car_budget = Category("Car", 5000)
#print(car_budget.withdraw(30))
# #print(car_budget.withdraw(1000))

entertainment_budget = Category("Entertainment", 400)
clothing_budget = Category("Clothing", 200)

print(clothing_budget.transfer(20, entertainment_budget))
