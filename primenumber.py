#! /usr/bin/env python3

#Program to find whether the entered number is prime or not

print('Enter a number:')
n= int(input())                     # Take the number n from user
sum=0
if n>1:
    for i in range (2, n):          #Check divisibility continuously till n
        if (n %i)==0:
            print ('Not a prime')
            break                   #Exit if not a prime
    else:
            print('Number is prime')
