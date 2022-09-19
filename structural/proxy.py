import time

class Producer():
    """ Define the resource intensive object to instantiate """
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now")


class Proxy:
    """ Define the 'relatively less resource-intensive' proxy to instantiate the producer object"""
    def  __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """ Check if the producer is available """
        print('Artist checking if producer is available ....')
        if self.occupied == 'No':
            # instantiate the producer class
            self.producer = Producer()
            time.sleep(3)
            # make the producer meet the quest!
            self.producer.meet()
        else:
            # otherwise do not instantiate a producer
            time.sleep(3)
            print('Producer is busy right now')

# instantiate proxy
p = Proxy()

# make the proxy : Artist peoduce until Producer is available
p.produce()


# change the state to 'occupied'
p.occupied = 'Yes'

# make the producer produce
p.produce()
        