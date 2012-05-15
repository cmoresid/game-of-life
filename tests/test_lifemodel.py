import unittest
from exceptions import NotImplementedError
from lifemodel import LifeModel

class TestLifeModel(unittest.TestCase):
	def test_find_neighbours_none(self):
		testmodel = LifeModel(10,10)
		# Check from (1, 0)
		self.assertEquals(testmodel.find_neighbours(0,0), 0)
		
	def test_find_neighbours_1(self):
		testmodel = LifeModel(10,10)
		testmodel.set_seed(1,1)
		# Check from (1, 0)
		# (1, 1) is 1 unit below (1,0)
		self.assertEquals(testmodel.find_neighbours(1, 0), 1)
		
	def test_next_generation(self):
		# TODO: Finish writing test.
		self.assertTrue(True)
		
if __name__ == "__main__":
	unittest.main()