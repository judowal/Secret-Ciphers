# imports Cipher class from cipher module
from cipher import Cipher

# the affine cipher is a substitution cipher where each letter is mapped to its numeric equivalent
# then encrypted using a simple mathematical function, then converted back to a letter

# encrypting with the affine cipher
# E(x) = (ax + b) mod m
# with a key of: 7, 2
# E(index of letter) = (7(index of letter) + 2) mod 26

# decrypting with the affine cipher
# D(x) = c(x - b) mod m
# with a key of: 7, 2
# D(index of letter) = 15(index of letter - 2) mod 26


# creates Affine class that inherits from Cipher
class Affine(Cipher):
    """ creates Affine class """
    # initializes the class with preset values
    def __init__(self, string):
        """ accepts a string and initializes class with preset values"""
        # gives class access to parent class attributes and methods
        super().__init__()

        # sets self.string to string
        self.string = string

        # make a dictionary mapping alphas to nums
        self.alpha_dict = {number: letter for letter, number in zip(self.alpha, range(0, 26))}

        # key for encoding and decoding messages
        self.key = [7, 2]

    # encrypts string using the affine cipher
    def encrypt(self):
        """ encrypts string using the Affine cipher """
        # creates empty list to store encrypted string
        result = ""

        # for each letter in string
        for letter in self.string:
            # if the letter is an alphabetical character
            if letter.isalpha():
                # stores index of letter in self.alpha
                index = self.alpha.index(letter.lower())

                # uses index of letter in alpha to calculate index of letter in affine cipher
                affine_index = (self.key[0] * index + self.key[1]) % len(self.alpha)

                # adds encrypted letter to results string
                result += self.alpha_dict[affine_index]

            # if letter is not an alphabetical character
            else:
                # add letter to result string
                result += letter

        # uses Cipher's encrypt_pad_string method to encrypt result string using one time pad
        # uses Cipher's split_blocks method to split one time pad encrypted string into five character blocks,
        # split_blocks method also replaces spaces with space_chars and uses pad_chars to pad string to correct length
        blocks = self.split_blocks(self.encrypt_pad_string(result))

        # prints user input and encrypted string
        print('\n"{}" has been encrypted to {}'.format(self.string, blocks))

    def decrypt(self):
        """ decrypts string using the Affine cipher """
        # uses Cipher's combine_blocks method to remove spaces and pad_chars, and replaces space_chars with spaces
        combined_blocks = self.combine_blocks(self.string)

        # decrypts one time pad encrypted string to keyword encrypted string
        encrypted_string = self.decrypt_pad_string(combined_blocks)

        # creates empty string to store decrypted string
        result = ""

        # for each letter in encrypted_string
        for letter in encrypted_string:
            # if letter is an alphabetical character
            if letter.isalpha():

                # store index of letter in self.alpha
                index = self.alpha.index(letter.lower())

                # uses index of letter in self.alpha to calculate the index of the decrypted letter
                letter_index = 15 * (index - self.key[1]) % len(self.alpha)

                # adds decrypted letter to result string
                result += self.alpha_dict[letter_index].lower()

            # if letter is not an alphabetical character
            else:
                # adds letter to result string
                result += letter

        # prints user input and encrypted string
        print('\n{} has been decrypted to "{}"'.format(self.string, result))


