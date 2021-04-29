class Budget:

    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self):
        return("This is a deposit method.")

    def check_balance(self):
        pass

    def withdraw(self):
        pass

    def transfer(self):
        pass

category = Budget("Clothing", 1000)
category2 = Budget("Food", 1000)
category2 = Budget("Entertainment", 1000)

#print(category.deposit())

# Can also modify given properties
class Car:

    def __init__(self, name, color):
        self.model = name
        self.color = color
    
    def my_car(self):
        print("My car's model is", self.model)

myCar1 = Car("BMW", "White")
# We can override the previous line by setting the model property to a different brand
myCar1.model = "Toyota"
#myCar1.my_car()

class MyClass:
    def __init__(self, height):
        self.height = 20

myHeight = MyClass(100)
del myHeight.height
print(myHeight.height)