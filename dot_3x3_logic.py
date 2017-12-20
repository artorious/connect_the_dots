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
'Northwest_West'            'North_Center'      'Northeast_East'
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

