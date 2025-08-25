"""
CSCI 150 Lab 2

Name: Sicun Huang
Section A

creativity:
1. create an add_stars function that draws multiple stars using a for loop
2. create a flowers function that draws flowers in the lower part of the screen
3. fish and flowers functions can give the objects random colors 
"""

import turtle as t
import random as r

LAKE_BLUE = "#add8e6"
NIGHT_BLUE = "#1b1e23"
MOON_GLOW = "#F4F1C9"
STAR_YELLOW = "#ffcd3c"
BOULDER_BROWN = "#6A483B"
    
def jumpto(x, y, heading):
    """move the cursor without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(heading)
    
def lake():
    """draw a lake with light blue"""
    jumpto(-350, 75, 0)
    t.fillcolor(LAKE_BLUE)#hex color of light blue
    t.begin_fill()
    for i in range(2):
        t.forward(700)
        t.right(90)
        t.forward(425)
        t.right(90)
    t.end_fill()
    
def night_sky():
    """draw the sky with black"""
    jumpto(-350, 75, 0)
    t.fillcolor(NIGHT_BLUE)#hex color of dark cyan-blue
    t.begin_fill()
    for i in range(2):
        t.forward(700)
        t.left(90)
        t.forward(275)
        t.left(90)
    t.end_fill()

def moon():
    """draw a moon at the upper-right corner"""
    t.fillcolor(MOON_GLOW) #hex color for moon glow
    t.begin_fill()
    jumpto(200, 350, -90)
    t.circle(175)
    t.end_fill()

def add_stars(numstars):
    """draws stars randomly throughout the screen"""
    t.pencolor(STAR_YELLOW) #hex code for star yellow
    for i in range(numstars):
        x = r.randint(-300,200)
        y = r.randint(100,350)
        jumpto(x, y, 0)
        for j in range (5):
            t.forward(10)
            t.right(144)
            
def boulders(numboulders):
    """draw numboulders boulders with random sidelength and number of sides randomly throughout the screen"""
    for i in range(numboulders):
        x = r.randint(-350,350)
        y = r.randint(-300,-250)
        jumpto(x, y, 0)
        sidelen = r.randint(100,150)
        numsides = r.randint (5,10)
        angle = 360 / numsides
        t.fillcolor(BOULDER_BROWN) #hex code for boulder brown
        t.begin_fill()
        for j in range (numsides):
            t.forward(sidelen)
            t.right(angle)
        t.end_fill()

def fish(numfish):
    """draw numfish fish with random colors randomly throughout the screen"""
    for i in range(numfish):
        x = r.randint(-350,350)
        y = r.randint(-200,-50)
        jumpto(x, y, 90)
        sidelen = r.randint(30,50)
        t.fillcolor(r.randint(0,1),r.randint(0,1),r.randint(0,1)) 
        t.begin_fill()
        for j in range(3):
            t.forward(sidelen)
            t.right(120)
        t.forward(sidelen/2)
        t.left(60)
        for k in range(3):
            t.forward(sidelen/2)
            t.left(120)
        t.end_fill()
        
def flowers(numflowers):
    """ Draw numflowers with random numbers of pedals """ 
    for i in range(numflowers):
        x = r.randint(-300,300)
        y = r.randint(-300,-250)
        jumpto(x, y, 0)
        radius = r.randint(5,10)
        num = r.randint(5,10)
        angle = 360/num
        t.fillcolor(r.randint(0,1),r.randint(0,1),r.randint(0,1)) 
        t.begin_fill()
        for j in range(num):
            t.circle(radius)
            t.right(angle)
        t.setheading(270)
        t.forward(radius*5)
        t.end_fill() #idea borrowed from rotating_circles in turtle_examples)

def bubbles(numbubbles):
    """draws bubbles of random radius randomly throughout the screen"""
    for i in range (numbubbles):
        x = r.randint(-350,350)
        y = r.randint(-350,0)
        radius = r.randint(3,5)
        jumpto(x, y, 90)
        t.fillcolor("white")
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

def triangle(x, y, sidelen):
    """draw a equilateral triangle with sides of sidelen at (x,y)"""
    jumpto(x, y, 90)
    t.fillcolor("red")
    t.begin_fill()
    for i in range(3):
        t.forward(sidelen)
        t.right(120)
    t.end_fill()

def polygon(x, y, numsides, sidelen):
    """draw a polygon with numsides sides of length sidelen at (x,y)"""
    jumpto(x, y, 90)
    angle = 360 / numsides #numsides >= 4
    t.fillcolor(BOULDER_BROWN) #hex code for boulder brown
    t.begin_fill()
    for i in range (numsides):
        t.forward(sidelen)
        t.right(angle)
    t.end_fill()

def add_circles(numcircles):
    """draws filled circles of random radius randomly throughout the screen"""
    t.fillcolor("white")
    t.begin_fill()
    for i in range (numcircles):
        x = r.randint(-350,350)
        y = r.randint(-350,350)
        radius = r.randint(5,100)
        jumpto(x, y, 90)
        t.circle(radius)
    t.end_fill()

def generate_picture():
    t.setup (width=700, height=700, startx=0, starty=0)
    lake()
    night_sky()
    moon()
    add_stars(70)
    boulders(10)
    fish(15)
    flowers(10)
    bubbles(50)