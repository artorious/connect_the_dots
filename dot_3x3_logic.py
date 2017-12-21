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
#     _w_sw         _s_c       _s_se
#       |            |           |
#       @---_s_sw----@---_s_se___@


# Init Line status - Initally, no lines exist anywhere (False)
_n_nw, _n_ne = False, False
_w_nw, _n_c, _e_ne = False, False, False
_w_c, _e_c = False, False
_w_sw, _s_c, _s_se = False, False, False
_s_sw, _s_se = False, False

# Init Current player - A string, 'X' for player X or 'Y' for player Y
_current_player = 'X'

# Init square ownership as None
#TODO: A string reps ownership, 'X' for player X or 'Y' for player Y

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
            _s_se and _s_se and _s_c:
        _bottom_right_owner = _current_player
        return True

    else:
        return False # Ownership unchanged

def _update_squares():
    """() -> turtle, bool
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
    return

def square_owner(sq):
    """ (str) -> turtle, NoneType
    Checks who owns the given square <sq>
    <sq> must be one of the strings, 'top_left', 'top_right', 'bottom_right'
    or 'bottom_left'
    
    Returns the player who owns the given square, and None if noone owns it
    """
    return

def check_line(line):
    """(str) -> bool
    Checks whether the line <line> exists. 
    The parameter <line> must be one of 'North_Northeast', 'North_Northwest',
    'East_Center', etc, (A string represnting a line on the game board)

    Returns True if the line exists on the game board, otherwise False if it
    doesn't exist yet
    """
    return

def winner():
    """() -> str, NoneType
    Declares the game's winner, player X, player Y or a draw
    
    Returns 'X' or 'Y', or 'Draw' if the game board is full and  both players
    each own two squares.
    Reurns None if open squares still exist, and so the game can continue
    """
    return

def initialize_board():
    """
    Makes the playing board ready for a new game.
        1. Clears all the lines from the board,
        2. makes all the squares empty, and
        3. sets the current player to X
    Does not return a value to the caller
    """
    return

def current_player():
    """() -> str
    Returns the player whose turn it is to move
    """
    return