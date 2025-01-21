from p5 import *
from snake import * 
from common import *
import scoring 

x = 3
y = 3
column_direction = -1
row_direction = 0
x_color_expected='green'
x_end_text_expected='Column boundary'
y_color_expected='red'
y_end_text_expected='Row boundary'
color_from_parameter=''
end_text_from_parameter=''

def stop_game(color_name, end_text):
    global color_from_parameter, end_text_from_parameter
    color_from_parameter=color_name
    end_text_from_parameter=end_text
    fill(colors.get(color_name, "black"))
    textSize(40)
    textAlign(CENTER, CENTER)
    text(
        end_text,
        SCREEN_WIDTH / 2 + CELL_WIDTH,
        SCREEN_HEIGHT / 2 - CELL_HEIGHT
    )

def check():   
    global x,y,column_direction,row_direction
    #tinkinam ar gerai kai iseina is lentos stulpelyje 0
    if x < -1:
      if color_from_parameter==x_color_expected and end_text_from_parameter==x_end_text_expected:
        scoring.score("snakeWallCollisionText", 1, 4)
        fill(143, 206, 44)
        textSize(CELL_HEIGHT * 2)                
        text("Correct 1/4", CELL_WIDTH * 8, CELL_HEIGHT * 6)
      else:
        scoring.score("snakeWallCollisionText", 1, 4)
        fill(249, 65, 61)
        textSize(CELL_HEIGHT * 2)                
        text("Incorrect", CELL_WIDTH * 8, CELL_HEIGHT * 6)
        noLoop()
      x=16
      y=3
      column_direction = 1
      row_direction = 0
    #tinkinam ar gerai kai iseina is lentos eiluteje 0
    if x > 21 :
      if color_from_parameter==x_color_expected and end_text_from_parameter==x_end_text_expected:
        scoring.score("snakeWallCollisionText", 2, 4)
        fill(143, 206, 44)
        textSize(CELL_HEIGHT * 2)                
        text("Correct 2/4", CELL_WIDTH * 8, CELL_HEIGHT * 6)
      else:
        scoring.score("snakeWallCollisionText", 1, 4)
        fill(249, 65, 61)
        textSize(CELL_HEIGHT * 2)                
        text("Incorrect", CELL_WIDTH * 8, CELL_HEIGHT * 6)
        noLoop()
      x=16
      y=3
      column_direction = 0
      row_direction = -1
    #tinkinam ar gerai kai iseina is lentos eiluteje 20
    if y < -1 :
      if color_from_parameter==y_color_expected and end_text_from_parameter==y_end_text_expected:
        scoring.score("snakeWallCollisionText", 3, 4)
        fill(143, 206, 44)
        textSize(CELL_HEIGHT * 2)                
        text("Correct 3/4", CELL_WIDTH * 8, CELL_HEIGHT * 6)
      else:
        scoring.score("snakeWallCollisionText", 2, 4)
        fill(249, 65, 61)
        textSize(CELL_HEIGHT * 2)                
        text("Incorrect", CELL_WIDTH * 8, CELL_HEIGHT * 6)
        noLoop()
      x=16
      y=18
      column_direction = 0
      row_direction = 1
    if y > 21 :
      if color_from_parameter==y_color_expected and end_text_from_parameter==y_end_text_expected:
        scoring.score("snakeWallCollisionText", 4, 4)
        fill(143, 206, 44)
        textSize(CELL_HEIGHT * 2)                
        text("Correct 4/4", CELL_WIDTH * 8, CELL_HEIGHT * 6)
      else:
        scoring.score("snakeWallCollisionText", 3, 4)
        fill(249, 65, 61)
        textSize(CELL_HEIGHT * 2)                
        text("Incorrect", CELL_WIDTH * 8, CELL_HEIGHT * 6)
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

    if (x < 1 or x > 20) or (y < 1 or y > 20):
        stop_game('blue', 'Try again!')
    # END_RODYTI

    # if key == 'a' and column_direction != 1:
    #   column_direction = -1
    #   row_direction = 0
    # elif key == 'd' and column_direction != -1:
    #   column_direction = 1
    #   row_direction = 0
    # elif key == 'w' and row_direction != 1:
    #   column_direction = 0
    #   row_direction = -1
    # elif key == 's' and row_direction != -1:
    #   column_direction = 0
    #   row_direction = 1
    x = x + column_direction
    y = y + row_direction
    check()