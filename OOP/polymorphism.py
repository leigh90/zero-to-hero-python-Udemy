class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        # print('{} says Woof'.format(self.name))
        return self.name + "says Woooof!!"
dogone = Dog('dogone')
# dogone.speak()

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        # print('{} says Meoow'.format(self.name))
        return self.name + "says Meoow"

catone = Cat('catone')
# catone.speak()


# def pet_speak(pet):
#     print(pet.speak())

# pet_speak(dogone)
# pet_speak(catone)

# for pet in [dogone,catone]:
#     print(type(pet))
#     print(pet.speak())


class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')

class Dog(Animal):
    def speak(self):
        return self.name + 'says Woof'

class Cat(Animal):
    def speak(self):
        return self.name + 'says Woowxaa'


myanumal = Dog('Nino')
isis = Cat('isis')
print(myanumal.speak())
print(isis.speak())
    



    
    