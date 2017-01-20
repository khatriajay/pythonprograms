#Number guess game

import random
secretnum = random.randint (1,15)                     #Selecting a random number between 1 and 15 
print ('I am thinking of a number between 1 and 15')  #Telling the user upper limit and lower limit.

for guessestaken in range (1,6):                      # Specifying number of guesses allowed
    print ('Make a guess')
    guess = int(input())                              #Storing the number entered by user in a variable

    if guess < secretnum:
        print ('The number you entered is lesser in value.')
    elif guess > secretnum:
        print ('The number you entered is higher in value.')
    else:
        break                                         #Correct guess case

if guess == secretnum:
    print('Awesome, you guessed the number in ' + str(guessestaken) + ' guesses.') #Print the number of guesses taken 
else:
    print (' You were not able to guess the number in' + str(guessestaken) + 'guesses. ' + 'The number is ' + str(secretnum) ) #Print the number if not able to guess

