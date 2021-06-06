import string
import random

def generate_random_email_password(domain=None, email_prefix=None):
    """

    :param domain:
    :param email_prefix:
    :return:
    """
    if not domain:
       domain = "supersqa.com"
    if not email_prefix:
        email_prefix = "testuser"

    random_email_string_length = 10
    random_string = "".join(random.choices(string.ascii_lowercase, k = random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    random_password_length = 20
    password = "".join(random.choices(string.ascii_letters, k = random_password_length))


    random_info = {'email': email, 'password': password}
    print(random_info)

    return random_info

def generate_random_fnama_lname(first_prefix = 'test f', last_prefix = 'test l'):
    random_fname = first_prefix + "".join(random.choices(string.ascii_lowercase, k=7))
    random_lname = last_prefix + "".join(random.choices(string.ascii_lowercase, k=7))

    return {'first_name':random_fname, 'last_name':random_lname}

def generate_random_coupon_code(sufix=None, length = 10):
    code = "".join(random.choices(string.ascii_uppercase, k=length))
    if sufix:
        code += sufix

    return code