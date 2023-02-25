# Name: Ben Morgan
# Class: CS 424-01
# Assignment: Programming Assignment 1
# Purpose: Use Python to implement a text-based version of the card game Exploding Kittens. Do not implement the special combos.

# https://www.geeksforgeeks.org/python-oops-concepts/

# Requirements for your program:
    # Use only built-in Python libraries.
    # Use object-oriented techniques (classes, etc.). You should not have any methods (other than a main method) outside of any classes.
    # Utilize modularity. In addition to classes, you must keep methods small and focused, i.e., do not have a very large main method - preferably keep to 10 lines or less - and do not have very large instance methods in your classes.
    # Document your code. In addition to good identifier names, use comments to explain your code (don't just repeat the obvious).
    # Put a comment header at the top your file(s) with your name, the name of the programming assignment, and a brief description of what your program does.
    # Allow the user to play the game (i.e., don't make a simulation of the game - it must be interactive).
    # Give extremely clear instructions to the user for how to enter input.
    # DO NOT copy any part of the assignment from the internet. Do not do an internet search for exploding kittens in Python (or any other language). Do not search for how to set up cards for a card game in Python. And so on. You CAN search for things like how to create classes in Python and how to do list comprehensions and things like that.
    # See the rubric for grading details.
    # Name your main file program1.py. If you use additional files, name them prog1_whatever.py, where "whatever" is whatever name you want to use.

from deck import *
from players import *

game = deck()
game.build()
