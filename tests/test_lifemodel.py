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