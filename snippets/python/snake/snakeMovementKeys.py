from p5 import *
from snake import * 

# BEGIN_RODYTI
x = 9
y = 12
column_direction = 0 
row_direction = 0
# END_RODYTI

def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    global x, y, column_direction, row_direction
    # BEGIN_RODYTI
    draw_cell(x, y)
    if key == "a":
      column_direction = -1
      row_direction = 0
    elif key == "d":
      column_direction = 1
      row_direction = 0
    elif key == "w":
      column_direction = 0
      row_direction = -1
    elif key == "s":
      column_direction = 0
      row_direction = 1
    x = x + column_direction
    y = y + row_direction
    # END_RODYTI
