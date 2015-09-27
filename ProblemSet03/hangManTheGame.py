def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessLeft = 8
    
    # create a list to store lettersGuessed
    lettersGuessed = [ ]
    
    # find the length of the secretWord
    k = len(secretWord)
    
    # print intro text, tell user the word length
    print str('Welcome to the game, Hangman!')
    print str('I am thinking of a word that is ' + str(k) + ' letters long.')
    print str('-------------')
    
    # while guessLeft is greater than zero (while user still has guesses left)
    while guessLeft > 0:
        
        # print how many guesses are left
        print str('You have ' + str(guessLeft) + ' guesses left.')
        
        # print available letters
        print str('Available letters: ') + getAvailableLetters(lettersGuessed)
        
        # prompt user to guess a letter
        guess = raw_input('Please guess a letter: ')
        
        # make sure letter entered is lowercase
        guessLower = guess.lower()
        
        # add the entered letter to lettersGuessed
        lettersGuessed.append(guessLower)
        
        # if the letter guessed is already in lettersGuessed, print Oops message and show progress using getGuessedWord function
        if lettersGuessed.count(guessLower) > 1:
            print str("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
            print str('-------------')
        
        # if the letter guessed is in secretWord, show progress (including the guess) using getGuessedWord function
        elif guessLower in secretWord:
            print str('Good guess: ') + getGuessedWord(secretWord, lettersGuessed)
            print str('-------------')
            
            # if they've guessed the entire word, print Congrats message and break out of the loop
            if isWordGuessed(secretWord, lettersGuessed) == True:
                return str('Congratulations, you won!')
                break
        # otherwise, if letter not in secretWord, decrement guessLeft by 1 and show progress using getGuessedWord function
        else:
            guessLeft -= 1
            print str('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
            print str('-------------')
    # if guessLeft is not >0, tell the user they ran out of guesses and print the secretWord
    else:
        return str('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')