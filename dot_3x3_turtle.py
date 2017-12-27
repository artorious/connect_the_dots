#!/usr/bin/env python3
"""Graphical Presentation for game board using Python's turtle"""

from turtle import *
from tkinter import messagebox
from dot_3x3_logic import *     # Game engine functions

# Init global vars supporting graphical interace
initial_dot = None  # First dot selected by a player when creating a line
dot_radius = 10     # Adjustable for larger/smaller dots

def square_to_point(sq):
    """(str) -> tuple
    Compute the (x, y) coordinates of the center of a square.
    Used to properly place the square's owner when it's captured.
    """
    if sq == 'top_left':
        return (200, 400)
    
    elif sq == 'top_right':
        return (400, 400)
    
    elif sq == 'bottom_left':
        return (200, 200)
    
    elif sq == 'bottom_right':
        return (400, 200)

def hit(x_pos, y_pos):
    """(int, int) -> str or None
    Returns the dot (if any) that the point (x_pos, y_pos) is within.
    Returns None if the point (x_pos, y_pos) does not overlap any dot.
    Used when a player clicks the mouse over the board to determine which dot
    (if any) was selected.
    """
    dot = None  # Default result

    if 90 < x_pos < 110 and 490 < y_pos < 510:
        dot = 'Northwest'
        
    elif 290 < x_pos < 310 and 490 < y_pos < 510:
        dot = 'North'
    
    elif 490 < x_pos < 510 and 490 < y_pos < 510:
        dot = 'Northeast'

    elif 90 < x_pos < 110 and 290 < y_pos < 310:
        dot = 'West'
    
    elif 290 < x_pos < 310 and 290 < y_pos < 310:
        dot = 'Center'

    elif 490 < x_pos < 510 and 290 < y_pos < 310:
        dot = 'East'

    elif 90 < x_pos < 110 and 90 < y_pos < 110:
        dot = 'Southwest'

    elif 290 < x_pos < 310 and 90 < y_pos < 110 :
        dot = 'South'
    
    elif 490 < x_pos < 510 and 90 < y_pos < 110:
        dot = 'Southeast'

    return dot

def dot_to_point(dot):
    """ (str) -> tuple
    Maps a <dot> to it's location on the board. used to render a dot in it's 
    proper place. 
    """
    if dot == 'Northwest':
        return 100, 500
    
    elif dot == 'North':
        return 300, 500
    
    elif dot == 'Northeast':
        return 500, 500

    elif dot == 'West':
        return 100, 300

    elif dot == 'Center':
        return 300, 300

    elif dot == 'East':
        return 500, 300

    elif dot == 'Southwest':
        return 100, 100

    elif dot == 'South':
        return 300, 100

    elif dot == 'Southeast':
        return 500, 100

def draw_dot(name, dot_color='black'):
    """(tuple) -> turtle
    Draws a graphical dot <name> within the graphical window.
    <col> specifies the dots's color (black by default)
    """
    global dot_radius

    pensize(1)
    penup()
    x_pos, y_pos = dot_to_point(name)
    setposition(x_pos, y_pos - dot_radius)
    pendown()
    color(dot_color)
    beginfill()
    circle(dot_radius)
    end_fill()
    update()

def draw_line(x_pos1, y_pos1, x_pos2, y_pos2):
    """(int, int, int, int) -> turtle
    Draws a line segment with endpints (x_pos1, y_pos1) and (x_pos2, y_pos2)
    """
    penup()
    setposition(x_pos1, y_pos1)
    pendown()
    setposition(x_pos2, y_pos2)
    update()

def draw_X(x_pos, y_pos):
    """(int, int) -> turtle
    Draws player X's mark at position (x_pos, y_pos)
    """

    pass

def draw_Y(x_pos, y_pos):
    """(int, int) -> turlte
    Draws player Y's mark at position (x_pos, y_pos)
    """
    pass

def drwaw_squares(sq, owner):
    """(tuple, str) -> turtle 
    Draws the owner of the square, if the square has an owner
    """
    pass

def check_squares():
    """(None) -> str
    Checks all squares to determine if any are complete.
    Draws the square owner's mark in a completed square.
    If all squares are owned, the function declares a winner or announces 
    a draw. 
    """
    pass

def mouse_click(x_pos, y_pos):
    """(int, int) -> turtle, messagebox
    Responds to the user clicking the mouse when the cursor is over the
    window. Determines if the user clicked on a dot. 
    Activates an initial dot if the initial dot is not already active. 
    Establishes a line to the terminal dot if possible.
    If the move is illegal, the function produces a message box alerting 
    the player
    """
    pass

def reset_game():
    """
    Reinitialize the game's state for the start of a new game
    """
    pass

def line_name(dot1, dot2):
    """(str, str) -> str, messagebox
    Returns the name of the line that connects the dot objects <dot1> and 
    <dot2>. Derives the line's name from the names of the dot objects.
    Displays an error message box if the two dots do not participate in a 
    valid line. 
    """
    return

def initialize():
    """(None) -> turtle
    Initializes the graphical presentation and game engine
    """


if __name__ == '__main__':
    initialize()    # Set up the game
    mainloop()      # Start game running
