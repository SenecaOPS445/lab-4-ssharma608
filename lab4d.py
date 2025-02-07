#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str1):
    # Place code here - refer to function specifics in section below
    first = str1[0:5]
    return first

def last_seven(str1):
    # Place code here - refer to function specifics in section below
    seven = str1[-7:]
    return seven

def middle_number(num1):
    # Place code here - refer to function specifics in section below
    number = str(num1)
    middle = number[1:3]
    return middle

def first_three_last_three(str1, str2):
    # Place code here - refer to function specifics in section below
    ftlt = str1[0:3] + str2[-3:]
    return ftlt

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
