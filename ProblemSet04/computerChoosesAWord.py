def compChooseWord(hand, wordList, n):
    return max([x if isValidWord(x, hand, [x]) else "" for x in wordList], 
               key=lambda x: getWordScore(x, n)) or None