# Collatz sequence using Python

def collatz(num):                           #Function definition
    if ( num%2==0):
        return num //2
    else:
        return num*3 +1
print ('Enter a number:')
n = input()                                 # User to enter a number
try: 
    while n !=1:                            # Condition for generating sequence untill the number becomes one.
        n= collatz(int(n))                  #Functional Call
        print(n)
except ValueError:
    print ('Enter only integer values. ')   #Exception case for non int values entered by user  

