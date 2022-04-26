import random
import string

from datetime import datetime


def get_current_date():
    return datetime.now().strftime("%Y.%m.%d")


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def set_datetime_stamp():
    return get_current_date() + "_" + datetime.now().strftime("%H.%M.%S")


def generate_random_password(length):
    """ Generates a random password containing lowercase, uppercase, digits and punctuation """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    return "".join(random.sample(lower + upper + num + symbols, length))


def generate_random_email(length):
    """ Generates a random email values for length less than prefix and postfix total length
        Generates a random email with format {test_user+/some_string/@test.io} to other cases"""
    prefix = "test_user+"
    postfix = "@test.io"
    mail_min_length = len(prefix) + len(postfix)
    if length <= mail_min_length:
        return generate_random_password(length)
    else:
        infix = generate_random_password(length - mail_min_length)
        return prefix + infix + postfix


def check_if_contains_any(str, set):
    """ Check whether sequence str contains ANY of the items in set. """
    return 1 in [c in str for c in set]


def check_if_contains_all(str, set):
    """ Check whether sequence str contains ALL of the items in set. """
    return 0 not in [c in str for c in set]