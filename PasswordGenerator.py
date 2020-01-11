#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

length = input('Enter the length of the password: ')
length = int(length)

password = ''

for c in range(length):
	password += random.choice(chars)
print(password)
