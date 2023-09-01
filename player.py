import random
import math

# Creates base player class 
class Player:
    """
    Creates an instance of Player
    """
    def __init__(self, letter): # InputName is the name that the player picks their name
       self letter = letter
    
    def get_move(self, game):  # All the player be able to get their next move 
        square = random.choice(game.available_moves())
        return square
  
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
      pass
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
      pass
      
    
    
    
    

  