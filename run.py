from player import HumanPlayer, RandomComputerPlayer
from colorama import Fore, Style

# Define class TicTacToe and Creates a board
class TicTacToe:

    def __init__(self): 
        # Use a list of length nine to represent 3x3 board then assign an index in this length nine list to each of the spaces
        self.board = [' ' for _ in range(9)]
        self.current_winner = None 
        # Create variable self current winner to keep track of wether or not there is a current winner in this game. And if there is who is it?

    def greeting(self):
        print(Fore.GREEN + 'Welcome to Tic-Tic-Toe game')
    
    def instructions(self): 
        # Need to put game rule tomorrow
        print(Style.RESET_ALL + "Here are step-by-step how to play Tic-Tac-Toe.\nTwo players. The human player takes 'X', and the computer player takes 'O'.\nIn with an empty three multiply three grid. This grid consists of three rows and three columns, resulting in a total of nine cells.\nPlayers take turns placing their symbol X or O in any empty cell of the grid\nBy typing the number 0-8 as shown on the first board, each number representing each cell in the board.\nThe first player, 'X', makes the initial move.\nThe objective is to get three of your symbols in a row, either horizontally, vertically, or diagonally.\nThe first player to achieve this wins the game.\n ")

    def print_board(self):
         # Represent three rows by group the number in length nine to three group[(0,1,2),(3,4,5),(6,7,8)]
        for row in [self.board[i*3:(i + 1)*3] for i in range(3)]:
            # Join row in a string where the separator is this vertical line 
            print('| ' + ' | '.join(row) + ' |') 

    # Creates method to print out the number on the board, What number corresponds to what box
    @staticmethod
    def print_board_nums():
        # What indices are in the rows for each of the rows like sub array[(0,1,2),(3,4,5),(6,7,8)](just like on the paint board)
        number_board = [[str(i) for i in range(j*3, (j + 1)*3)] for j in range (3)] 
        for row in number_board:
              print('| ' + ' | '.join(row) + ' |')

    # Create available moves method to tell player what are the available moves after they make a move
    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0:'x'), (1:'x'), (2:'x')]
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If valid move, assign square to letter then make a move then return true if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                # To check for the winner
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check all of 3 in a row anywhere
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]

        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals
        # Only if the square is an even number (0, 2, 4, 6, 8)
        # These are the only moves possible to win a diagonal
        if square % 2 == 0:
            # Left to right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            # Right to left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
            # If all of these fail
        return False
            
# Define the play function outside the TicTacToe class to passing in a game, an X player, and O player to print out the step to tell player
def play(game, x_player, o_player, print_game=True): 
    # Return the winner of the game(the letter)! or None for a tie
    if print_game:
        game.print_board_nums()
    # Starting letter
    letter = 'X' 

    # Iterate while the game still has empty squares
    # Return the winner name using return statement to break out the loop
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # Define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                # Empty line
                print('') 
            if game.current_winner:
                if print_game:
                    print(letter + ' WINS !')
                return letter
            # After player made a move, alternate letter
            # Switches player
            letter = 'O' if letter == 'X' else 'X' 

    if print_game:
            print("It's a tie!")


if __name__ == '__main__':
     # Import human player nad random computer player from player file on the top of the page 
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe() 
    t.greeting()
    t.instructions()
    play(t, x_player, o_player, print_game=True)
    answer = " "
    while answer not in ("Y","N"):
        answer = input("Do you want to play again Y/N ?: \n").upper()
        if answer == "N":
            print("Thanks for playing the game")
            break
        if answer == "Y":
            while True:
                t = TicTacToe() 
                t.greeting()
                t.instructions()
                play(t, x_player, o_player, print_game=True)
                replay = input("Do you want to play again?(Y/N): \n")
        else:
            print("This is an invalid choice")
   


  

     
     