# Password Strength Calculator

When launching the script asks a password, then examines its strength by following points:
1. length of the password
1. does password have a digit symbol
1. does password consist of a lowercase character
1. does password consist of a uppercase character
1. whether password has a sequence of digits in date format dd[-./]mm[-./]yyyy, dd[-./]mm[-./]yy
1. whether password has words form a password black list like 'password', '12345', username and so on.

Based on these points the script calculates the strength of the password by 10-points scale and outputs 
result to console.

# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python3 password_strength.py <path to file>
```
Where parameter `<path to file>` specifyes a file containing a list of the words not recommended for the  password.
If launching the script without parameters then blacklist includes the Username only.

Output example as following:

```
Your password: Password1
The strength of your password by 10-points scale (1 - weak password, 10 - good password) is :  2
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
