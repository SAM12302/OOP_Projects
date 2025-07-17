import random
import string
my_dict = {
    "letters": list(string.ascii_letters),
    "numbers": [str(i) for i in range(10)],
    "punctuation": list(string.punctuation)
}

class Password:
    """Class Password: Allows the user to generate password according to the strength level
    :param strength ranges from low, mid and high
    :param length allows the user to specify the length of the password


    """

    def __init__(self, strength='mid', length=12):
        self.strength = strength
        if strength == 'low':
            self.length = 8
        elif strength == 'mid':
            self.length = 12
        elif strength == 'high':
            self.length = 16
        else:
            self.length = length

        self.length = length

    def password(self):
        current = self.strength
        if self.strength == 'low':
            count = 0
            passcode = ""
            while count < self.length:
                index = random.randrange(start=0, step=1, stop=50)
                letter = my_dict['letters'][index]
                passcode = passcode + letter
                count = count + 1

        elif self.strength == 'mid':
            combined_list = my_dict['letters'] + my_dict['numbers']
            current = self.strength
            count = 0
            passcode = ""
            while count < self.length:
                index = random.randrange(start=0, step=1, stop=len(combined_list))
                letter = combined_list[index]
                passcode = passcode + letter
                count = count + 1

        elif self.strength == 'high':
            combined_list = my_dict['letters'] + my_dict['numbers'] + my_dict['punctuation']
            current = self.strength
            count = 0
            passcode = ""
            while count < self.length:
                index = random.randrange(start=0, step=1, stop=len(combined_list))
                letter = combined_list[index]
                passcode = passcode + letter
                count = count + 1

        return passcode

    
    @staticmethod
    def show_input_exercise():
        pass


p1 = Password('low', 30)
print(p1.password())