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
    begin_fill()
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
    color('blue')
    pensize(10)
    draw_line(x_pos - 40, y_pos - 40, x_pos + 40, y_pos + 40)
    draw_line(x_pos - 40, y_pos + 40, x_pos + 40, y_pos - 40)

def draw_Y(x_pos, y_pos):
    """(int, int) -> turlte
    Draws player Y's mark at position (x_pos, y_pos)
    """
    color('blue')
    pensize(10)
    draw_line(x_pos - 40, y_pos + 40, x_pos, y_pos)
    draw_line(x_pos + 40, y_pos + 40, x_pos, y_pos)
    draw_line(x_pos, y_pos, x_pos, y_pos - 40)

def draw_square(sq, owner):
    """(tuple, str) -> turtle 
    Draws the owner of the square, if the square has an owner
    """
    # Coordinates the square
    x_pos, y_pos = square_to_point(sq)
    
    if owner == 'X':
        draw_X(x_pos, y_pos)
    
    elif owner == 'Y':
        draw_Y(x_pos, y_pos)
    # Else do not draw anything - the square ha no owner

def check_squares():
    """(None) -> str
    Checks all squares to determine if any are complete.
    Draws the square owner's mark in a completed square.
    If all squares are owned, the function declares a winner or announces 
    a draw. 
    """
    draw_square('top_left', square_owner('top_left'))
    draw_square('top_right', square_owner('top_right'))
    draw_square('bottom_left', square_owner('bottom_left'))
    draw_square('bottom_right', square_owner('bottom_right'))

    # Check the ownership of each potential square
    win = winner()

    if win == 'X':
        messagebox.showinfo('Game Over', 'X wins')
    
    elif win == 'Y':
        messagebox.showinfo('Game Over', 'Y wins')
    
    elif win == 'Draw':
        messagebox.showinfo('Game Over', 'Tied Game')
        

def mouse_click(x_pos, y_pos):
    """(int, int) -> turtle or messagebox
    Responds to the user clicking the mouse when the cursor is over the
    window. Determines if the user clicked on a dot. 
    Activates an initial dot if the initial dot is not already active. 
    Establishes a line to the terminal dot if possible.
    If the move is illegal, the function produces a message box alerting 
    the player
    """
    global initial_dot

    print('Initial dot = {0}'.format(initial_dot))

    print('Clicked at x = {0} and y = {1}'.format(x_pos, y_pos))
    dot = hit(x_pos, y_pos) # Did the player click on a dot?
    
    if dot:
        print(dot)

        if not initial_dot:
            initial_dot = dot
            draw_dot(initial_dot, 'red')
        
        elif dot != initial_dot:
            
            if add_line(line_name(initial_dot, dot)):
                # Draw the added line
                color('black')
                pensize(5)
                x_pos1, y_pos1 = dot_to_point(initial_dot)
                x_pos2, y_pos2 = dot_to_point(dot)

                draw_line(x_pos1, y_pos1, x_pos2, y_pos2)

                # Adjust title bar to show current player
                title('3x3 Connect the dots - Current player: {0}'.format(current_player()))
                
                # Check to see if the move captured a square and/or ended the game
                check_squares()
            
            # Clear the initial dot and redraw both connecting dots
            draw_dot(initial_dot)
            initial_dot = None # Initial dot no longer in play
            draw_dot(dot)

    else:
        if initial_dot:
            draw_dot(initial_dot)
            initial_dot = None     

def reset_game():
    """
    Reinitialize the game's state for the start of a new game
    """
    clearscreen()
    initialize()

def line_name(dot1, dot2):
    """(str, str) -> str, messagebox
    Returns the name of the line that connects the dot objects <dot1> and 
    <dot2>. Derives the line's name from the names of the dot objects.
    Displays an error message box if the two dots do not participate in a 
    valid line. 
    """
    if (dot1 == 'Northwest' and dot2 == 'North') or \
            (dot1 == 'North' and dot2 == 'Northwest'):
        return 'North_Northwest'

    elif (dot1 == 'Northeast' and dot2 == 'North') or \
            (dot1 == 'North' and dot2 == 'Northeast'):
        return 'North_Northeast'

    elif (dot1 == 'Northwest' and dot2 == 'West') or \
            (dot1 == 'West' and dot2 == 'Northwest'):
        return 'West_Northwest'

    elif (dot1 == 'North' and dot2 == 'Center') or \
            (dot1 == 'Center' and dot2 == 'North'):
        return 'North_Center'

    elif (dot1 == 'Northeast' and dot2 == 'East') or \
            (dot1 == 'East' and dot2 == 'Northeast'):
        return 'East_Northeast'

    elif (dot1 == 'West' and dot2 == 'Center') or \
            (dot1 == 'Center' and dot2 == 'West'):
        return 'West_Center'

    elif (dot1 == 'East' and dot2 == 'Center') or \
            (dot1 == 'Center' and dot2 == 'East'):
        return 'East_Center'

    elif (dot1 == 'West' and dot2 == 'Southwest') or \
            (dot1 == 'Southwest' and dot2 == 'West'):
        return 'West_Southwest'

    elif (dot1 == 'South' and dot2 == 'Center') or \
            (dot1 == 'Center' and dot2 == 'South'):
        return 'South_Center'
   
    elif (dot1 == 'East' and dot2 == 'Southeast') or \
            (dot1 == 'Southeast' and dot2 == 'East'):
        return 'East_Southeast'

    elif (dot1 == 'South' and dot2 == 'Southwest') or \
            (dot1 == 'Southwest' and dot2 == 'South'):
        return 'South_Southwest'

    elif (dot1 == 'South' and dot2 == 'Southeast') or \
            (dot1 == 'Southeast' and dot2 == 'South'):
        return 'South_Southeast'

    else:
        print('Not a VALID dot link')
        messagebox.showerror('Invalid Link', 'Can\'t connect those two dots')
        return None

def initialize():
    """(None) -> turtle
    Initializes the graphical presentation and game engine
    """
    # Global dot objects

    # Init game engine
    initialize_board()

    screensize(600, 600) # Specify the dimensions of the window
    setworldcoordinates(0, 0, 599, 599) # Move origin (0, 0) to the left bottom of the window

    # Apply tricks to speed up the image rendering
    tracer(0)
    hideturtle()

    # Register callback functions with the Turtle graphics framework
    onscreenclick(mouse_click) # On mouse-click
    onkeyrelease(reset_game, 'q') # On pressing <key> Q

    listen()    # Permit window to listen to keypress events
    
    # Set initial window title
    title('3x3 Connect the dots - Current player: {0}'.format(current_player()))

    initial_dot = None # No initial dot has been selected

    # Draw all the dots
    for dot in ('North', 'Northeast', 'Northwest',\
                'South', 'Southeast', 'Southwest',\
                'Center', 'East', 'West'):
        draw_dot(dot)

    update() # Compel window to show drawing

if __name__ == '__main__':
    initialize()    # Set up the game
    mainloop()      # Start game running
