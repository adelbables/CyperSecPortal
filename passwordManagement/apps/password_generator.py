import random
import string


def create_password(length: int, use_capital_letters=False, use_digits=False, use_symbols=False):
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    password_contain = small_letters
    v = 0

    # check which parameter selected
    if use_capital_letters:
        v += 1
    if use_digits:
        v += 2
    if use_symbols:
        v += 4

    # add the wanted values to the password
    match v:
        case 1:
            password_contain += capital_letters
        case 2:
            password_contain += digits
        case 3:
            password_contain += capital_letters
            password_contain += digits
        case 4:
            password_contain += symbols
        case 5:
            password_contain += capital_letters
            password_contain += symbols
        case 6:
            password_contain += digits
            password_contain += symbols
        case 7:
            password_contain += capital_letters
            password_contain += digits
            password_contain += symbols

    # generate the password
    temp = random.sample(password_contain, length)
    password = "".join(temp)

    return password
