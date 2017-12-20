#!/usr/bin/env python3
"""dot_3x3_logic.py
Game Engine

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
            |   |
        @   @   @
                |
        @   @---@

When a player completes a square, that player wins the square and retains 
control of the next turn. The following shows a game in which player Y has
completed a square:

        @---@   @
            |   |
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

# Current player - A string, 'X' for player X or 'Y' for player Y
_current_player = 'X'

# Initsquare ownership as None
# A string reps ownership, 'X' for player X or 'Y' for player Y

_top_left_owner, _top_right_owner = None, None
_bottom_left_owner, _bottom_right_owner = None, None


