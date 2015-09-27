def playGame(wordList):
  hand = False
  while True:
      user = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ").lower()
      if user not in 'nre':
          print("Invalid command.")
      else:
          if user == 'r' and not hand:
              print("You have not played a hand yet. Please play a new hand first!")
          elif user == 'n':
              hand = dealHand(HAND_SIZE)
              playHand(hand.copy(), wordList, HAND_SIZE)
          elif user == 'r' and hand:
              playHand(hand.copy(), wordList, HAND_SIZE)
          else:
              break
          print("")