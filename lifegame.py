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

import pygame
from lifemodel import LifeModel
from lifeconstants import *

class GameOfLife:
	"""The core class of the game. Responsible
	   for drawing the world and responding to
       user events. This is the view of the
       application.
	"""
	def __init__(self):
		"""Initializes the PyGame framework and various
		   other elements.   
		"""
		pygame.init()		

		self.screen = pygame.display.set_mode(SCREEN_SIZE)
		pygame.display.set_caption(WINDOW_CAPTION)	
		
		# Create toolbar
		self.toolbar = pygame.surface.Surface((SCREEN_SIZE[0], TOOLBAR_HEIGHT))
		
		# Initialize the model
		self.model = LifeModel(BOARD_SIZE, BOARD_SIZE)
		self.start = False
		self.done  = False
		
		# Create the "Generation:" label object
		self.game_text = pygame.font.SysFont(FONT, FONT_SIZE)
		self.generation_label = self.game_text.render(GENERATION_TEXT, 1, BLACK)
		
		# Load the button images
		self.start_button = pygame.image.load(START_BUTTON).convert()
		self.clear_button = pygame.image.load(CLEAR_BUTTON).convert()

		# Initialize frame rate stuff
		self.clock = pygame.time.Clock()
		self.speed = FRAME_RATE
	
	def game_loop(self):
		"""Contains the core game loop that
		   listens for events and manipulates
		   the world accordingly. Also responsible
		   for updating the screen.
		"""
		while self.done == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.done = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
				
					self.detect_button_events(pos)
					self.set_cell_state(pos)
			
			if self.start:
				self.model.next_generation()
			
			self.screen.fill(BLACK)

			self.screen.set_clip(0,0,SCREEN_SIZE[0], TOOLBAR_HEIGHT)
			self.draw_toolbar()			

			self.screen.set_clip(0,TOOLBAR_HEIGHT,SCREEN_SIZE[0], SCREEN_SIZE[1])			
			self.draw_world()

			self.clock.tick(FRAME_RATE)
			pygame.display.flip()
	
	def detect_button_events(self, pos):
		"""Detects when either of the two buttons
		   are clicked and manipulates the world
		   accordingly.
		"""
		if self.start_button.get_rect().move(START_BUTTON_LOC).collidepoint(pos):
			self.start = False if self.start else True

		if self.clear_button.get_rect().move(CLEAR_BUTTON_LOC).collidepoint(pos):
			self.start = False
			self.model.clear_world()
			
	def set_cell_state(self, pos):
		"""Toggles the state of a cell. Green
		   represents a live cell and white
		   represents a dead cell.
		"""
		y = pos[0] // (CELL_SIZE+MARGIN)
		x = pos[1] // (CELL_SIZE+MARGIN)

		self.model.set_seed(x, y)
	
	def draw_toolbar(self):
		"""Draws the toolbar to the screen."""
		self.toolbar.fill(GREY)
		self.screen.blit(self.toolbar, (0,0))	
		
		self.screen.blit(self.generation_label, GENERATION_LABEL_LOC)
		
		gen = self.game_text.render(str(self.model.generation), 1, BLACK)
		self.screen.blit(gen, GENERATION_LOC)
		self.screen.blit(self.start_button, START_BUTTON_LOC)
		self.screen.blit(self.clear_button, CLEAR_BUTTON_LOC)

	def draw_world(self):
		"""Draws the state of the world based
		   on the state of each cell in the LifeModel.
		"""
		for x in range(BOARD_SIZE):
			for y in range(BOARD_SIZE):
				# If the cell is dead, color it white.
				# Else the cell is alive, color it green.
				if self.model.get_currentgrid_xy(x, y) == False:
					color = WHITE
				else:
					color = GREEN

				pygame.draw.rect(self.screen, color, [ \
					MARGIN+(CELL_SIZE+MARGIN)* y, \
					MARGIN+(CELL_SIZE+MARGIN)* x, \
					CELL_SIZE, \
					CELL_SIZE \
				])
	
	def quit(self):
		"""Called when the user presses
		   the close button. Cleans up the
		   PyGame framework.
		"""
		pygame.quit()	
		
