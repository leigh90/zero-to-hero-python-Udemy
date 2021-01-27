# creating a class
class Sample():
    pass
# creating an instance
mysample = Sample()
# check type of instance
print(type(mysample))


class Dog():
    # understaning class attributes and how they are declared
    def __init__(self, mybreed):
        self.my_attribute = mybreed

dog1 = Dog(mybreed='Huskie')
print(dog1.my_attribute)
print(type(dog1))

class Dog():
    # class object attributes 
    species = 'Mammal'

    # init method initializes creation of individual instances
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    # class methods
    def bark(self):
        print('wOOF')

    def bark2(self,number):
        print('WOOF name is {} and the number is {}'.format(self.name, number))

# creating and instance of a class
mydog = Dog(breed= 'Lab', name='Terry', spots=False)
# check the attributes of an object
print(mydog.name, mydog.breed, mydog.spots, mydog.species)
# call a class method
mydog.bark2(11)

class Circle():

    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    def get_circumference(self):
        return self.radius * Circle.pi * 2

mycircle = Circle(9)
print(mycircle.get_circumference())



