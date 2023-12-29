from random import choice, randint
from string import ascii_letters, digits, punctuation
from datetime import datetime

def storing_password(password):
    with open("./resources/passwords.txt",'a+') as note:
        note.write(f"Password:{password} - length of password:{len(password)} - timestamp:{datetime.now()}\n")

if __name__ == "__main__":
    character = digits+ascii_letters+punctuation
    length_of_password = randint(8,16)
    password = "".join(choice(character)for every_character in range(length_of_password))
    storing_password(password)
