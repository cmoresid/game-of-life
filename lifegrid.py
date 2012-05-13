import numpy as np

class LifeGrid:
	def __init__(self, width, height):
		self.grid = np.zeros(width*height, dtype=np.bool).reshape(width,height)
		self.width = width
		self.height = height
		
	def toggle_xy(self, x, y):
		self.grid[y, x] = False if self.grid[y,x] else True
		
	def get_xy(self, x, y):
		return self.grid[y, x]
		
	def set_xy(self, x, y, val):
		self.grid[y, x] = val
		
	def peek(self, x, y, horz = 0, vert = 0):
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
		print self.grid