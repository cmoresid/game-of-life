from lifegame import GameOfLife

"""Main driver for game."""
if __name__ == "__main__":
	app = GameOfLife()
	app.game_loop()
	app.quit()