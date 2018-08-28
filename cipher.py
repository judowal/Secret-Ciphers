# imports random module
import random


class Cipher:
    """ creates cipher class that all other classes will be inherit from """
    # initializes the class with preset values
    def __init__(self):
        """ intializes class's starting values """
        # alphabet that all cipher conversions will be based upon
        self.alpha = "abcdefghijklmnopqrstuvwxyz"

        # one time pad that will be used to add a second layer of encryption
        self.pad = "hkmjustindqvxbcfgyzwalerop"

        # list of characters that will be used to pad strings to the correct length
        self.pad_chars = ["#", "%", "&"]

        # list of characters that will be used to replace spaces in strings
        self.space_chars = ["<", "$", "@", "!", "*", "+", "=", "-", ">"]

    # encrypts string with one time pad
    def encrypt_pad_string(self, string):
        """ accepts a string and encrypts it using the one time pad """
        # create empty string to hold pad encrypted string
        result = ""

        # for each letter in the string
        for letter in string:
            # if letter is an alphabetical character
            if letter.isalpha():
                # uses letter's index in self.alpha to select the corresponding letter with the same index in self.pad
                pad_letter = self.pad[self.alpha.index(letter.lower())]

                # adds pad_letter to result string
                result += pad_letter

            # if letter is not an alphabetical character
            else:
                # adds letter to result string
                result += letter

        # return the one time pad encrypted string
        return result

    # decrypts string with one time pad
    def decrypt_pad_string(self, string):
        """ accepts a string and decrypts it using the one time pad """
        # creates empty string to store pad decrypted string
        result = ""

        # for each letter in the string
        for letter in string:
            # if the letter is an alphabetical character
            if letter.isalpha():
                # uses letter's index in self.pad to select the corresponding letter with the same index in self.alpha
                no_pad_letter = self.alpha[self.pad.index(letter.lower())]

                # adds no_pad_letter to result string
                result += no_pad_letter

            # if the letter is not an alphabetical character
            else:
                # adds letter to result string
                result += letter

        # returns one time pad decrypted string
        return result

    # splits string into five character blocks
    def split_blocks(self, string):
        """ accepts an encrypted string, splits it into 5 character blocks, and pads the length to a multiple of 5 """
        # converts each letter in string to uppercase and turns string into list
        string_list = list(string.upper())

        # list comprehension that loops through string list and returns a new list
        # adds character to filled_list if character is not a space
        # if character is a space, add random character from self.space_chars instead
        filled_list = [x if x != " " else random.choice(self.space_chars) for x in string_list]

        # we need our string's length to be a multiple of five
        # while our filled_list is not evenly divisible by five
        while len(filled_list) % 5 != 0:
            # adds a random character from self.pad_chars at a random position in the list
            filled_list.insert(random.randint(0, len(string_list)), random.choice(self.pad_chars))

        # joins the characters in filled_list to create a string
        string = "".join(filled_list)

        # we need blocks of text that are five characters long
        num_of_chars = 5

        # uses a list comprehension to split string into blocks that are five characters long
        # joins blocks with a space
        blocks = " ".join([string[i:i+num_of_chars] for i in range(0, len(string), num_of_chars)])

        # returns string of five character blocks
        return blocks

    # combines blocks to return string to it's original format
    def combine_blocks(self, string):
        """ accepts a string formatted into 5 character blocks and returns it to it's original format """
        # converts string to list and replace each space in the list with an empty string
        string_list = list(string.replace(" ", ""))

        # loops through string list and adds character to space_list if character is not in self.space_chars
        # if character is in self.space_chars, adds space instead
        space_list = [x if x not in self.space_chars else " " for x in string_list]

        # loops through space_list and adds character to pad_list if character is not in self.pad_chars
        # if character is in self.pad_chars, adds empty string instead
        pad_list = [x if x not in self.pad_chars else "" for x in space_list]

        # joins characters in pad list to create string
        string = "".join(pad_list)

        # returns string in original format
        return string
