"""#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
##########################################################
# maze solving program using the Left Hand Rule algorithm
# DavisMT 07.01.2018
##########################################################

import turtle                    # import turtle library
import time
import sys

wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # set the background colour
wn.setup(1300,700)                  # setup the dimensions of the working window


# class for the Maze turtle (white square)
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)                   # sets the speed that the maze is written to the screen

# class for the End marker turtle (green square)
class End(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

# class for the sprite turtle (red turtle)
class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)  # point turtle to point down
        self.penup()
        self.speed(0)


    def spriteDown(self):
        if (self.heading() == 270):                   # check to see if the sprite is pointing down
            x_walls = round(sprite.xcor(),0)          # sprite x coordinates =
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:          # if sprite and the
                print("Finished")
                endProgram()
            if (x_walls +24, y_walls) in walls:          # check to see if they are walls on the left
                if(x_walls, y_walls -24) not in walls:   # check to see if path ahead is clear
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


    def spriteleft(self):
        if (self.heading() == 0):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls, y_walls +24) in walls:       # check to see if they are walls on the left
                if(x_walls +24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


    def spriteUp(self):
        if (self.heading() == 90):
            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls -24, y_walls ) in walls:  # check to see if they are walls on the left
                if (x_walls, y_walls + 24) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)

    def spriteRight(self):
        if (self.heading() == 180):

            x_walls = round(sprite.xcor(),0)
            y_walls = round(sprite.ycor(),0)
            if (x_walls, y_walls) in finish:   # check turtle coordinates are at the finish line
                print("Finished")
                endProgram()
            if (x_walls, y_walls -24) in walls:  # check to see if they are walls on the left
                if (x_walls - 24, y_walls) not in walls:
                    self.forward(24)
                else:
                    self.right(90)
            else:
                self.left(90)
                self.forward(24)


def endProgram():
    wn.exitonclick()
    sys.exit()


grid = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+  ++++++++++  +++++++++++++  +++++++  ++++  +",
"+           +                 +        +     +",
"+  +++++++  +++++++++++++  +++++++++++++++++++",
"+  +     +  +           +  +                 +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +",
"+  +  +  +  +  +  +     +  +  +  +        +  +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  +",
"+  +     +  +              +           +  +  +",
"+  ++++  +  ++++++++++++++++  +++++++++++++  +",
"+     +  +                    +              +",
"++++  +  ++++++++++++++++++++++  ++++++++++  +",
"+  +  +                    +     +     +  +  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  +",
"+  +  +     +     +     +  +  +     +     +  +",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  +",
"+                       +  +  +              +",
"++++  +  +  ++++++++++  +  +  +  +++++++++++++",
"+++++++++++++++++++++++e++++++++++++++++++++++",
]


def setupMaze(grid):
    for y in range(len(grid)):                       # select each line in the grid
        for x in range(len(grid[y])):                # identify each character in the line
            character = grid[y][x]                   # assign the grid reference to the variable character
            screen_x = -588 + (x * 24)               # assign screen_x to screen starting position for x ie -588
            screen_y = 288 - (y * 24)                # assign screen_y to screen starting position for y ie  288

            if character == "+":                     # if grid character contains an +
                maze.goto(screen_x, screen_y)        # move turtle to the x and y location and
                maze.stamp()                         # stamp a copy of the turtle (white square) on the screen
                walls.append((screen_x, screen_y))   # add coordinate to walls list

            if character == "e":                     # if grid character contains an e
                end.goto(screen_x, screen_y)         # move turtle to the x and y location and
                end.stamp()                          # stamp a copy of the turtle (green square) on the screen
                finish.append((screen_x, screen_y))  # add coordinate to finish list

            if character == "s":                     # if the grid character contains an s
                sprite.goto(screen_x, screen_y)      # move turtle to the x and y location


# ############ main program starts here  ######################

maze = Maze()                # enable the maze class
sprite = sprite()            # enable the sprite  class
end = End()                  # enable End position class
walls =[]                    # create walls coordinate list
finish = []                  # enable the finish array

setupMaze(grid)              # call the setup maze function

while True:
        sprite.spriteRight()
        sprite.spriteDown()
        sprite.spriteleft()
        sprite.spriteUp()

        time.sleep(0.02)
