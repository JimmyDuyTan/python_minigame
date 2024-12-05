import random
NUM_DIGITS = 3 # try to setting this 1 to 10
MAX_GUESSES = 10 #Try setting this 1 to 100

def main():

    print('''Bagels, a deductive logic game.
    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    
    When I say: That means:
    Pico One digit is correct but in the wrong position.
    Fermi One digit is correct and in the right position.
    Bagels No digit is correct.
    
    For example, if the secret number was 248 and your guguess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    #start game
    while True: #Main game loop
        # this stores secret number the players need to guess
        secretNum = getSecretNumber()
        print('I have thought up a number')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # break a loop if they're correct
            if numGuesses > MAX_GUESSES:
                print('You ran out of your turns')
                print('The answer was {}.'.format(secretNum))
        #Ask player if they want to play agian
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getSecretNumber():
    numbers = list('123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit in correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues == 0):
        return 'Bagels' # none of digits is correct
    else:
        #Sort the clues into alphabetical order so their original order
        #doesn't give infomation away
        clues.sort()
        # make a single string form the list of string clues
        return ''.join(clues)
