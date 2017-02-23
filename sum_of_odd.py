#! /usr/bin/env python3 

#Program to find sum of odd numbers, maximum range specified by user

print ('Enter the upper limit for calculating sum:')
num = int(input())
sum=0
while num >0:
    if num % 2!=0:              #Condition to check odd
        sum = sum + num
        num = num-2
    else:
        num=num-1               # If a user enters even number
print('The sum of odd numbers is: ' + str(sum))                      # Print total sum
    
