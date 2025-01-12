from p5 import *
from snake import *
import scoring

# BEGIN_RODYTI
x = 9
y = 12
# END_RODYTI

frame_count = 0
coords = []

def check():
    global frame_count, y
    coords.append(y)
    frame_count += 1
    if frame_count == 5:
        correct = all(y1 + 1 == y2 for y1, y2 in zip(coords[:-1], coords[1:]))
        if correct:
            scoring.score("movementDown", 1, 1)
            fill(143, 206, 44)
            textSize(CELL_HEIGHT * 2)                
            text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)
        else:
            scoring.score("movementDown", 0, 1)
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
    global x, y
    # BEGIN_RODYTI
    draw_cell(x, y)
    x += 1
    # END_RODYTI
    check()
