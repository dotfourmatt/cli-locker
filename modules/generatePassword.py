from random import SystemRandom
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

# Password Generator Class => I am aware that it is very simple, suggestions to make it more complex would be appreciated
# Or even if it does not need to be more complex, just tips that can make this code more efficient would be nice
class passwordGenerator():
    """ 
    This class allows you to input the length of the desired password and the "options" to be added.\n
    Length is just a simple integer value. The minmum length is 8, and the maximum is 50 characters long.\n
    When selecting "options" a list of booleans must be entered e.g. [True, True, False, False] for lower & upper case letters, but not digits and punc.\n
    Options:\n
    ==> Lowercase Letters:  abcdefghijklmnopqrstuvwxyz\n
    ==> Uppercase Letters:  ABCDEFGHIJKLMNOPQRSTUVWXYZ\n
    ==> Digits: 0123456789\n
    ==> Punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n
    """

    def __init__(self, length = int, options = list): 
        # Is it possible to set the expected variable types?
        # So that length must be an integer, options must be a list and save must be a boolean, without __exceptionHandler()?
        self.length = length # Integer
        self.options = options # List
        self.__exceptionHandler() # Checks if inputs are correct

    def __str__(self):
        return self.__generate()

    def __generate(self):
        opts = self.__determineOptions()
        password = ''.join(SystemRandom().choice(opts) for i in range(self.length))
        return password
    
    def __determineOptions(self):
        optionsSelected = ''

        # Input list should be input as [Lower, Upper, Digits, Punctuation]. Each value will be a boolean
        if self.options[0]:
            optionsSelected += ascii_lowercase
        if self.options[1]:
            optionsSelected += ascii_uppercase
        if self.options[2]:
            optionsSelected += digits
        if self.options[3]:
            optionsSelected += punctuation
            
        return optionsSelected

    # Checks if inputted variables are the correct types
    def __exceptionHandler(self):
        if isinstance(self.length, int) == False:
            raise TypeError(f"Please input an integer, not a {type(self.length)}")
        else:
            if self.length < 8:
                self.length = 8

            elif self.length > 50:
                self.length = 50

        if isinstance(self.options, list):
            if len(self.options) != 4:
                if len(self.options) > 4:
                    raise IndexError(f"List is too long, it must contain 4 boolean values, not {len(self.options)}!")
                else:
                    raise IndexError(f"List is too short, it must contain 4 boolean values, not {len(self.options)}!")

            for item in self.options:
                if isinstance(item, bool) == False:
                    raise ValueError("Incorrect value input, must be either 'True' or 'False' ie a boolean.")
            
            if self.options.count(True) == 0:
                raise Exception("Please enter at least 1 option")

        else:
            raise TypeError(f"Please input a list, not a {type(self.options)}")