from player import HumanPlayer, RandomComputerPlayer
from colorama import Fore, Back, Style
from simple_term_menu import TerminalMenu

class TicTacToe:
    """ Define class TicTacToe and Creates a board """
    def __init__(self): 
        """ Use a list of length nine to represent 3x3 board then assign an 
        index in this length nine list to each of the spaces """
        self.board = [' ' for _ in range(9)]
        # Create variable self current winner to keep track of wether or not there is a current winner in this game. And if there is who is it?
        self.current_winner = None 

    def greeting(self):
        print(Fore.YELLOW + 'Welcome to Tic-Tic-Toe GAME!!!')
    
    def instructions(self): 
        """ instruction method to explain rule """
        print(f"""{Fore.BLUE}
    Here are step-by-step how to play Tic-Tac-Toe.
Two players, human player takes 'X', and random computer player takes 'O'.
In with an empty three multiply three grid. This grid consists of three rows and three columns,
resulting in a total of nine cells.
- Players take turns placing their symbol X or O in any empty cell of the grid 
  by typing the number 0-8 as shown on the first board.
- Each number representing each cell in the board.
- The human player 'X' makes the initial move.
- The random computer player will generate the number to move automatically.
- The objective is to get three of your symbols in a row, either horizontally, vertically, or diagonally.
- The human player to achieve this wins the game.
- You can stop or continue to play by selecting a simple menu using the arrow up and down 
  to enter Play Again or Quit.
      
      """) 
    def print_board(self):
        """ print board method to print out the first board """
        formatted_board_lines = ['| ' + ' | '.join(self.board[i*3:(i + 1)*3]) + ' |' for i in range(3)]
        formatted_board = '\n'.join(formatted_board_lines)
        print(formatted_board)

    @staticmethod
    def print_board_nums():
        """ Creates method to print out the number on the board(What number corresponds to what box) """
        number_board = [f'{i}' for i in range (9)]
        number_board = [number_board[i:i+3] for i  in range(0, 9, 3)] 
        for row in number_board: 
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """ This method to create available moves(to tell player what are the available moves after they make a move """
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        """ if valid move this method will assign square to letter then make a move then return true if invalid return false"""
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                # To check for the winner
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """ This method to check all of 3 in row anywhere"""
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]

        if all([spot == letter for spot in column]):
            return True
        
        # Check diagonals Only if the square is an even number (0, 2, 4, 6, 8)(These are the only moves possible to win a diagonal)
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
            
def play(game, x_player, o_player, print_game=True): 
    """ Define the play function outside the TicTacToe class to passing in a game, an X player, and O player to print out the step to tell player """
    # Return the winner of the game(the letter)! or None for a tie
    if print_game:
        game.print_board_nums()
    letter = 'X' 

    # Iterate while the game still has empty squares, return the winner name using return statement to break out the loop
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
                    print(Fore.GREEN + letter + ' WINS !')
                return letter
            # After player made a move, alternate letter
            # Switches player
            letter = 'O' if letter == 'X' else 'X' 

    if print_game:
            print("It's a tie!")


if __name__ == '__main__':
    # Import human player nad random computer player from player file to the top of the page first
    options = ["Play Again", "Quit"]

    while True:
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = TicTacToe() 
        t.greeting()
        t.instructions()
        play(t, x_player, o_player, print_game=True)
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if menu_entry_index == 0:
            print("Play Again")
            continue
        else:
            print(Fore.YELLOW + "Thanks for playing the game Goodbye!!!")
            break
