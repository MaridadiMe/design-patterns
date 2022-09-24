class Handler: # Abstract Handler
    def __init__(self, successor):
        # define the next handler
        self._successor = successor

    def handle(self, request):
        handled = self._handle(request) # if handled stop here

        # otherwise pass the request to the next handler
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')



class ConcreteHandler1(Handler):
    # concrete handler 1
    def _handle(self, request):
        if 0 < request <= 10: # provide condition for handling
            print("Request {} handled in handler 1".format(request))
            return True # indicate that the request has been handled


class DefaultHandler(Handler):
    """ Default Handler """
    def _handle(self, request):
        """ If there is no handler available """
        # no condition checking since this is a default handler
        print("End of Chain no handler for {}".format(request))
        return True # indicate that the request has been handled


class Client: #using handlers
    def __init__(self):
        # create handlers and use them in sequence that you want
        self.handler = ConcreteHandler1(DefaultHandler(None))

    def delegate(self, requests): # send requests one at a time
        for request in requests:
            self.handler.handle(request)

if __name__ == "__main__":
    # create client
    client = Client()
    
    # Create requests
    requests = [2,5,12,4,8,10]

    # send requests to the client
    client.delegate(requests)
