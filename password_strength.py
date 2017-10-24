import re


def get_password_strength(password):
    password_black_list = ['password', 'qwerty', '12345', '111', '555', '777',
                           'test', 'admin', 'god']

    password_length = (len(password) > 1) * 0 + (len(password) > 6) * 2 + \
                      (len(password) > 10) * 4

    password_has_digit = (re.search('[0-9]', password) != None)

    password_has_upper = (re.search('[A-ZА-Я]', password) != None)

    password_has_lower = (re.search('[a-zа-я]', password) != None)

    password_has_special = (re.search('[~!@#$%^&*()_]', password) != None)

    password_has_date = (re.search(r'\d{2}-\d{2}-\d{4}', password) != None)

    password_has_bad_word = (sum(1 for word in password_black_list
                                 if re.search(word, password.lower())) > 0)

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
    print('The strength of your password by 10-points scale '
          '(1 - weak password, 10 - good password) is : ',
          get_password_strength(checked_password))
