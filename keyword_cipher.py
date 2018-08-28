# imports Cipher class from cipher module
from cipher import Cipher


# the keyword cipher is a substitution cipher that uses a keyword as the key
# the last letters may not be encrypted
# keyword for this cipher: "mygodjustinwaler"

# creates Keyword class that inherits from Cipher
class Keyword(Cipher):
    """ creates Keyword class """
    # initializes the class with preset values
    def __init__(self, string):
        """ accepts a string and initializes class with preset values """
        # gives class access to parent class attributes and methods
        super().__init__()

        # sets self.string to string
        self.string = string

        # the keyword cipher that will be used to encrypt messages
        self.altered = ""

    # sets the keyword that the cipher will use to encrypt the string
    def set_keyword(self):
        """ prompts the user to enter a keyword to construct our keyword cipher and stores the input """
        # while self.altered does not have a value set
        while self.altered == "":
            # inform user that they need to enter a keyword to be used with the keyword cipher
            print("\nA keyword will be used as a key for the cipher.\n")

            # also inform user that keyword must contain only letters and may not repeat any letters
            print("Key must only contain alphabetical characters and must not contain any repeating characters.\n")

            # prompt the user to enter the keyword
            keyword_key = input("Enter the keyword:  ").lower()

            # a set contains only one copy of each item
            # we convert the string into a set to get one copy of each letter in the string

            # if all characters in keyword_key are letters
            # and if the length of keyword_key when converted to a set is equal to the length of the keyword_key string
            if all(x.isalpha() for x in keyword_key) and len(set(keyword_key)) == len(keyword_key):
                # informs the user of their chosen keyword
                print("\nKeyword has been set to: {}\n".format(keyword_key))

                # turn make copy of self.alpha and convert it into a list
                altered_alpha = list(self.alpha)

                # for each letter in keyword_key
                for letter in keyword_key:
                    # remove the letter from altered_alpha
                    altered_alpha.remove(letter)

                # join each item in altered_alpha to convert the list to a string
                # concatenate keyword_key and altered_alpha string
                # set result to self.altered
                self.altered = keyword_key + "".join(altered_alpha)

            # if user enters an empty string
            elif keyword_key == "":
                # run the function again
                self.set_keyword()

            # if all characters in keyword_key are letters or any letters in keyword_key are repeated
            else:
                print("\nPlease enter a string without repeating characters.\n")

        # informs the user of the alphabet that will be used to encrypt the string
        print("Message will be encrypted using: {}".format(self.altered))

    # encrypts string using the keyword cipher
    def encrypt(self):
        """ encrypts string using the Keyword cipher """
        # sets keyword used to encrypt string
        self.set_keyword()

        # creates empty string to store encrypted string
        result = ""

        # for each letter in self.string
        for letter in self.string:
            # if letter is an alphabetical character
            if letter.isalpha():
                # uses letter's index in self.alpha to select the corresponding letter with the same index in
                # self.altered
                encrypted_letter = self.altered[self.alpha.index(letter.lower())]

                # adds encrypted letter to result string
                result += encrypted_letter

            # if the letter is not an alphabetical character
            else:
                # adds letter to result string
                result += letter

        # uses Cipher's encrypt_pad_string method to encrypt result string using one time pad
        # uses Cipher's split_blocks method to split one time pad encrypted string into five character blocks,
        # split_blocks method also replaces spaces with space_chars and uses pad_chars to pad string to correct length
        blocks = self.split_blocks(self.encrypt_pad_string(result))

        # prints user input and encrypted string
        print('\n"{}" has been encrypted to: {}'.format(self.string, blocks))

    # decrypts string using the keyword cipher
    def decrypt(self):
        """ decrypts string using Keyword cipher """
        # sets keyword used to decrypt string
        self.set_keyword()

        # uses Cipher's combine_blocks method to remove spaces and pad_chars and replace space_chars with spaces
        combined_blocks = self.combine_blocks(self.string)

        # decrypts one time pad encrypted string to keyword encrypted string
        encrypted_string = self.decrypt_pad_string(combined_blocks)

        # creates empty string to store decrypted string
        result = ""

        # for each letter in encrypted_string
        for letter in encrypted_string:

            # if the letter is an alphabetical character
            if letter.isalpha():
                # uses letter's index in self.altered to select the corresponding letter with the same index in
                # self.alpha
                decrypted_letter = self.alpha[self.altered.index(letter.lower())]

                # adds decrypted letter to result string
                result += decrypted_letter

            # if the letter is not an alphabetical character
            else:
                # adds letter to result string
                result += letter

        # prints user input and encrypted string
        print('\n{} has been decrypted to "{}"'.format(self.string, result))
