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
    if player:
        return repr(player.strip())
    else:
        return ''

def draw_game():
# TODO: Fix alignment
    """(None) -> str
    Draws the connect the dot game using text graphics
    """
    # 0---1---2   ----------------------------------
    print('   0', end='')
    if check_line('North_Northwest'):
        print('---', end='')
    
    else:
        print('   ', end='')

    print('1', end='')
    if check_line('North_Northeast'):
        print('---', end='')
    
    else:
        print('   ', end='')

    print('2')

    # |   |   |   ----------------------------------
    
    if check_line('West_Northwest'):
        print('   |', end='')
    else:
        print('    ', end='')
    
    print(show_player(square_owner('top_left')), end='')

    if check_line('North_Center'):
        print('  |', end='')
    else:
        print('   ', end='')
    
    print(show_player(square_owner('top_right')), end='')

    if check_line('East_Northeast'):
        print('  |')
    else:
        print('   ')

    # 3---4---5   ----------------------------------

    print('   3', end='')
    if check_line('West_Center'):
        print('---', end='')
    
    else:
        print('   ', end='')

    print('4', end='')
    if check_line('East_Center'):
        print('---', end='')
    
    else:
        print('   ', end='')

    print('5')

    # |   |   |   ----------------------------------

    if check_line('West_Southwest'):
        print('   |', end='')
    else:
        print('   ', end='')
    
    print(show_player(square_owner('bottom_left')), end='')

    if check_line('South_Center'):
        print('  |', end='')
    else:
        print('   ', end='')
    
    print(show_player(square_owner('bottom_right')), end='')

    if check_line('East_Southeast'):
        print('  |')
    else:
        print('   ')

    # 6---7---8   ----------------------------------

    print('   6', end='')
    if check_line('South_Southwest'):
        print('---', end='')
    
    else:
        print('   ', end='')

    print('7', end='')
    if check_line('South_Southeast'):
        print('---', end='')
    
    else:
        print('   ', end='')

    print('8')

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
    if move == '01' or move == '10':
        return 'North_Northwest'

    elif move == '21' or move == '12':
        return 'North_Northeast'

    elif move == '03' or move == '30':
        return 'West_Northwest'

    elif move == '14' or move == '41':
        return 'North_Center'

    elif move == '25' or move == '52':
        return 'East_Northeast'

    elif move == '34' or move == '43':
        return 'West_Center'

    elif move == '45' or move == '54':
        return 'East_Center'

    elif move == '36' or move == '63':
        return 'West_Southwest'

    elif move == '47' or move == '74':
        return 'South_Center'

    elif move == '58' or move == '85':
        return 'East_Southeast'

    elif move == '67' or move == '76':
        return 'South_Southwest'

    elif move == '78' or move == '87':
        return 'South_Southeast'

    else:
        return 'No line' # Default 

# TODO: Fix declaration of winner
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