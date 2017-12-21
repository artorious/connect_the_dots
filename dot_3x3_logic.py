#!/usr/bin/env python3
"""Game Engine 

Provides the logic for a simplified connect the dots game.
The code in this module determines and enforces the rules of the game.
Callers are responsible for the game's presentation component,
or user experience (UX)

The playing surface consits of 3x3 grid of dots:

        @   @   @

        @   @   @

        @   @   @

The game allows two players, X and Y, to alternately add horizontal and
vertical lines to connect the dots. The following shows a game in progress:

        @---@   @
            |	|
        @   @   @
                |
        @   @---@

When a player completes a square, that player wins the square and retains 
control of the next turn. The following shows a game in which player Y has
completed a square:

        @---@   @
            |	|
        @   @---@
            | Y |
        @   @---@

If a player connects two dots and does not complete a square, control passes
to the other player. A player must add a line during his/her turn. The game 
ends when all dots ahve been connected. The player with more squares wins the
game, and the game is a draw if both players have two squares each.

This game engine manages 12 lines. Each line distinguished by its name 
(a string) as shown here:

        @---'North_Northwest'---@---'North_Northeast'---@
        |                       |                       |
        |                       |                       |
        |                       |                       |
'West_Northwest'            'North_Center'      'East_Northeast'
        |                       |                       |
        |                       |                       |
        |                       |                       |
        @---'West_Center'-------@-----'Center_East'-----@
        |                       |                       |
        |                       |                       |
        |                       |                       |
'West_Southwest'         'Center_South'         'East_Southeast'
        |                       |                       |
        |                       |                       |
        |                       |                       |
        @---'South_Southwest'---@---'South_Southeast'---@

The game engine manages four squares. Each square is distinguished by it's
name (a string) as shown here:

        @---------------@---------------@
        |               |               |
        |               |               |
        |   'top_left'  |  'top_right'  |
        |               |               |
        @---------------@---------------@
        |               |               |
        |               |               |
        | 'bottom_left' |'bottom_right' |
        |               |               |
        |               |               |
        @---------------@---------------@

The string 'X' represents player X, and the string 'Y' represents playey Y. 

"""
# NOTE:
# ----------------------------------------------------------------------------
# Global vars (private) - maintain the state of the game. prefix vars with
#       underscores to dicourage access outside this module.
# ----------------------------------------------------------------------------
# Boolean vars that keep track of whether or not a line exists between two 
#       dots. E.g. If _n_nw is True, the line identifeid as 'North_Northwest'
#       exists.
# ----------------------------------------------------------------------------
#       @----_n_nw---@---_n_ne---@
#       |            |           |        
#     _w_nw         _n_c       _e_ne
#       |            |           |
#       @----_w_c----@----_e_c---@
#       |            |           |
#     _w_sw         _s_c       _e_se
#       |            |           |
#       @---_s_sw----@---_s_se___@


# Init Line status (exists) - Initally, no lines exist anywhere (False)
_n_nw, _n_ne, _n_c = False, False, False
_w_nw, _w_sw, _w_c = False, False, False
_e_ne, _e_se, _e_c = False, False, False
_s_sw, _s_se, _s_c = False, False, False

# Init Current player - A string, 'X' for player X or 'Y' for player Y
_current_player = 'X'

# Init square ownership as None
# A string reps ownership, 'X' for player X or 'Y' for player Y

_top_left_owner, _top_right_owner = None, None
_bottom_left_owner, _bottom_right_owner = None, None

##############################################################################
# Note: Private Functions (prefixed with underscore)
# Functions accessed only within this module
#-----------------------------------------------------------------------------

def _update_square(sq):	
    """(str) -> bool
    Updates the owner of square <sq>, if possible.
    <sq> must one of the strings; 'top_left', 'top_right', 'bottom_left',
    or 'bottom_right'. 
    Function Checks to see:
        1. If the square currently is not owned by a player and
        2. if all the lines are in place to complete the sqaure.
    
    If both conditions are met, it marks the square with the current player
    and returns True. 
    If one of the players already owns the square, or if not all lines exist 
    to complete the square, returns False. 		
    """
    # Declare global vars affected by function
    global _top_left_owner, _top_right_owner, _bottom_left_owner, \
            _bottom_right_owner
    
    if sq == 'top_left' and _top_left_owner == None and _n_nw and _n_c and \
            _w_c and _w_nw: 
        _top_left_owner = _current_player 
        return True
    
    elif sq == 'top_right' and _top_right_owner == None and _n_ne and _e_ne \
            and _e_c and _n_c:
        _top_right_owner = _current_player
        return True

    elif sq == 'bottom_left' and _bottom_left_owner == None and _w_c and _s_c \
            and _s_sw and _w_sw:
        _bottom_left_owner = _current_player
        return True

    elif sq == 'bottom_right' and _bottom_right_owner == None and _e_c and \
            _e_se and _s_se and _s_c:
        _bottom_right_owner = _current_player
        return True

    else:
        return False # Ownership unchanged

def _update_squares():
    """() ->  bool
    Attepts to update the owners of all the squares that a new line might 
    affect. 
    
    Returns True if one or more squares receives a new owner, otherwise False
    """
    top_left = _update_square('top_left')
    top_right = _update_square('top_right')
    bottom_left = _update_square('bottom_left')
    bottom_right = _update_square('bottom_right')
    
    return top_left or top_right or bottom_left or bottom_right

##############################################################################

##############################################################################
# NOTE: Functions that reveal or control the state of the current game.
# These functions are meant to be accessed outside of this module
#-----------------------------------------------------------------------------

