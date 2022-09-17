class Dog:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return 'Woof!'

class Cat:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return 'Meow!'



def get_pet(pet='dog'):
    """ Factory Method """
    pets = dict(dog=Dog('Simba'), cat=Cat('Lily'))
    return pets[pet]


if __name__ == '__main__':
    d = get_pet('dog')
    print(d.speak())

    c = get_pet('cat')
    print(c.speak())