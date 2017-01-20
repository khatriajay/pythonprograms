#Program to ask for my name and password

while True:
    print ('Who are you?')
    myname= input()
    if myname != 'ajay':
        continue                                    #Loop back to ask the username
    print (' Welcome ajay. Enter the password:')
    password= input()
    if password == 'ninja':                         #Check the password.
        break
print( 'access granted')
    
