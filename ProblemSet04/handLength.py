def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    letters = list(hand)
    total = 0
    i = 0
 
    while i < len(letters):
        total += hand[letters[i]]
        i += 1
    return total  
