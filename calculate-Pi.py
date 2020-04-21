import math

def generatePiToNth():
    Pi = str(math.pi)
    print('Welcome to the Genereate Pi to the Nth term game! How many decimal places in Pi  would you like to go? Please pick a number between 1 and 15.')
    userNumber = int(input())

    if userNumber > 15 or userNumber == '':
        print('You need to pick a number from 1 to 15 for the game to work!')
        playAgain()
    elif userNumber <= 0:
        print('You can go higher than that! You need to pick a number from 1 to 15 for the game to work!')
        playAgain()
    else:
        userNumberPlusTwo = int(userNumber) + 2  #This is to get the correct value for indexing the string
        print('Pi to ' + str(userNumber) + ' decimal places is: ' + Pi[0:userNumberPlusTwo])
        playAgain()

def playAgain():
    print('Would you like to go again? Please state Yes if so.')
    userAnswer = input()
    if userAnswer.upper() == 'YES':
        generatePiToNth()
    else:
        print('Thanks for playing!')
        return

generatePiToNth()