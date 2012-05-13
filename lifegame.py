import pygame
from lifemodel import LifeModel

black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

class GameOfLife:
	def __init__(self):
		pygame.init()
		
		self.cell_size = 25
		self.width = 25
		self.height = 25
		self.margin = 1
		self.screen_size = [ \
			self.cell_size*self.width+(self.width), \
			self.cell_size*self.height+(self.width) \
		]
			
		self.model = LifeModel(self.width, self.height)
		self.screen = pygame.display.set_mode(self.screen_size)
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
					y = pos[0] // (self.cell_size+self.margin)
					x = pos[1] // (self.cell_size+self.margin)
					self.model.set_seed(x, y)
				if event.type == pygame.KEYDOWN:
					keys = pygame.key.get_pressed()
					if keys[pygame.K_RETURN] == 1:
						start = True
			
			if start:
				self.model.next_generation()
			
			self.screen.fill(black)
		
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
				
			self.clock.tick(self.speed)
			pygame.display.flip()
	
	def quit(self):
		pygame.quit()
		
if __name__ == "__main__":
	game = GameOfLife()
	game.game_loop()
	game.quit()
	
		