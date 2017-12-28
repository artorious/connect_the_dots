#!/usr/bin/env python3
"""
Game board interface using text-output and keyboard-only-input
"""
from dot_3x3_logic import initialize_board
from dot_3x3_logic import add_line
from dot_3x3_logic import square_owner
from dot_3x3_logic import check_line
from dot_3x3_logic import winner
from dot_3x3_logic import current_player

def show_player(player):
    """(str) -> str
    Determines the string to print in the context of a square's 
    owner <player>
    """
    return

def draw_game():
    """(None) -> str
    Draws the connect the dot game using text graphics
    """
    # TODO: 0---1---2   ----------------------------------

    # TODO: |   |   |   ----------------------------------

    # TODO: 3---4---5   ----------------------------------

    # TODO: |   |   |   ----------------------------------

    # TODO: 6---7---8   ----------------------------------

    pass

def make_line(move):
    """(str) -> str
    Determines the line between two dots specified in the string <move>
    The <move> parameter is one of '01', '12', '03' etc. representing a line
    connecting the dots in the pattern;
        0---1---2
        |   |   |
        3---4---5
        |   |   |
        6---7---8
    Returns the string that reprsents the line position between the dots, one
    of 'North_Northwest', 'Center_North' etc. If the dot1, dot2 pair 
    represents an invalid combination e.g (0, 4), returns string 'No line'
    """
    return


if __name__ == '__main__':
    # Start a new game
    initialize_board()
    draw_game()
    winning_player = None   # No winner at start
    
    while not winning_player:
        prompt = 'Move for player {0} : '.format(current_player())
        move = input(prompt)    # Get the dots to connect
        
        if move == 'Q' or move == 'q' : # 'Q' quits the program
            break
        
        print()
        
        new_line = make_line(move) # Add the line if possible
        
        if new_line != 'No line' and add_line(new_line):
            draw_game()

        else:
            print('Connection not possible')
        
        winning_player = winner() # Check for win

    # Determine winner, either player X or player Y
    if winning_player == 'X':
        print('X won')

    elif winning_player == 'Y':
        print('Y won')

    else:
        print('Draw')
    
    print('\n**** GAME OVER ****')