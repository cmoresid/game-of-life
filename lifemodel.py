from lifegrid import LifeGrid

class LifeModel:
	"""The main model that contains the games
	   logic. The model contains two LifeGrid
	   objects: one repesents the current generation
	   of cells and the other represents the next
	   generation. The 23/3 rules are applied to
	   the current generation grid and the results are
	   placed in the next generation grid. The roles
	   of the grids alternate with each call to
	   the next_generation method."""
	def __init__(self,width,height):
		"""Initializes the model with the specified
		   width and height (i.e. the number of cells
		   horizontally and vertically).
		"""
		# The two LifeGrids used to represent the world.
		self.lifegrid1 = LifeGrid(width, height)
		self.lifegrid2 = LifeGrid(width, height)
		# Variables that represent the current
		# role of each grid. These roles alternate
		# with each turn.
		self.currentgen_grid = self.lifegrid1
		self.nextgen_grid = self.lifegrid2
		# Set the dimensions of the grid.
		self.width = width
		self.height = height
		# Represents which generation the world is
		# currently on.
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
				# Finds the number of immediate surrounding
				# cells that are alive.
				nbrs = self.find_neighbours(x, y)
				# Apply the 23/3 rules to the current grid
				# and set results in the next generation grid.
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
		
		# Increment the generation count.
		self.increment_gen_count()
		# Now switch the roles of the grids.
		# i.e. the grid1 now is used as the current
		# generation and grid2 is now used as the
		# next generation.
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
	
	def print_world(self):
		print "Generation: ", self.generation
		self.currentgen_grid.print_grid()
	
