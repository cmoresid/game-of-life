import numpy as np
from lifegrid import LifeGrid

class LifeModel:
	def __init__(self,width,height):
		self.lifegrid1 = LifeGrid(width, height)
		self.lifegrid2 = LifeGrid(width, height)
		self.currentgen_grid = self.lifegrid1
		self.nextgen_grid = self.lifegrid2
		self.width = width
		self.height = height
		self.generation = 1
	
	def switch_grid_roles(self):
		if (self.nextgen_grid == self.lifegrid1):
			self.nextgen_grid = self.lifegrid2
			self.currentgen_grid = self.lifegrid1
		else:
			self.nextgen_grid = self.lifegrid1
			self.currentgen_grid = self.lifegrid2
	
	def get_nextgen_grid(self):
		return self.nextgen_grid
		
	def set_seed(self, x, y):
		self.currentgen_grid.toggle_xy(x, y)

	def get_currentgrid_xy(self, x, y):
		return self.currentgen_grid.get_xy(x, y)
	
	def increment_gen_count(self):
		self.generation = self.generation + 1
		
	def clear_world(self):
		self.currentgen_grid.clear()
		self.nextgen_grid.clear()
		self.generation = 1

	def next_generation(self):
		for x in range(self.width):
			for y in range(self.height):
				nbrs = self.find_neighbours(x, y)
				
				if self.currentgen_grid.get_xy(x,y):
					if (nbrs == 2 or nbrs == 3):
						self.nextgen_grid.set_xy(x, y, True)
					else:
						self.nextgen_grid.set_xy(x, y, False)
				else:
					if (nbrs == 3):
						self.nextgen_grid.set_xy(x, y, True)
					else:
						self.nextgen_grid.set_xy(x, y, False)
		
		self.increment_gen_count()
		self.switch_grid_roles()
		
	def find_neighbours(self, x, y):
		i = -1
		num = 0
		
		while (i < 2):
			if self.currentgen_grid.peek(x, y, i, -1):
				num = num + 1
			if self.currentgen_grid.peek(x,y,i,1):
				num = num + 1
			
			i = i + 1
		
		if self.currentgen_grid.peek(x, y, -1, 0):
			num = num + 1
		if self.currentgen_grid.peek(x, y, 1, 0):
			num = num + 1
			
		return num			
		
	def print_world_debug(self):
		print "Current Board:"
		self.currentgen_grid.print_grid()
		print "Next Gen:"
		self.nextgen_grid.print_grid()
	
	def print_world(self):
		print "Generation: ", self.generation
		self.currentgen_grid.print_grid()

if __name__ == "__main__":
	l = LifeModel(10, 10)
	l.set_seed(5, 4)
	l.set_seed(4, 5)
	l.set_seed(5, 5)
	l.set_seed(6, 5)
	
	for i in range(10):
		print ""
		l.print_world()
		l.next_generation()
	
