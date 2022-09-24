import types
class Strategy:
    def __init__(self, function=None):
        self.name = "Default Strategy"

        # if a reference to a function is provided, replace the executed method
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self): # this gets replaced by another version if another function is provided
        """ The default method that prints the name of the strategy being used """
        print("{} is used!".format(self.name))
        

# REPLACEMENT METHOD 1
def strategy_one(self):
        print("{} is used to execute method 1".format(self.name))

# REPLACEMENT METHOD 2
def strategy_two(self):
        print("{} is used to execute method 2".format(self.name))

if __name__ == "__main__":
    # create our default strategy
    s0 = Strategy()

    # Execute default strategy
    s0.execute()


    # create first variation of our default strategy 
    s1 = Strategy(strategy_one)
    s1.name = "Strategy One"
    # execute it
    s1.execute()

    # create first variation of our default strategy 
    s2 = Strategy(strategy_two)
    s2.name = "Strategy Two"
    # execute it
    s2.execute()