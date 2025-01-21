from p5 import *
from snake import * 
from common import * 
import random
import scoring


x4=0
y4=0
# BEGIN_RODYTI
x = 11; y = 12
x2 = 10; y2 = 12
x3 = 9; y3 = 12
# END_RODYTI
column_direction = 1
row_direction = 0
food_x = random.randint(1, 20)
food_y = random.randint(1, 20)
score = 0
scorring_finished= False
correct= False
frame_count = 0

def check():
    global scorring_finished,correct, frame_count

    frame_count += 1
    
    if scorring_finished==False:
      if frame_count == 3:
        if abs(x-x2)+abs(y-y2)==1 and abs(x2-x3)+abs(y2-y3)==1 and abs(x3-x4)+abs(y3-y4)==1:
          scoring.score("threeSegments4Cells", 1, 1)
          correct= True
          fill(143, 206, 44)
          textSize(CELL_HEIGHT * 2)                
          text("Correct", CELL_WIDTH * 6, CELL_HEIGHT * 6)  
        else:
          scoring.score("threeSegments4Cells", 0, 1)
          correct= False
          fill(249, 65, 61)
          textSize(CELL_HEIGHT * 2)                
          text("Incorect", CELL_WIDTH * 6, CELL_HEIGHT * 6) 
        scorring_finished=True
    else:
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
    global x, y, x2, y2, x3, y3, column_direction, row_direction, food_x, food_y, score, x4, y4

    draw_food(food_x, food_y)
    check()
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
