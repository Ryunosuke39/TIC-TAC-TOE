import math 
import random 


class Player:
    def __init__(self, letter):
        # letter is o or x
        self.letter = letter
    # we want all player to get their next move given name
    def get_move(self, game):
        pass

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
