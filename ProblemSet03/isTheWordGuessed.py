def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    true = 0
    false = 0
    for char in secretWord:
        if char in lettersGuessed:
            true += 1
        else:
            false +=1
    if false == 0:
        return True
    else:
        return False
