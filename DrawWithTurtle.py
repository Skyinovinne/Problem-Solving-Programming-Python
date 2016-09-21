##PROBLEM: Draw a picture using turtle graphics using command inputs from a file
##
##ALGORITHM:
##      1. Ask user to input a filename or “quit”.
##      2. If the user types “quit”, exit the program.
##      3. If the file doesn’t exist, tell the user and ask for another filename.
##      4. Open the file, if you can’t, warn the user and ask for another filename.
##      5. Display a turtle window.
##      6. Clear the turtle window, reset the line and fill color to black, and put
##          the turtle at the origin.
##      7. Read the next line from the file
##      8. If line contains “#”, ignore everything after it including #
##      9. Trim the line of spaces and make it lowercase.
##      10. Split the line by spaces to form words.
##      11. If there are no words, continue to the next line.
##      12. Note: The following steps are to be implemented using a dictionary of
##          words to functions.
##      13. If the first word of the line is “color”, then set the line and fill color
##          to the second word
##      14. If the first word of the line is “rect”, then draw a rectangle with x, y,
##          width, and height. x is the second word, y is the third word, width is the
##          fourth word, and height is the fifth word. The x and y coordinates are for
##          the top left corner, and are relative to the origin. Fill and outline the
##          rectangle with the current color with the specified size.
##      15. If the first word of the line is “circle”, then draw a circle with x, y, and radius. x is the second word, y is the third word, radius is the fourth word. The x and y coordinates are for the center of the circle, and are relative to the turtle. Fill and outline a circle of the specified radius with the current color. Don’t move the turtle.
##      16. If the first word of the line is “line”, then draw a line with x, y, angle, and
##          length. x is the second word, y is the third word, angle is the fourth word, and
##          length is the fifth word. The x and y coordinates are for the starting point. The
##          angle is in degrees and is typical for a Cartesian coordinate system. The length
##          is how long the line is.
##      17. If the first word of the line is not defined in the program then it is an invalid
##          word; warn the user and display the current line in the python shell, and continue
##          to the next line.
##      18. If during the process of any of these commands, there are not enough arguments or
##          cannot convert an argument to an integer if needed, then warn user and display the
##          current line. Continue to the next line.
##      19. Repeat the above steps (not including clearing the window) until there are no more
##          lines.
##      20. Loop back to step 2. 
##
##ERROR HANDLING: Filename inputs and any parsing errors
import turtle
import os.path

# Sets the line and fill color to the specified color
#
# Parameters:
#       clr : string - The color to set
def color(clr):
    turtle.color(clr)

# Draws a rectangle of given width and height at the specified x, y position
#
# The string parameters are parsed as floats
#
# Parameters:
#       x : string - X position of the top left corner
#       y : string - Y position of the top left corner
#       width : string - The width of the rectangle
#       height : string - The height of the rectangle
# Throws:
#       ValueError : if a string argument could not be parsed as a float
def rect(x, y, width, height):
    turtle.penup()
    turtle.goto(float(x), float(y))
    turtle.pendown()
    
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(float(width))
        turtle.right(90)
        turtle.forward(float(height))
        turtle.right(90)
    turtle.end_fill()

# Draws a circle at the specified point x, y with the given radius
#
# The string parameters are parsed as floats
#
# Parameters:
#       x : string - X position of the center of the circle
#       y : string - Y position of the center of the circle
#       radius : string - Radius of the circle to be drawn
# Throws:
#       ValueError : if a string argument could not be parsed as a float
def circle(x, y, radius):
    turtle.penup()
    turtle.goto(float(x), float(y) - float(radius))
    turtle.pendown()
    
    turtle.begin_fill()
    turtle.circle(float(radius))
    turtle.end_fill()

# Draws a line at the specified point x, y with the given angle and length
#
# The string parameters are parsed as floats
#
# Parameters:
#       x : string - X position of the start of the line
#       y : string - Y position of the start of the line
#       angle : string - Angle of the line in degrees
#       length : string - The length of the line
# Throws:
#       ValueError : if a string argument could not be parsed as a float
def line(x, y, angle, length):
    turtle.penup()
    turtle.goto(float(x), float(y))
    turtle.pendown()
    
    turtle.setheading(float(angle))
    turtle.forward(float(length))
    turtle.setheading(0)
    
COMMANDS = {"color" : color, "rect" : rect, "circle" : circle, "line" : line}

# Asks the user to input a filename, or quit
#
# Returns an open file or None if the user wants to quit.
# The caller is responsible for closing the file.
def getFileFromUser():
    while True:
        try:
            filename = input("Enter File to open and draw (or quit) ==> ")

            if filename.lower() == "quit":
                return None
            
            if not os.path.exists(filename):
                print("File does not exist:", filename)
                continue
            
            return open(filename)
        except IOError:
            print("Could not open file:", filename)
    
while True:
    file = getFileFromUser()
    if file is None:
        break;

    turtle.showturtle()
    turtle.reset()

    # Draw as fast as possible
    turtle.speed("fastest")
    turtle.hideturtle()
    turtle.delay(0)
    
    for line in file:
        try:
            # Handle comments in the line
            if "#" in line:
                line = line[:line.find("#")]
            
            # Parse the command
            words = line.strip().lower().split()

            # Ignore empty lines
            if len(words) == 0:
                continue

            # Execute the command handler from a dictionary
            COMMANDS[words[0]](*words[1:])
            
        except TypeError:
            print("This line did not have proper number of arguments\n", line)
        except ValueError:
            print("Could not convert an argument to float\n", line)
        except KeyError:
            print("Bad command given could not interpret\n", line)
        except turtle.TurtleGraphicsError:
            print("A graphics error occurred processing this line\n", line)

    file.close()
    turtle.done()
