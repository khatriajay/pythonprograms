#! /usr/bin/env python3

# Collatz sequence using Python3

def collatz(num):           #Function definition
    if ( num%2==0):
        a= num //2
        return a
    else:
        b= num*3 +1
        return b
print ('Enter a number:')
n=int(input())
while n !=1:                #loop until entered number becomes 1
    n= collatz(n)           # Call Function
    print(n)

 

        
