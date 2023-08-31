import random
import math

# Creates base player class 
class Player:
    """
    Creates an instance of Player
    """
    def __init__(self, inputName): # InputName is the name that the player picks their name
       self.inputName = inputName
    
    def get_move(self, game):  # All the player be able to get their next move 
        pass
  
class RandomComputerPlayer(Player):
    def __init__(self, inputName):
        super().__init__(inputName)
        
    def get_move(self, game):
      pass
    
class HumanPlayer(Player):
    def __init__(self, inputName):
        super().__init__(inputName)
        
    def get_move(self, game):
      pass
      
    
    
    
    

  