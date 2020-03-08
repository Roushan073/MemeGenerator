

class QuoteModel(object):
    """ Class for storing Quote Information """

    def __init__(self, body, author):
        """ Create a new Quote.
            Arguments:
                body {str} -- a quote
                quote {int} -- author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'
