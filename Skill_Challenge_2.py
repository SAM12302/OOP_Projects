import random

class Password:
    """Class Password: Allows the user to generate password according to the strength level
    :param strength ranges from low, mid and high
    :param length allows the user to specify the length of the password

    
    """
    def __init__(self, strength, length):
        self.strength = strength
        self.length = length