from p5 import *
from snake import * 
from snake import draw_cell  as draw_cell_orginal
import scoring

x_expected=20
y_expected=1
frame_count = 0
def draw_cell(x, y):
    global frame_count
    draw_cell_orginal(x, y)
    frame_count = frame_count + 1
    if frame_count == 3:
        if x==x_expected and y==y_expected:
            scoring.score("head", 1, 1)
            fill(143, 206, 44)
            textSize(CELL_HEIGHT * 2)                
            text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)
        else:
            scoring.score("head", 0, 1)
            fill(249, 65, 61)
            textSize(CELL_HEIGHT * 2)                
            text("Incorrect", CELL_WIDTH * 6, CELL_HEIGHT * 6)
        noLoop()        


def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    # BEGIN_RODYTI
    # Draw the snake's head at column 10, row 5
    draw_cell(10, 5)
    # END_RODYTI
