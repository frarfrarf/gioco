import pygame
import sys

from os import system
system("cls")

#gioco normale: 18 blocchi X 11
BOX = '§'
GOAL = '+'
WALL = 'P'
PLAYER = '£'
BOX_SIZE= 36
TRAGUARDO = ''
VOID = ' '
world = []
goals = []
pygame.init()
# def getScreenSize():
#     j = 0
#     for i in range(len(world)):
#         j = len(world[i]) if len(world[i]) > j else j
#     return j * BOX_SIZE, len(world) * BOX_SIZE


WINDOW_SIZES = (pygame.display.get_desktop_sizes()[0][0] - 200, pygame.display.get_desktop_sizes()[0][1] - 200)
# WINDOW_SIZES = getScreenSize()

pygame.display.init()
pygame.display.set_caption("Sokoban ma fiko")
screen = pygame.display.set_mode(WINDOW_SIZES)
screen.fill((255, 0 ,0))


def initWorld():
    global world
    with open('test.txt', 'r' , encoding = 'utf8')as f:
        for line in f.read():
            world.append(list(line))
    
    print(world)


def initGoals(world):
    print(world)
    for i in range(len(world)):
        for j in range(len(world[i])):
            if j == GOAL:
                goals.append(list(j))

def getScreenSize():
    j = 0
    for i in range(len(world)):
        j = len(world[i]) if len(world[i]) > j else j
    return j * BOX_SIZE, len(world) * BOX_SIZE

def drawWorld(screen):

    #mettere qua le varie immagini con:
    img_wall = pygame.image.load('muro verticale.png')
    # img_basement = pygame.image.load('pavimento base.png')
    img_char = pygame.image.load('omino ometto.png')
    img_goal = pygame.image.load('goal.png')
    img_traguardo = pygame.image.load('Scatoletta 3 verde.png')
    img_scatola = pygame.image.load('scatoletta 3.png')
    # image_XXX = pygame.image.load('da dove')
    images = {BOX: img_scatola,WALL: img_wall, PLAYER: img_char, TRAGUARDO: img_traguardo, GOAL: img_goal, VOID: }

    for i in range (len(world)):
        for j in range (len(world)):
            screen.blit(images[world[i][j]], (j*BOX_SIZE, i*BOX_SIZE))
            #nel blit metterò le varie immagini
    pygame.display.update()

# def main():5
initWorld()
goals = initGoals(world)


def isGoal(posi,posj):
    for goal in goals:
        if goal[0] == posi and goal[1] ==posj:
            return True
    return False

def getplayerpos():
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == PLAYER:
                return i,j

def doMove(posi,posj,i,j):
    world[posi+ i][posj+j] = PLAYER
    if isGoal(posi, posj):
        world[posi,posj] = GOAL
    else:
        world[posi][posj] = VOID
def movePlayer(i,j):
    posi,posj = getplayerpos()

    if world[posi+i][posj+j] == VOID:
        doMove(posi,posj,i,j)
    elif world[posi+i][posj+j] == WALL:
        pass
    elif world[posi+i][posj+j] == BOX:
        if world[posi + 2*i][posj +2*j] == VOID:
            world[posi + 2*i][posj +2*j] == BOX
            doMove(posi,posj,i,j)
        elif world[posi+ 2*i][posj+ 2*j] == GOAL:
            world[posi+ 2*i][posj + 2*j] = TRAGUARDO
            doMove(posi.posj,i,j)


def move_left():
    movePlayer(0, -1)
def move_right():
    movePlayer(0, 1)
def move_up():
    movePlayer(-1,0)
def move_down():
    movePlayer(1,0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right()
            elif event.key == pygame.K_LEFT:
                move_left()
            elif event.key == pygame.K_UP:
                move_up()
            elif event.key == pygame.K_DOWN:
                move_down()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                break
drawBoard(screen)
        



