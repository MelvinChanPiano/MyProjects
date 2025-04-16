A puzzle from the Advent of Code: Day 8 - Advent of Code 2022
adventofcode.com/2022/day/8/input

Programming language: Python

Purpose of Code:
You are given a grid of tree heights. A tree is visible if no taller or equal-height
tree blocks it in a straight line to any edge (up, down, left, or right). First, count
how many trees are visible from the outside.
Then, for each tree, calculate a scenic score by multiplying how far you can
see in each direction until a tree blocks the view. The task is to find the
highest scenic score in the grid.

Scale of project: 95 lines(excluding spaces), 11 functions.

Interesting implementations: 
Perform 1D projections on a 2D array. 
Involves list slicing, to decompose the problem.
