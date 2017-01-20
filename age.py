#Program to print the name, calculate name length and predict 5 year age from now.

print ('Hello world')
print ('What is your name?')
myname= input()                         #Get input from user
print ('Good to see you,' + myname);
print ('The length of your name is:')
print (len(myname))                     #Calculate the lenght of name
print ('What is your age?')
myage= input()                          #Get age from user
print ('You will be ' + str(int(myage) +5) + ' in 5 years from now')
