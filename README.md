Game Of Life
============

A Simple Implementation of Conway's Game of Life written
in Python using PyGame. The rules used to determine the
evolution of the cells are the original '23/3' rules. The
board is represented using two toroidal structures backed by
a NumPy array. The algorithm used to determine the next
generation of cells is a bit naive (i.e. it checks all the
all cells, and not just ones that are likely to have changed.)
I might optimize the algorithm a bit later when I'm bored.

Requirements:
* PyGame 1.9.1 (GUI)
* NumPy  1.6.1 (Backend)

**Note:** I only tested the game with the above versions of the libraries,
so it may or may not work with other versions.

This is my first attempt at using PyGame, so the drawing/
event handling code might be a little weird.
