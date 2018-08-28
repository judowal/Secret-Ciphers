# imports sys module
import sys

# imports Cipher class from cipher module
from cipher import Cipher

# imports Atbash class from atbash module
from atbash_cipher import Atbash

# imports Affine class from affine module
from affine_cipher import Affine

# imports Keyword class from keyword module
from keyword_cipher import Keyword


# creates App class that inherits from Cipher
class App(Cipher):
    """ creates App class that contains and runs code that will interface with the user """
    def __init__(self):
        """ initializes class's starting values """
        super().__init__()
        self.user_name = ""
        self.functionality = ""
        self.cipher = ""
        self.message = ""
        self.pad_confirmed = False

    # closes the app
    def exit_app(self):
        """ thanks the user for using the app, then closes the app """
        # thanks the user for using the app
        print("\nThank you for choosing The Cipher. Goodbye {}.".format(self.user_name))

        # exits the app
        sys.exit()

    # greets the user
    def greeting(self):
        """ stores the user's name, greets the user, and calls confirm_pad() """
        # prints app title
        print("===== The Cipher =====\n")

        # prompts the user to enter a name and assigns value to self.user_name
        self.user_name = input("Please enter your name:  ")

        # greets the user
        print("\nHello {}. Welcome to The Cipher!\n".format(self.user_name))

        # describes the app
        print("This app can encrypt and decrypt secret messages using three different ciphers.\n")

        # prompt the user to enter the correct one time pad
        self.confirm_pad()

    # prompts the user to enter the one time pad
    def confirm_pad(self):
        """ prompts the user to confirm the one time pad and calls set_functionality(), or exits the app, """
        # while self.pad_confirmed is false:
        while not self.pad_confirmed:
            # prompts the user for the one time pad
            pad = input("To get started, please enter the one time pad:  ")

            # if user enters the correct one time pad
            if pad == self.pad:
                # sets self.pad_confirmed to true and exits loop
                self.pad_confirmed = True

            # if user enters "exit"
            elif pad == "exit":
                # exits app
                self.exit_app()

            # if user enters anything else
            else:
                # informs the user that an invalid pad was entered
                print("\nInvalid pad.")

        # call function that selects encryption or decryption functionality
        self.set_functionality()

    # selects encryption or decryption functionality
    def set_functionality(self):
        """ prompts the user to select a functionality and calls set_cipher(), or exits the app """
        # while self.functionality has no value set
        # loop will run until user enters 1, 2, or "exit"
        while self.functionality == "":
            # prompts the user to select encryption or decryption
            functionality = input("\nPlease enter 1 to encrypt a message or 2 to decrypt a message:  ")

            # if user enters 1 or 2
            if functionality in ["1", "2"]:
                # set self.functionality to functionality
                self.functionality = functionality

            # if user enters "exit"
            elif functionality == "exit":
                # exits the app
                self.exit_app()

        # call function that prompts the user to choose a cipher
        self.set_cipher()

    # prompts the user to choose a cipher
    def set_cipher(self):
        """ prompts the user to select a cipher and calls capture_input(), or exits app """
        # while self.cipher has no value set
        # loop will run until user enters 1, 2, 3, or "exit"
        while self.cipher == "":
            # prints selectable ciphers
            print("\n1. Affine")
            print("2. Atbash")
            print("3. Keyword\n")

            # prompts the user to choose a cipher
            cipher = input("Now enter the number of the cipher you would you like to use:  ")

            # if user enters 1, 2, or 3
            if cipher in ["1", "2", "3"]:
                # set self,cipher to cipher
                self.cipher = cipher

            # if user enters "exit"
            elif cipher == "exit":
                # exit app
                self.exit_app()

        # call function that prompts user to enter the string to be encrypted or decrypted
        self.capture_input()

    # prompts the user to input the string to be encrypted or decrypted
    def capture_input(self):
        """ captures the message to be encrypted or decrypted and calls string_check(), or exits the app """
        # while self.message has no value set
        # loop will run until user enters 1, 2, or "exit"
        while self.message == "":
            # if self.functionality is set to "1"
            if self.functionality == "1":
                # inform the user of the input's requirements
                print("\nIn order to be encrypted, messages must be comprised of only letters and spaces.")

                # prompt the user to enter the string to be encrypted
                message = input("\nPlease enter the message you want to encrypt:  ")

                # if user enters exit
                if message == "exit":
                    # exit app
                    self.exit_app()

                # if user enters anything else
                else:
                    # call function that checks string to see if it can be encrypted or decrypted
                    self.string_check(message)

            # if self.functionality is set to "2"
            elif self.functionality == "2":
                # prompts user for the string to be decrypted
                message = input("\nPlease enter the message you want to decrypt:  ")

                # if user enters exit
                if message == "exit":
                    # exit app
                    self.exit_app()

                # if user enters anything else
                else:
                    # call function that checks string to see if it can be encrypted or decrypted
                    self.string_check(message)

    # checks strings to see if they can be encrypted or decrypted
    def string_check(self, string):
        """ accepts a string to be checked for decryption/encryption eligibility, calls crypter() if eligible """
        # if self.functionality is set to "1"
        if self.functionality == "1":
            # if string contains only letters and spaces
            if all(x.isalpha() or x.isspace() for x in string):
                # sets self.message to string
                self.message = string

                # calls function that encrypts or decrypts messages
                self.crypter()

            # if string contains characters other than letters and spaces
            else:
                # prompt the user to enter a string containing only letters and spaces
                print("\nPlease enter a string containing only letters and spaces.")

        # if self.functionality is set to "2"
        elif self.functionality == "2":
            # if string contains only letters, spaces, space_chars, or pad_chars
            if all(x.isalpha() or x.isspace() or x in Cipher().space_chars or x in Cipher().pad_chars for x in string):
                # sets self.message to string
                self.message = string

                # calls function that encrypts or decrypts messages
                self.crypter()

            # if string contains characters that cannot be decrypted
            else:
                # prompt the user to enter a valid string to be decrypted
                print("\nPlease enter a valid string to be decrypted.")

    # gives user the option to run the app again or exit
    def loop(self):
        """ thanks the user for using the app, and prompts them to continue using the app or exit the app """
        # loop will run until user enters yes or no
        while True:
            # thanks the user for using the app
            print("\nThanks for choosing The Cipher {}.\n".format(self.user_name))

            # prompts the user to encrypt/decrypt another string or exit the program
            run_again = input("{}, would you like to encrypt or decrypt another message [Y/n]?  ".format(self.user_name))
            print("\n")

            # if user enters "yes" or "y
            if run_again.lower() == "yes" or run_again.lower() == "y":
                # reinitialize the class, resetting all attributes to their starting values
                self.__init__()

                # restarts the app
                self.greeting()

            # if the user enters "no or "n"
            elif run_again.lower() == "no" or run_again.lower() == "n":
                # exit the app
                self.exit_app()

    # encrypts or decrypts string with the selected encryption
    def crypter(self):
        """ encrypts or decrypts a string using the chosen cipher """
        # if self.functionality is set to "1"
        if self.functionality == "1":
            # if self.cipher is set to "1"
            if self.cipher == "1":
                # use the affine cipher to encrypt self.message
                Affine(self.message).encrypt()

            # if self.cipher is set to "2"
            elif self.cipher == "2":
                # use the atbash cipher to encrypt self.message
                Atbash(self.message).encrypt()

            # if self.cipher is set to "3"
            elif self.cipher == "3":
                # use the keyword cipher to encrypt self.message
                Keyword(self.message).encrypt()

        # if self.functionality is set to "2"
        elif self.functionality == "2":
            # if self.cipher is set to "1"
            if self.cipher == "1":
                # use the affine cipher to decrypt self.message
                Affine(self.message).decrypt()

            # if cipher is set to "2"
            elif self.cipher == "2":
                # use the atbash cipher to decrypt self.message
                Atbash(self.message).decrypt()

            # if cipher is set to "3"
            elif self.cipher == "3":
                # use the keyword cipher to decrypt self.message
                Keyword(self.message).decrypt()

        # prompt the user to continue using the app or exit
        self.loop()


# if the __name__ of this file is "__main__"
if __name__ == "__main__":
    # run app
    App().greeting()
