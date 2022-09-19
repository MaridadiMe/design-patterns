class Component:
    """ Abstract Class """
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Child(Component):
    """ Concrete class """
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        # this is where you store the name of the child item
        self.name = args[0]

    def component_function(self):
        # print name of your child item here
        print('{}'.format(self.name))

class Composite(Component):
    """ concrete class that maintains the tree recursive structure  """

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, *kwargs)

        # this is where we store name of the composite object
        self.name = args[0]

        # this is where we keep child items
        self.children = []

    def append_child(self, child):
        """ Method to add a new child item """
        self.children. append(child)

    def remove_child(self, child):
        """ Method to remove a child """
        self.children.remove(child)

    def component_function(self):
        """" Print name of the composite object """
        print('{}'.format(self.name))

        # iterate through the child objects and invoke their component_function
        for child in self.children:
            child.component_function()



# build a composite submenu 1
sub1 = Composite("submenu1")

# create a new schild sub menu 11
sub11 = Child('submenu11')

# create a new schild sub menu 12
sub12 = Child('submenu12')

# add sub menu 11 to submenu 1
sub1.append_child(sub11)

# add sub menu 12 to submenu 1
sub1.append_child(sub12)

# build a top level composite menu
top = Composite('top')

# build a submenu 2 that is not composite
sub2 = Child("submenu2")

# add composite submenu 2 to the top level composite menu
top.append_child(sub1)

# add the plain sub menu 2 to the top level composite menu
top.append_child(sub2)


# lets see if the composite pattern works
top.component_function()




    