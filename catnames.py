#! /usr/env/bin python3

#Storing cat names as list program

nameofcats= []                                                   #Store cat names as a list
while True:
    print ('Enter the name of cat ' + str(len(nameofcats) +1))   #Enter the names of cat and display the count as well
    name = input()
    if name == '':                                               # Blank or no name exits the loop, otherwise the names keep on adding. 
        break
    nameofcats = nameofcats + [name]                             # List concatenation
print ('The cat names are: ')
for name in nameofcats:                                          # Loop to print the name of every cat 
           print (name)
