class InvalidArgumentException(Exception):
    """Exception raised for errors that are Caused if a invalid Argument was given.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
