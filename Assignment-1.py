#!/usr/bin/env python
# coding: utf-8

#1. Write a Python program to print the following string in a specific format.


poem = """Twinkle, twinkle, little star,
                How I wonder what you are!
                        Up above the world so high,
                        Like a diamond in the sky.

          Twinkle, twinkle, little star,
                How I wonder what you are"""
print(poem)


# Write a Python program to get the Python version you are using


import platform
print('Python current version')
print(platform.python_version())


# Write a Python program to display the current date and time.


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# Write a Python program which accepts the radius of a circle from the user
# and compute the area.


radius = int(input('Please enter the value of circle radius'))
area = 3.14 * (radius ** 2 )
print('Area')
print(area)


# Write a Python program which accepts the user's first and last name and
# print them in reverse order with a space between them.


firstName = input('Please enter first name')
lastName = input('Please enter last name')
print('Reversed full name')
print(lastName + ' ' + firstName)


# Write a python program which takes two inputs from user and print them
# addition


value1 = int(input('Please enter value-1 for addition'))
value2 = int(input('Please enter any value-2 for addition'))
print('Total') 
print(value1 + value2)




