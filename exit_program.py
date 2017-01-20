# program to make user type exit to exit the program


import sys                          # Import module

while True:                         #always true by default
    print (' Type exit to exit:')
    response=input()                
    if response == 'exit':          # Condition check
        sys.exit()                  
    print ('You typed ' + response + '.')
           
    
