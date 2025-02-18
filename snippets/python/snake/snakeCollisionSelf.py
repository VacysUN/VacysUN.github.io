from p5 import *
from snake import * 
from common import * 
import random

# BEGIN_RODYTI
xs = [11, 10, 9]
ys = [12, 12, 12]
# END_RODYTI

column_direction = 1
row_direction = 0
food_x = random.randint(1, 20)
food_y = random.randint(1, 20)
score = 0

def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    global xs, ys, column_direction, row_direction, food_x, food_y, score

    draw_food(food_x, food_y)
    # BEGIN_RODYTI
    for i in range(len(xs)):
        draw_cell(xs[i], ys[i]) 
    # END_RODYTI

    if (xs[0] < 1 or xs[0] > 20) or (ys[0] < 1 or ys[0] > 20):
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
    for j in range(len(xs) - 1, 0, -1):
        xs[j] = xs[j - 1]
        ys[j] = ys[j - 1]
    
    xs[0] += column_direction
    ys[0] += row_direction
    
    if xs[0] == food_x and ys[0] == food_y:
        xs.append(xs[-1])
        ys.append(ys[-1])
        score += 1
        food_x = random.randint(1, 20)
        food_y = random.randint(1, 20)
    # END_RODYTI      

    display_score(score)

    # BEGIN_RODYTI
    for i in range(1, len(xs)):
        if xs[i] == xs[0] and ys[i] == ys[0]:
            stop_game('red', 'You bit yourself!')
    # END_RODYTI
