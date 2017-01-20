# Collatz sequence using Python

def collatz(num):                           #Function definition
    if ( num%2==0):
        a= num //2
        print(a)
        return a
    else:
        b= num*3 +1
        print(b)
        return b
print ('Enter a number:')
n = input()                                 # User to enter a number
try: 
    while n !=1:                            # Condition for generating sequence untill the number becomes one.
        n= collatz(int(n))                  #Functional Call 
except ValueError:
    print ('Enter only integer values. ')   #Exception case for non int values entered by user  

