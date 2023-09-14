import random
import math
from colorama import Fore, Back, Style

class Player:
    """ Creates an instance of Player """
    def __init__(self, letter): 
       # letter is the name that the player picks their name
       self.letter = letter
    
    def get_move(self, game):  
        # All the player be able to get their next move 
        pass
  
class RandomComputerPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
      # Get a random valid spot for player next move
      square = random.choice(game.available_moves())
      return square
    
class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        valid = None

        while not valid_square:

            square = input (Style.RESET_ALL + self.letter + "\'s turn. Input move (0-8):\n")
            try: 
                # Check this is a correct value by try to cast
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except ValueError:
                # If that spot is not available on the board, print out "invalid" to tell player
                print(Fore.RED + 'Invalid square. Try again.')

        return val