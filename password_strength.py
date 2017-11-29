import sys
import getpass
import re
import string


def load_blacklist_file(blacklist_file):
    try:
        with open(blacklist_file, 'r') as file:
            return file.readlines()

    except FileNotFoundError:
        return []


def make_blacklist(user_blacklist):
    blacklist = [line.strip('\n ') for line in user_blacklist
                 if line.strip('\n ')]
    blacklist.append(getpass.getuser())
    return blacklist


def get_password_strength(password, password_blacklist):
    medium_length = 6
    good_length = 10
    min_password_strength = 1

    date_pattern = r'''(0[1-9] | [12][0-9] | 3[01])   #день 01-31
                           [- /.]
                           (0[1-9] | 1[012])          #месяц 01-12
                           [- /.]
                           \d{2,4}'''                 # год, 2/4 значный

     password_strength = max(((len(password) > medium_length) * 2
                             + (len(password) > good_length) * 4
                             + bool(re.search('[0-9]', password))
                             + bool(re.search('[A-ZА-Я]', password))
                             + bool(re.search('[a-zа-я]', password))
                             + any(char in password for char
                                   in string.punctuation)
                             - bool(re.search(date_pattern, password,
                                              re.VERBOSE))
                             - any(bad_word for bad_word in password_blacklist
                                   if bad_word in password.lower()) * 2),
                             min_password_strength)

    return password_strength


if __name__ == '__main__':

    user_password = getpass.getpass()
    try:
        user_blacklist = load_blacklist_file(sys.argv[1])

    except IndexError:
        user_blacklist = []

    blacklist = make_blacklist(user_blacklist)
    print('''The strength of your password by 10-points scale
              (1 - weak password, 10 - good password) is :''',
              get_password_strength(user_password, blacklist))
