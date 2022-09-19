class Korean:
    """ Korean speaker """
    def __init__(self):
        self.name = 'Korean'

    def speak_Korean(self):
        return 'An-neyong?'

class British:
    """ British speaker """
    def __init__(self):
        self.name = 'British'

    def speak_English(self):
        return 'Hello?'


class Adapter:
    def __init__(self, obj, **adapted_method):
        """ Change the name of the method """
        self._object = obj

        # Add a new dictionary item that establishes mapping between generic method names and concrete method names
        self.__dict__.update(adapted_method)

    
    def __getattr__(self, attr):
        """ Simply return the rest of attributes"""
        return getattr(self._object, attr)


# list to store speaker objects
objects = []

# create KOrean object
korean = Korean()

# create English object
british = British()


# append objects to the objects list
objects.append(Adapter(korean, speak=korean.speak_Korean))
objects.append(Adapter(british, speak=british.speak_English))


for obj in objects:
    print('{} says "{}"\n'.format(obj.name, obj.speak()))
