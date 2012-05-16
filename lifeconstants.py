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

# Color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
GREY = (192,192,192)
# Visible view is 25
# + 2 since the toolbar hides two cells
BOARD_SIZE = 25 + 2
# Size of each cell on the board
CELL_SIZE = 25
# Size of the margin surrounding cells
MARGIN = 1
# Screen size
SCREEN_SIZE = [ \
	(CELL_SIZE*BOARD_SIZE)+BOARD_SIZE, \
	(CELL_SIZE*BOARD_SIZE)+BOARD_SIZE
]
# The height of the toolbar
TOOLBAR_HEIGHT = 50 + 2
# Window caption
WINDOW_CAPTION = "Game of Life"
# 'Generation:' Text
GENERATION_TEXT = "Generation:"
# Locations of the button images
START_BUTTON = "img/start_button.png"
CLEAR_BUTTON = "img/clear_button.png"
# Default frame rate
FRAME_RATE = 12
# Locations of various components on screen
GENERATION_LABEL_LOC = (SCREEN_SIZE[0]-200, 8)
GENERATION_LOC 		 = (SCREEN_SIZE[0]-70, 8)
START_BUTTON_LOC     = (20, 0)
CLEAR_BUTTON_LOC     = (130, 0)
# Font
FONT_SIZE = 22
FONT = "Comic Sans MS"