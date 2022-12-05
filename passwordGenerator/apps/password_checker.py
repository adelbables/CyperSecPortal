import string


def validate_password(passwd):
    password_strength = {0 :"Weak", 1: "Ok", 2 :"Good", 3:"Strong"}
    conditions_met = 0
    capital_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    #check if the Password contain min a capital letter, digit or a symbol
    if len(passwd) >= 8:
        if any(s in passwd for s in capital_letters):
            conditions_met +=1
        if any(s in passwd for s in digits):
            conditions_met +=1
        if any(s in passwd for s in symbols):
            conditions_met +=1
    else: conditions_met = 0

    return password_strength[conditions_met]
