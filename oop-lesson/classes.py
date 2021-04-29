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
# Can delete attributes
del myHeight.height
#print(myHeight.height)


# Derived class inherits features from the base class where new features can be added to it
# Results in the reusuability of code
class Person:

    def __init__(self):
        self.firstname = "Joshua"

    def printname(self):
        print(self.firstname)

# User the Person class to create an object and execute the printname method:
#X = Person("John", "Doe")
#X.printname()


# Consider the second class below which is the child class
class Student(Person):
    
    # Can add the init function like in the Parent class
    # When you add the init function to the child class, it will no longer
    # inherit the parent's init funcion
    def __init__(self, fname):
        self.firstname = fname

student1 = Student("Daniel")
student1.printname()