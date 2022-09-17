
class Borg:
    """ The Borg design pattern"""
    _shared_data = {}

    def __init__(self):
        self.__dict__ = self._shared_data


class Singleton(Borg):
    """ The Singleton class """
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


# create first singleton object
x = Singleton(HTTP= 'Hyper Text Transfer Protocol')
print(x)
y= Singleton(SMTP = 'Simple Mail Transfer Protocol')
print(y)