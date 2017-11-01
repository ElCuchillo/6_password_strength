import sys
import getpass
import re
import string


def load_blacklist_file(blacklist_file=''):

    try:
        with open(blacklist_file, 'r') as loaded_data:
            return loaded_data.readlines()

    except FileNotFoundError:
        return []

    
def complete_blacklist(loaded_data):

    blacklist = (list(filter(None,[line.rstrip('\n')
                                  for line in loaded_data])))
    blacklist.append(getpass.getuser())

    return blacklist


def get_password_strength(password, password_blacklist):

    medium_length = 6
    good_length = 10

    password_length = (len(password) > medium_length) * 2 + \
                      (len(password) > good_length) * 4

    password_has_digit = bool(re.search('[0-9]', password))

    password_has_upper = bool (re.search('[A-ZА-Я]', password))

    password_has_lower = bool(re.search('[a-zа-я]', password))

    password_has_special = bool([char for char in set(string.punctuation)
                                 if char in password])

    password_has_date = bool(re.search(r'''(0[1-9]|[12][0-9]|3[01])[- /.]
                                       (0[1-9]|1[012])[- /.]\d{2,4}''',
                                       password))

    password_has_bad_word = \
        bool(list(filter(lambda x: x in password.lower(),
                         password_blacklist)))

    password_strength = (password_length + password_has_digit * 1 +
                         password_has_upper * 1 +
                         password_has_lower * 1 +
                         password_has_special * 1 -
                         password_has_date * 1 -
                         password_has_bad_word * 2)
    if password_strength < 0:
        password_strength = 1

    return password_strength


if __name__ == '__main__':

    checked_password = getpass.getpass()
    try:
        loaded_data = load_blacklist_file(sys.argv[1])
    except IndexError:
        loaded_data = load_blacklist_file()

    blacklist = complete_blacklist(loaded_data)
    print('''The strength of your password by 10-points scale 
          (1 - weak password, 10 - good password) is : ''',
          get_password_strength(checked_password, blacklist))
