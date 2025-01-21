from p5 import *
from snake import *
import scoring  

# BEGIN_RODYTI
x = 9
y = 12
column_direction = 1 
row_direction = 0
# END_RODYTI

frame_count = 0
coords = []

def check():
    global frame_count
    global x, y
    if key == "p":
      coords.append((x, y))
      frame_count = frame_count + 1
      if frame_count == 3:
          correct = True
          for (x1, y1), (x2, y2) in zip(coords[:-1], coords[1:]):
              if (x1, y1 ) != (x2, y2):
                  correct = False
                  break
          if correct:
              scoring.score("noReversePause", 1, 1)
              fill(143, 206, 44)
              textSize(CELL_HEIGHT * 2)                
              text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)
          else:
              scoring.score("noReversePause", 0, 1)
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
    global x, y, column_direction, row_direction
    # BEGIN_RODYTI
    draw_cell(x, y)
    if key == 'a' and column_direction != 1:
      column_direction = -1
      row_direction = 0
    elif key == 'd' and column_direction != -1:
      column_direction = 1
      row_direction = 0
    elif key == 'w' and row_direction != 1:
      column_direction = 0
      row_direction = -1
    elif key == 's' and row_direction != -1:
      column_direction = 0
      row_direction = 1
    x = x + column_direction
    y = y + row_direction
    # END_RODYTI
    check()