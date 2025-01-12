from p5 import *
from snake import * 

# BEGIN_RODYTI
x = 9
y = 12
# END_RODYTI

def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    global x, y
    # BEGIN_RODYTI
    draw_cell(x, y)
    x = x + 1
    # END_RODYTI
