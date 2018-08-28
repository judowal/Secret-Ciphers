# imports Cipher class from cipher module
from cipher import Cipher

# the atbash cipher is a substitution cipher that uses a reversed alphabet to encrypt messages
# a = z, b = y, c = x, and so on


# creates Atbash class that inherits from Cipher
class Atbash(Cipher):
    """ creates Atbash class """
    # initializes the class with preset values
    def __init__(self, string):
        """ accepts string and initializes class's starting values """
        # gives class access to parent class attributes and methods
        super().__init__()

        # sets self.string to string
        self.string = string

        # creates reversed alphabet that will be used to encrypt messages
        self.rev = self.alpha[::-1]

    # encrypts string using atbash cipher
    def encrypt(self):
        """ encrypts string using the Atbash cipher """
        # creates empty string to store encrypted string
        result = ""

        # for each letter in self.string
        for letter in self.string:
            # if letter is an alphabetical character
            if letter.isalpha():
                # uses letter's index in self.alpha to select the corresponding letter with the same index in self.rev
                reverse_index = self.rev[self.alpha.index(letter.lower())]

                # adds letter's atbash equivalent to result string
                result += reverse_index

            # if letter is not an alphabetical character
            else:
                # adds letter to result string
                result += letter

        # uses Cipher's encrypt_pad_string method to encrypt result string using one time pad
        # uses Cipher's split_blocks method to split one time pad encrypted string into five character blocks
        # split_blocks method also replaces spaces with space_chars and uses pad_chars to pad string to correct length
        blocks = self.split_blocks(self.encrypt_pad_string(result))

        # prints user input and encrypted string
        print('\n"{}" has been encrypted to: {}'.format(self.string, blocks))

    # decrypts string using atbash cipher
    def decrypt(self):
        """ decrypts string using Atbash cipher """
        # uses Cipher's combine_blocks method to remove spaces and pad_chars and replace space_chars with spaces
        combined_blocks = self.combine_blocks(self.string)

        # decrypts one time pad encrypted string to atbash encrypted string
        encrypted_string = self.decrypt_pad_string(combined_blocks)

        # creates empty string to store decrypted string
        result = ""

        # for each letter in encrypted_string
        for letter in encrypted_string:
            # if letter is an alphabetical character
            if letter.isalpha():
                # uses letter's index in self.rev to select the corresponding letter with the same index in self.alpha
                decrypted_letter = self.alpha[self.rev.index(letter.lower())]

                # add decrypted letter to result string
                result += decrypted_letter

            # if letter is not an alphabetical character
            else:
                # add letter to result string
                result += letter

        # prints user input and decrypted string
        print('\n{} has been decrypted to: "{}"'.format(self.string, result))
