import pygame
from lifemodel import LifeModel

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
grey = (192,192,192)

class GameOfLife:
	def __init__(self):
		pygame.init()		
		self.cell_size = 25
		self.width  = 25 + 2
		self.height = 25 + 2
		self.margin = 1
		self.screen_size = [ \
			self.cell_size*self.width+(self.width), \
			self.cell_size*self.height+(self.width) \
		]

		self.toolbar_height = 50 + 2
		self.toolbar = pygame.surface.Surface((self.screen_size[0], self.toolbar_height))
			
		self.model = LifeModel(self.width, self.height)

		self.screen = pygame.display.set_mode(self.screen_size)
		pygame.display.set_caption("Game of Life")		
		
		self.game_text = pygame.font.SysFont("Comic Sans MS", 24)
		self.generation_label = self.game_text.render("Generation:", 1, black)

		self.start_button = pygame.image.load("img/start_button.png").convert()
		self.clear_button = pygame.image.load("img/clear_button.png").convert()

		self.clock = pygame.time.Clock()
		self.speed = 12
	
		
	def game_loop(self):
		done = False
		start = False
		
		while done == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					
					if self.start_button.get_bounding_rect().collidepoint(pos):
						start = False if start else True

					y = pos[0] // (self.cell_size+self.margin)
					x = pos[1] // (self.cell_size+self.margin)

					self.model.set_seed(x, y)
			
			if start:
				self.model.next_generation()
			
			self.screen.fill(black)

			self.screen.set_clip(0,0,self.screen_size[0], self.toolbar_height)
			self.draw_toolbar()			

			self.screen.set_clip(0,self.toolbar_height,self.screen_size[0], self.screen_size[1])			
			self.draw_world()

			self.clock.tick(self.speed)
			pygame.display.flip()

	def draw_toolbar(self):
		self.toolbar.fill(grey)
		self.screen.blit(self.toolbar, (0,0))	
		self.screen.blit(self.generation_label, (self.screen_size[0]-150,16))
		gen = self.game_text.render(str(self.model.generation), 1, black)
		self.screen.blit(gen, (self.screen_size[0]-50,16))
		self.screen.blit(self.start_button, (20, 0))
		self.screen.blit(self.clear_button, (130, 0))

	def draw_world(self):
		for x in range(self.width):
			for y in range(self.height):
				if self.model.get_currentgrid_xy(x, y) == False:
					color = white
				else:
					color = green

				pygame.draw.rect(self.screen, color, [ \
					self.margin+(self.cell_size+self.margin)* y, \
					self.margin+(self.cell_size+self.margin)* x, \
					self.cell_size, \
					self.cell_size \
				])
	
	def quit(self):
		pygame.quit()
		
if __name__ == "__main__":
	game = GameOfLife()
	game.game_loop()
	game.quit()
	
		
