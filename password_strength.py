import re


def get_password_strength(password):

    password_blacklist = ['password', 'qwerty', '12345', '111', '555', '777',
                           'test', 'admin', 'god']
    medium_length = 6
    good_length = 10

    password_length = (len(password) > medium_length) * 2 + \
                      (len(password) > good_length) * 4

    password_has_digit = bool(re.search('[0-9]', password))

    password_has_upper = bool (re.search('[A-ZА-Я]', password))

    password_has_lower = bool(re.search('[a-zа-я]', password))

    password_has_special = bool(re.search('[~!@#$%^&*()_]', password))

    password_has_date = bool(re.search(r'''(0[1-9]|[12][0-9]|3[01])[- /.]
                                       (0[1-9]|1[012])[- /.]\d{2,4}''',
                                       password))

    password_has_bad_word = bool(sum(1 for word in password_blacklist
                                 if re.search(word, password.lower())))

    password_strength = (password_length + password_has_digit * 1 +
                         password_has_upper * 1 +
                         password_has_lower * 1 +
                         password_has_special * 1 -
                         password_has_date * 2 -
                         password_has_bad_word * 3)
    if password_strength < 0:
        password_strength = 1

    return password_strength


if __name__ == '__main__':
    checked_password = input('Your password: ')
    print('''The strength of your password by 10-points scale 
          (1 - weak password, 10 - good password) is : ''',
          get_password_strength(checked_password))
