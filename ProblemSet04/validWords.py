def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    letters = list(word)
    i = 0
    newHand = hand.copy()
 
    while i < len(word):
        if letters[i] in newHand and newHand[letters[i]] > 0:
            letterNum = newHand[letters[i]]
            letterNum -= 1
            newHand[letters[i]] = letterNum
            i += 1
        else:
            return False
    return word in wordList
