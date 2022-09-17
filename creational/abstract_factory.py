class Dog:
    def speak(self):
        return 'Woof!'

    def __str__(self):
        return 'Dog'

class DogFactory:
    def get_pet(self):
        """ Returns dog object """
        return Dog()

    def get_food(self):
        """ Returns a dog food object """
        return "Dog food"


class PetStore:
    """ Petstore houses our Abstract Factory """

    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility Method to display the details of the objects returned """

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        
        print('our pet is "{}"!'.format(pet))
        print('our pet says hello by "{}"!'.format(pet.speak()))
        print('its food is "{}"'.format(pet_food))


# create dog factory
factory = DogFactory()

# create a pet store housing our abstract factory
shop = PetStore(factory)

# invoke the utility method to show the details of our pet
shop.show_pet()