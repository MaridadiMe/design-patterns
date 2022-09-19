from functools import wraps


def make_blink(function):
    """ Defines the Decorator """

    # This makes the decorator transparent in terms of its name and docs
    @wraps(function)

    # Define inner function
    def decorator():
        # grab the return value of the function being decorated
        ret = function()


        # add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

# apply decorator here

@make_blink
def hello_world():
    """ Original function """
    return "Hello World!"


# check the result of decorating
print(hello_world())

# check if the function name is still the same name of the function being decorated
print(hello_world.__name__)


# check if the docstring is still the same as the function being decorated
print(hello_world.__doc__)