from p5 import *
from snake import * 
from common import * 
import random
import scoring

x = 3
y = 3
column_direction = 1
row_direction = 0
a_expected=10
b_expected=15
correct = False

def check():
    if correct:
      scoring.score("foodRightCorner", 1, 1)
      fill(143, 206, 44)
      textSize(CELL_HEIGHT * 2)                
      text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
    else:
      scoring.score("foodRightCorner", 0, 1)
      fill(249, 65, 61)
      textSize(CELL_HEIGHT * 2)                
      text("Incorect", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
    noLoop()  

original_randint = random.randint
def randint(a, b):
    global correct
    if a==a_expected and b==b_expected:
      correct = True
    else:
      correct = False
    return original_randint(a , b )

random.randint = randint

# BEGIN_RODYTI
food_x = random.randint(1, 20)
food_y = random.randint(1, 20)
# END_RODYTI

def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    
    noFill()
    stroke('green')
    strokeWeight(4)
    rect(
        CELL_WIDTH * 10,
        CELL_HEIGHT * 10 ,
        CELL_WIDTH * 6,
        CELL_HEIGHT * 6,
    )
    stroke(72, 72, 72)
    strokeWeight(1)

    global x, y, column_direction, row_direction, food_x, food_y
    # BEGIN_RODYTI
    draw_food(food_x, food_y)
    draw_cell(x, y)
    # END_RODYTI

    if (x < 1 or x > 20) or (y < 1 or y > 20):
        stop_game('blue', 'Try again!')
    
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

    check()
