# importing the required libraries

import sys
import time
import pygame as pg
from pygame.locals import *
from exercise_1 import astar


width = 400
height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)



# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()

# infrastructure of the display
screen = pg.display.set_mode((width, height + 160), 0, 32)

# game window
pg.display.set_caption("Find the shortest path")

# loading the images as python object
initiating_window = pg.image.load("images.jpg")

# resizing images
initiating_window = pg.transform.scale(
	initiating_window, (width, height + 160))


centers = []
maze_w = 10
maze_h = 10
for i in range(maze_w):
    temp=[]
    for j in range(maze_h):
        temp.append((height/(2*maze_h)+height/maze_h*j, width/(2*maze_w)+width/maze_w*i))
    centers.append(temp)
def draw_rect(center, w, h, color):
    pt1 = (center[0]-w/2, center[1]-h/2)
    pt2 = (center[0]+w/2, center[1]+h/2)
    rect_object = pg.Rect(pt1[0], pt1[1], w, h)
    pg.draw.rect(screen, color, rect_object)

button_color = (50, 255, 250)
def draw_button(center, w, h, color, text):
    draw_rect(center, w, h, color)
    font = pg.font.SysFont('Constantia',20)
    text = font.render(text, 1, (255, 0, 90))
    text_rect = text.get_rect(center=center)
    screen.blit(text, text_rect)

def game_initiating_window():
    # displaying over the screen
    screen.blit(initiating_window, (0, 0))

    # updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    for i in range(len(centers)):
        for j in range(len(centers[i])):
            if maze[i][j] == 1:
                color = (0, 0, 0)
            elif maze[i][j] == 0:
                color = (200, 200, 200)
            if start == (i, j):
                color = (0, 255, 0)
            if goal == (i, j):
                color = (255, 0, 0)
            draw_rect(centers[i][j], 36, 36, color)
    draw_button((200, 480), 80, 60, (250, 150, 100), 'SOLVE')

def solve(start, goal):
    global maze, old_path
    path = astar(maze, start, goal)
    for pos in old_path:
        if pos != start and pos != goal:
            if maze[pos[0]][pos[1]]==0:
                draw_rect(centers[pos[0]][pos[1]], 36, 36, (200, 200, 200))
            if maze[pos[0]][pos[1]]==1:
                draw_rect(centers[pos[0]][pos[1]], 36, 36, (0, 0, 0))
    for pos in path:
        if pos != start and pos != goal:
            draw_rect(centers[pos[0]][pos[1]], 36, 36, (150, 100, 150))
            pg.display.update()
            time.sleep(0.2)
    old_path = path
    print('Done')

node = None
def user_click():
    global maze, start, goal
	# get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    for i in range(len(centers)):
        for j in range(len(centers[i])):
            if x<(centers[i][j][0]+width/2/maze_w) and x>(centers[i][j][0]-width/2/maze_w) and y<(centers[i][j][1]+height/2/maze_h) and y>(centers[i][j][1]-height/2/maze_h) and (i, j)!=start and (i, j)!=goal:
                if maze[i][j] == 0:
                    maze[i][j] = 1
                    draw_rect(centers[i][j], 36, 36, (0, 0, 0))
                elif maze[i][j] == 1:
                    maze[i][j] = 0
                    draw_rect(centers[i][j], 36, 36, (200, 200, 200))

    if (x<240 and x>160 and y<510 and y>450):
        solve(start, goal)



start = (0, 0)
goal = (8, 9)
old_path = []

maze =     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],  # 1: obstacle position
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
# maze = []
# for i in range(maze_h):
#     temp = []
#     for j in range(maze_w):
#         temp.append(0)
#     maze.append(temp)

game_initiating_window()

while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            user_click()
    # print(node.state)
    pg.display.update()
    CLOCK.tick(fps)
