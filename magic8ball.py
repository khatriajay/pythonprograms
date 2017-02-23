#! /usr/bin/env python3

#python3 program for magic 8 ball

import random      #import random module
messages = ['certain' , 'decidely' , 'definitely' , 'reply hazy try again', 'ask again', 'concentrate and ask again' , 'no' , 'outlook not good' , 'very doubtful']
r = random.randint(0,len(messages)-1)    #generate random integer every run
print (messages[r])
