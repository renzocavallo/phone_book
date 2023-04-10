import re

def email_patron(email):
    
    patron = re.compile("^\S+@\S+\.\S+$")
    
    return patron.match(email)

def password_patron(password):

    patron = re.compile("^\S{6,}")

    return patron.match(password)