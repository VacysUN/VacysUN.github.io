from p5 import *
from snake import * 


def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    # BEGIN_RODYTI
    # Draw the snake's head at column 10, row 5
    draw_cell(10, 5)
    # END_RODYTI