def add_line(line):
    """(str) -> turtle, bool
    Attempts to add a line between two dots. 
    The parameter <line> must be one of 'North_Northeast', 'North_Northwest',
    'East_Center', etc, (A string represnting a line on the game board)
    
    If the line is not present, adds the line and returns True.
    If the line is already present, no change to state of game board and
    returns False
    """
    # Declare global vars the func may affect maintaining the game-state
    global _n_nw, _n_c, _n_ne, _s_c, _s_se, _s_sw, _e_c, _e_se, _e_ne, \
            _w_c, _w_sw, _w_nw, _current_player
    
    line_added = False  # Init unsuccessful by defaulr
    
    if line == 'North_Northwest' and not _n_nw:
        _n_nw = True
        line_added = True
    
    elif line == 'North_Center' and not _n_c:
        _n_c = True
        line_added = True

    elif line == 'North_Northeast' and not _n_ne:
        _n_ne = True
        line_added = True

    elif line == 'South_Center' and not _s_c:
        _s_c = True
        line_added = True

    elif line == 'South_Southeast' and not _s_se:
        _s_se = True
        line_added = True

    elif line == 'South_Southwest' and not _s_sw:
        _s_sw = True
        line_added = True

    elif line == 'East_Center' and not _e_c:
        _e_c = True
        line_added = True

    elif line == 'East_Southeast' and not _e_se:
        _e_se = True
        line_added = True

    elif line == 'East_Northeast' and not _e_ne:
        _e_ne = True
        line_added == True

    elif line == 'West_Northwest' and not _w_nw:
        _w_nw = True
        line_added = True

    elif line == 'West_Southwest' and not _w_sw:
        _w_sw = True
        line_added = True

    elif line == 'West_Center' and not _w_c:
        _w_c = True
        line_added = True
    
    # If line added succesfully, check whether it completes square
    if line_added and not _update_squares():
        # Turn move to next player upoun a successful move
        if _current_player == 'X':
            _current_player = 'Y'
        else:
            _current_player = 'X'
    
    return line_added

def square_owner(sq):
    """ (str) -> turtle, NoneType
    Checks who owns the given square <sq>
    <sq> must be one of the strings, 'top_left', 'top_right', 'bottom_right'
    or 'bottom_left'
    
    Returns the player who owns the given square, and None if no-one owns it
    """
    if sq == 'top_left':
        return _top_left_owner
    
    elif sq == 'top_right':
        return _top_right_owner
    
    elif sq == 'bottom_left':
        return _bottom_left_owner
    
    elif sq == 'bottom_right':
        return _bottom_right_owner

    else:
        return None

def check_line(line):
    """(str) -> bool
    Checks whether the line <line> exists. 
    The parameter <line> must be one of 'North_Northeast', 'North_Northwest',
    'East_Center', etc, (A string represnting a line on the game board)

    Returns True if the line exists on the game board, otherwise False if it
    doesn't exist yet
    """
    if line == 'North_Northwest':
        return _n_nw 
    
    elif line == 'North_Center':
        return _n_c

    elif line == 'North_Northeast':
        return _n_ne 

    elif line == 'South_Center':
        return _s_c 

    elif line == 'South_Southeast':
        return _s_se

    elif line == 'South_Southwest':
        return _s_sw

    elif line == 'East_Center':
        return _e_c

    elif line == 'East_Southeast':
        return _e_se

    elif line == 'East_Northeast':
        return _e_ne 

    elif line == 'West_Northwest':
        return _w_nw 

    elif line == 'West_Southwest':
        return _w_sw 

    elif line == 'West_Center':
        return _w_c

    else:
        return False

def winner():
    """() -> str, NoneType
    Declares the game's winner, player X, player Y or a draw
    
    Returns 'X' or 'Y', or 'Draw' if the game board is full and  both players
    each own two squares.
    Reurns None if open squares still exist, and so the game can continue
    """
    # Init counter var for the players' squares
    x_count, y_count = 0, 0

    if _top_left_owner == 'X':
        x_count += 1
    
    elif _top_left_owner == 'Y':
        y_count += 1
    
    elif _top_right_owner == 'X':
        x_count += 1

    elif _top_right_owner == 'Y':
        y_count += 1

    elif _bottom_left_owner == 'X':
        x_count += 1
    
    elif _bottom_left_owner == 'Y':
        y_count += 1
    
    elif _bottom_right_owner == 'X':
        y_count += 1
    
    elif _bottom_right_owner == 'Y':
        y_count += 1

    if x_count + y_count == 4: # All squares filled
        if x_count > y_count:
            return 'X'  # Player X won
        
        elif x_count < y_count:
            return 'Y'  # Player Y won

        else:
            return 'Draw' # Tied game

    else:
        return None     # No Winner or draw; game continues

    

def initialize_board():
    """
    Makes the playing board ready for a new game.
        1. Clears all the lines from the board,
        2. makes all the squares empty, and
        3. sets the current player to X
    Does not return a value to the caller
    """
    # Declare global vars the func may affect maintaining the game-state
    global _n_nw, _n_c, _n_ne, _s_c, _s_se, _s_sw, _e_c, _e_se, _e_ne, _w_c, \
            _w_sw, _w_nw, _current_player, _top_left_owner, _top_right_owner, \
            _bottom_left_owner, _bottom_right_owner

    # Init (line exists) to default state (False)
    _n_nw = _n_c = _n_ne = _s_c = _s_se = _s_sw = _e_c = _e_se = _e_ne = \
            _w_c = _w_sw = _w_nw = False

    # Init/Clear all the squares to default state
    _top_left_owner = _top_right_owner = _bottom_left_owner = \
        _bottom_right_owner = None
    
    # Init current player - X always starts
    _current_player = 'X'

def current_player():
    """() -> str
    Returns the player whose turn it is to move
    """
    return _current_player