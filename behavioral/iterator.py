def count_to(count):
    """ custom iterator implementation """

    # our list
    numbers_in_iraqw = ["wak", "tsar", "tam" , "tsiyah", "koan", "lahho"]

    # our iterator
    # creates tuples such as (1, "wak")

    iterator = zip(range(count), numbers_in_iraqw)
    print(iterator)

    #  iterate through our iterable list
    #  exract the iraqw numbers
    #  put them in a generato called numbers

    for position, number in iterator:
        #  returns generator containing numbers in iraqw
        yield number


if __name__ == "__main__":
    for num in count_to(3):
        print(num)