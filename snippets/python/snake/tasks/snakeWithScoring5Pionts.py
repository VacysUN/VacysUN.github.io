from p5 import *
from snake import * 
from common import * 
import random
import scoring

x = 9
y = 12
column_direction = 1
row_direction = 0
# BEGIN_RODYTI
food_x = random.randint(1, 20)
food_y = random.randint(1, 20)
score = 0
# END_RODYTI
old_score=score
scorring_finished= False
correct= False
old_food_x =food_x 
old_food_y =food_y 

def check():
    global correct,scorring_finished

    if x==old_food_x and y==old_food_y:
      if old_score+5==score:
        scoring.score("withScoring5Pionts", 1, 1)
        correct= True
        fill(143, 206, 44)
        textSize(CELL_HEIGHT * 2)                
        text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
      else:
        scoring.score("withScoring5Pionts", 0, 1)
        correct= False
        fill(249, 65, 61)
        textSize(CELL_HEIGHT * 2)                
        text("Incorect", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
      scorring_finished=True

    if scorring_finished==True:
      if correct==True:
        fill(143, 206, 44)
        textSize(CELL_HEIGHT * 2)                
        text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
      else:
        fill(249, 65, 61)
        textSize(CELL_HEIGHT * 2)                
        text("Incorect", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
        

def setup():
    createCanvas(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw():
    background(255)
    frameRate(5)
    draw_grid(GRID_COLUMNS, GRID_ROWS, CELL_WIDTH, CELL_HEIGHT)
    global x, y, column_direction, row_direction, food_x, food_y, score, old_food_x, old_food_y, old_score
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

    old_food_x=food_x
    old_food_y=food_y
    old_score=score

    # BEGIN_RODYTI
    if x == food_x and y == food_y:
      score += 1
      food_x = random.randint(1, 20)
      food_y = random.randint(1, 20)
    # END_RODYTI
    display_score(score)
    check()
