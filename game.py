
# Define class TicTacToe and Creates a board
class TicTacToe:
    def __init__(self): # Use a list of length nine to represent 3x3 board then assign an index in this length nine list to each of the spaces
        self.board = [' ' for _ in range(9)]
        self.current_winner = None # Create variable self current winner to keep track of wether or not there is a current winner in this game. And if there is who is it?
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: # Represent three row by group the number in length nine to three group[(0,1,2),(3,4,5),(6,7,8)]
            print('| ' + ' | '.join(row) + ' |') # Join row in a string where the separator is this vertical line
