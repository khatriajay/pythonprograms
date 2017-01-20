# Collatz sequence using Python

def collatz(num):           #Function definition
    if ( num%2==0):
        a= num //2
        print(a)
        return a
    else:
        b= num*3 +1
        print(b)
        return b
print ('Enter a number:')
n=int(input())
while n !=1:                #loop until entered number becomes 1
    n= collatz(n)   

 

        
