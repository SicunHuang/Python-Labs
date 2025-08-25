"""
Drawing different shaps with recursive functions

CSCI 150 Lab 9 Fractals

Name: Sicun Huang
Section: A

Creativity:

"""

import turtle as t

def gcd(a, b):
    """
    Compute the greatest common divisor of two positive integers
    
    Args:
        a: Positive integer
        b: Positive integer
    
    Return:
        GCD of a and b
    """
    rem = a % b
    if rem == 0:
        return b
    else:
        return gcd(b,rem)

# Sample calls for testing
# gcd(36, 81)
# gcd(13, 6)

        
def stairs(length, levels):
    """
    Draw "stairs" of decreasing length corresponding to each levels
    
    Args:
        length: Integer length of stairs
        levels: Integer number of stairs
    """
    if levels > 0:
        t.forward(length)
        t.right(90)
        t.forward(length)
        t.left(90)
        stairs(length/2, levels-1)
        t.backward(length)
        t.right(90)
        t.backward(length)
        t.left(90)

# Sample calls for testing
# stairs_demo(300, 1)
# stairs_demo()


def sierpinski(length, iterations):
    """
    Draw sierpinski triangle with length equals to length and generations equal to iterations
    
    Args:
        length: Length of the base of the triangles
        iterations: Generations of triangles
    """
    if iterations > 0:
        for i in range(3):
            t.forward(length)
            t.left(120)
        sierpinski(length/2, iterations-1)
        t.forward(length/2)
        sierpinski(length/2, iterations-1)
        t.backward(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        sierpinski(length/2, iterations-1)
        t.left(60)
        t.backward(length/2)
        t.right(60)
        
# Sample calls for testing
# sierpinski_demo(300, 1)
# sierpinski_demo()


def recursive_h(length, level):
    """
    Drawing recursive H with vertical length of length and horizontal length of 2 length with different levels
    
    Args:
        length: Length of the recursive H
        level: Number of levels of the revursive H
    """
    if level == 0:
        t.dot()
    else:
        t.forward(length)
        t.right(90)
        t.forward(length/2)
        t.left(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.forward(length)
        t.right(90)
        recursive_h(length/2, level-1)
        t.right(90)
        t.forward(length/2)
        t.right(90)
        t.forward(length*2)
        t.right(90)
        t.forward(length/2)
        t.right(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.backward(length)
        t.right(90)
        recursive_h(length/2, level-1)
        t.left(90)
        t.forward(length/2)
        t.right(90)
        t.forward(length)
        
# Sample calls for testing
# recursive_h_demo(200, 1)
# recursive_h_demo()

# When all is complete, create screenshot using
# drawing_demo()


# Testing code is provided below that calls the recursive functions above
        
def stairs_demo(length=256, levels=5):
    """
    Set up for stairs drawing and call stairs().

    First moves the turtle to the top left of the screen, then calls stairs()  
    to draw a staircase of squares. Calls turtle.done() at the end of drawing.
    
    Args:
        length: side length of top square in pixels 
        levels: number of boxes to draw 
    """
    # pick up the pen and move the turtle so it starts at the left edge of the canvas 
    t.penup()
    t.goto(-t.window_width()/2 + 20, t.window_height()/2 - 20)
    t.pendown()    

    # draw the stairs by calling recursive function
    stairs(length, levels)

    # finished
    t.done()


def sierpinski_demo(length=300, iterations=5):
    """
    Set up for sierpinski drawing and call sierpinski().
    
    First moves the turtle to the left edge of the drawing window, turns off
    tracer, and then calls sierpinski(). Calls turtle.done() at end of drawing.
    
    Args:
        length: base length of Sierpinski triangle in pixels 
        iterations: complexity level of Sierpinski triangle 
    """
    if iterations > 3:
        # turn off animation (too slow for high iterations)
        t.tracer(False)
    
    # pick up the pen and move the turtle so it starts at the left edge of the canvas
    t.penup()
    t.goto(-t.window_width()/3 + 20,0)
    t.pendown()
    
    sierpinski(length, iterations)
    
    # finish
    t.update()   # need t.update() if using t.tracer(False)
    t.done()     
    

def recursive_h_demo(length=150, level=3):
    """
    Set up for recursive_h drawing and call recursive_h().
    
    Turns tracer off, calls recursive_h(), and ends with turtle.done().
    
    Args:
        length: height of innermost H in pixels
        level: complexity level of recursive H
    """
    if level > 2:
        # turn off animation (too slow for high iterations)
        t.tracer(False)
    
    recursive_h(length, level)
    
    t.update()    # need t.update() if using t.tracer(False)
    t.done()
    

def drawing_demo():
    """
    Create drawings of `stairs`, `sierpinski`, and `recursive_h`.
    
    Args:
        None
    """
    t.tracer(False)
    
    # draw stairs in upper left of drawing window
    t.penup()
    t.goto(-t.window_width()/2 + 20, t.window_height()/2 - 20)
    t.pendown()    
    stairs(150, 6)
       
    # draw sierpinski in upper right of drawing window
    t.penup()
    t.goto(0, t.window_height()/2 - 300)
    # t.goto(0,40)
    t.pendown()    
    sierpinski(300, 5)
    
    # draw recursive H in lower half of drawing window
    t.penup()
    t.goto(0, -t.window_height()/4)
    t.pendown()    
    recursive_h(150, 4)
    
    # finish
    t.update() 
    t.done()     
