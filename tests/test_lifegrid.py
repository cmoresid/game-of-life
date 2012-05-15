import unittest

from exceptions import NotImplementedError
from lifegrid import LifeGrid

class TestLifeGrid(unittest.TestCase):
	def test_peek_vertical_boundaries(self):
		testgridbottom = LifeGrid(10,10)
		# (0, 0) + (0, -1) == (0, 9)
		testgridbottom.set_xy(0,9, True)
		self.assertTrue(testgridbottom.peek(0,0,0,-1))
		
		testgridtop = LifeGrid(10,10)
		# (0, 9) + (0, 1) == (0, 0)
		testgridtop.set_xy(0, 0, True)
		self.assertTrue(testgridtop.peek(0,9,0,1))
		
	def test_peek_horizontal_boundaries(self):
		testgridleft = LifeGrid(10,10)
		# (0, 0) + (-1, 0) == (9, 0)
		testgridleft.set_xy(9, 0, True)
		self.assertTrue(testgridleft.peek(0,0,-1,0))
		
		testgridright = LifeGrid(10,10)
		# (9, 0) + (1, 0) == (0, 0)
		testgridright.set_xy(0, 0, True)
		self.assertTrue(testgridright.peek(9,0,1,0))
		
	def test_peek_diagonal(self):
		testgrid_diagonal = LifeGrid(10,10)
		# (0, 0) + (-1, -1) == (9, 9)
		testgrid_diagonal.set_xy(9, 9, True)
		self.assertTrue(testgrid_diagonal.peek(0,0,-1,-1))
		
if __name__ == "__main__":
	unittest.main()