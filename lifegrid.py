# Copyright 2012 Connor Moreside
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np

class LifeGrid:
	"""The underlying structure used in LifeModel. 
	   Represents the world as a toroidal grid. A 
	   True value represents a live cell and a 
	   False value represents a dead cell. The X axis
	   goes horizontal, and the Y axix is vertical.
	   The co-ordinates are opposite in the array
	   representation, FYI. The type of array used
	   is a NumPy array. The only reason I used it
	   is because I wanted to learn the array API of
	   NumPy.
	"""
	def __init__(self, width, height):
		"""Initializes the multidimensional array
		   to be used as the grid. Width and height
		   are saved as instance variables as well.
		"""
		self.grid = np.zeros(width*height, dtype=np.bool).reshape(width,height)
		self.width = width
		self.height = height
		
	def toggle_xy(self, x, y):
		"""Toggles the value at the specified
		   co-ordinate. i.e. if the cell is dead,
		   make it alive, and vice versa.
		"""
		self.grid[y, x] = False if self.grid[y,x] else True
		
	def clear(self):
		"""Clears the board by setting
		   all the values in grid to false.
		"""
		self.grid.fill(False)

	def get_xy(self, x, y):
		"""Returns the value specified by
		   the given co-ordinate.
		"""
		return self.grid[y, x]
		
	def set_xy(self, x, y, val):
		"""Sets the value at the given
		   co-ordinate.
		"""
		self.grid[y, x] = val
		
	def peek(self, x, y, horz = 0, vert = 0):
		"""This method is where the toroidal
		   'magic' comes from. If the
		   co-ordinate lies on a boundary and
		   the horz or vert over-steps that
		   boundary, the resulting value
		   corresponds to co-ordinate
		   is 'wrapped around.'
		   
		   
		   Example: Peek from co-ordinate (0, 0). Set
		     the value of (9, 0) ( (0,0) + (-1, 0) ) 
			 to True. Peek at the 'wrapped' value.
			 
		   >>> grid = LifeGrid(10, 10)
		   >>> grid.set_xy(9, 0, True)
		   >>> grid.peek(0, 0, -1, 0)
		   True
		   
		"""
		X, Y = x + horz, y + vert
		
		if (X < 0):
			X = self.width - 1
		elif (X > self.width - 1):
			X = 0
		if (Y < 0):
			Y = self.height - 1
		elif (Y > self.height - 1):
			Y = 0
			
		return self.get_xy(X, Y)
		
	def print_grid(self):
		"""Prints out the grid. Used
		   for debugging purposes.
		"""
		print self.grid
