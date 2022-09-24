class House(object): # the class being visited
    def accept(self, visitor):
        """ Interface to accept a visitor """
        # triggers the visiting operation
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "Worked on by", hvac_specialist)

    def work_on_electricity(self, electrician):
        print(self, "Worked on by", electrician)

    def __str__(self):
        """ Simply return the class name when the house object is printed """
        return self.__class__.__name__




class Visitor(object):
    """ Abstract Visitor """
    def __str__(self):
        """ Simply return the class name when the visitor object is printed """
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    """ concrete visitor : hvac specialist """
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    """ concrete visitor : electrician """
    def visit(self, house):
        house.work_on_electricity(self)


if __name__ == "__main__":
    # create visitors
    h = HvacSpecialist()
    e = Electrician()


    # create house
    home = House()

    # let electrician and hvac specialist visit home
    home.accept(h)
    home.accept(e)