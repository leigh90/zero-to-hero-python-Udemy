class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        # print(f'{self.name} says Woof!')
        return self.name + "says Woooof!!"

dogone = Dog('dogone')
# print(dogone.speak())

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        # print(f'{self.name} says Meoow')
        return self.name + "says Meoow"

catone = Cat('catone')
# print(catone.speak())

# for pet in [dogone,catone]:
#     print(type(pet))
#     print(pet.speak())

# interesting to note that pet_speak function doesnt necessarily know the type of object past into it. but since bot objects share a similar method name it can be called by pet_speak.
def pet_speak(pet):
    print(pet.speak())

pet_speak(catone)
pet_speak(dogone)

# IN APPLICATION

class Animal():
    def __init__(self,name):
        self.name = name

    # This is an abstract method because it is never instantiated in the base class 'Animal' The expectation is that you will create a
    # new class that will inherit from Animal and the instantiate this from there.
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):
    def speak(self):
        return self.name + 'says Woof'

class Cat(Animal):
    def speak(self):
        return self.name + 'says Woowxaa'

myanimal = Animal('Terry') #this would not work and will raise an error
mydog = Dog('Nino')
isis = Cat('Isis')
print(mydog.speak())
print(isis.speak())
    



    
    