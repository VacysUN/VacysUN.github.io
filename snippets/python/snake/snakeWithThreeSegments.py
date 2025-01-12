from p5 import *
from snake import * 
from common import * 
import random

x = 11
y = 12
x2 = 10
y2 = 12
x3 = 9
y3 = 12
column_direction = 1
row_direction = 0
# BEGIN_RODYTI
food_x = random.randint(1, 20)
food_y = random.randint(1, 20)
score = 0
# END_RODYTI

def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    global x, y, x2, y2, x3, y3, column_direction, row_direction, food_x, food_y, score

    draw_food(food_x, food_y)
    # BEGIN_RODYTI
    draw_cell(x, y)
    draw_cell(x2, y2)
    draw_cell(x3, y3)
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

    # BEGIN_RODYTI
    x3 = x2
    y3 = y2

    x2 = x
    y2 = y
    
    x = x + column_direction
    y = y + row_direction
    # END_RODYTI      

    if x == food_x and y == food_y:
      score += 1
      food_x = random.randint(1, 20)
      food_y = random.randint(1, 20)

    display_score(score)
