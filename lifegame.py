import pygame
from lifemodel import LifeModel
from lifeconstants import *

class GameOfLife:
	def __init__(self):
		pygame.init()		

		self.toolbar = pygame.surface.Surface((SCREEN_SIZE[0], TOOLBAR_HEIGHT))
		self.screen = pygame.display.set_mode(SCREEN_SIZE)
		pygame.display.set_caption(WINDOW_CAPTION)	
		
		self.model = LifeModel(BOARD_SIZE, BOARD_SIZE)
		self.start = False
		self.done  = False

		self.game_text = pygame.font.SysFont("Comic Sans MS", FONT_SIZE)
		self.generation_label = self.game_text.render(GENERATION_TEXT, 1, BLACK)

		self.start_button = pygame.image.load(START_BUTTON).convert()
		self.clear_button = pygame.image.load(CLEAR_BUTTON).convert()

		self.clock = pygame.time.Clock()
		self.speed = FRAME_RATE
	
	def game_loop(self):		
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
		if self.start_button.get_rect().move(START_BUTTON_LOC).collidepoint(pos):
			self.start = False if self.start else True

		if self.clear_button.get_rect().move(CLEAR_BUTTON_LOC).collidepoint(pos):
			self.start = False
			self.model.clear_world()
			
	def set_cell_state(self, pos):
		y = pos[0] // (CELL_SIZE+MARGIN)
		x = pos[1] // (CELL_SIZE+MARGIN)

		self.model.set_seed(x, y)
	
	def draw_toolbar(self):
		self.toolbar.fill(GREY)
		self.screen.blit(self.toolbar, (0,0))	
		
		self.screen.blit(self.generation_label, GENERATION_LABEL_LOC)
		
		gen = self.game_text.render(str(self.model.generation), 1, BLACK)
		self.screen.blit(gen, GENERATION_LOC)
		self.screen.blit(self.start_button, START_BUTTON_LOC)
		self.screen.blit(self.clear_button, CLEAR_BUTTON_LOC)

	def draw_world(self):
		for x in range(BOARD_SIZE):
			for y in range(BOARD_SIZE):
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
		pygame.quit()
		
if __name__ == "__main__":
	game = GameOfLife()
	game.game_loop()
	game.quit()
	
		
