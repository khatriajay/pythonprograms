#! /usrbin/env python3

#Program to store birthday of friends in a dictionary

birthday = {'ajay': '10 Mar' , 'tinto' : '10th May', 'ravi': '19 Oct'}
while True:
    print ('Enter a name: ')
    name = input()
    if name == '':
        break                     #Empty name, exit immediately
    if name in birthday:          #If name is found
        print ('The birth date of ' + name + ' is ' + birthday[name])
    else:
        print('Sorry, I do not have their birthday.')
        print ('Enter this person birthday')
        dob= input()              #Store new birthday in dictionary.
        birthday[name]= dob
        print('Birthday db updated')

    
