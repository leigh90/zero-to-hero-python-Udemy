class Animal():
    def __init__(self):
        print('Animal Created')

    def eat(self):
        print('I am eating')

    def who_am_i(self):
        print('I am an animal')
animalone = Animal()
animalone.eat()


# to inherit the animal base class you pass in the name of the class inside the brackets
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    
    #you can ovewrite the base class methods by creating new methods with the same name as the base class otherwise the class will inherit the base class methods as they are 
    def eat(self):
        print('Dog here eating')
    
    # you can also add new methods
    def bark():
        print('Woof')


dogone = Dog() #this creating a new instance of the dog class
dogone.eat() #this is the ovewritten method
dogone.who_am_i() #this is a method inherited from the animal class

