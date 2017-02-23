#! /usr/bin/env python3

#Python3 program for checking if you have a pet with name entered.

petname= ['rosie', 'jack', 'roxy', 'blossom']    #Define a list with pet names
print (' Enter your pet name')
name = input()
if name not in petname:                         #Check if name exists in list
    print ('You dont have a pet named ' + name )
else:
    print ('Your pet ' + name + ' missed you while you were away')
