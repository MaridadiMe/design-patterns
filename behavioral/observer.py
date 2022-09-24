""" implementing observer pattern. A nuclear has a core whose temperature is subject to change, once temperature changes, the observers must be notified of this change """


class Subject(object): # represents what is being observed
    def __init__(self):
        self._observers = [] #this is a reference to all the observers
                            # note that this is one to many relationship

    def attach(self, observer):
        # if the observer is not in the observers list
        # append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer): 
        # simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)


class Core(Subject): 
    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name
        self._temp = 0 

    @property # Getter that gets the core temperature
    def temp(self):
        return self._temp 

    @temp.setter # setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        # Notify the observers whenever somebody changes the core temperature
        self.notify()


class TempViewer:
    # the observer class
    def update(self, subject): # Alert method that is invoked when the temperature changes
        print("Temperature viewer: {} has Temperature {}".format(subject._name, subject._temp))


if __name__ == "__main__":
    # let's create our subjects
    core1 = Core("Core1")
    core2 = Core("Core2")

    # let's create our observers
    v1 = TempViewer()
    v2 = TempViewer()

    # Let's attach our observers to the first core
    core1.attach(v1)
    core1.attach(v2)

    # let's change the temperature of our first core
    core1.temp = 80
    core1.temp = 90