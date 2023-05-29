import pygame
import sys
# from PIL import  ImageFont
from os import system
system("cls")

#gioco normale: 18 blocchi X 11
BOX = '§'
GOAL = '+'
WALL = 'P'
PLAYER = '£'
BOX_SIZE= (36,36)
BOX_SCALE = (42,42)
TRAGUARDO = '*'
VOID = ' '
world = []
goals = []


file = "level1.txt"
pygame.init()
# def getScreenSize():
#     j = 0
#     for i in range(len(world)):
#         j = len(world[i]) if len(world[i]) > j else j
#     return j * BOX_SIZE[1], len(world) * BOX_SIZE[0]


WINDOW_SIZES = (pygame.display.get_desktop_sizes()[0][0] - 890, pygame.display.get_desktop_sizes()[0][1] - 430)
# WINDOW_SIZES = getScreenSize()

pygame.display.init()
pygame.display.set_caption("Sokoban ma fiko")
screen = pygame.display.set_mode(WINDOW_SIZES)
# screen.fill((255, 0 ,0))  COMMENTO ABRAHAM questo lo spostiamo nel while principale, in modo che lo faccia non solo all'inizio, ma sempre


def initWorld():
    global world
    with open(file, 'r' , encoding = 'utf8')as f:
        # for line in f.read():
        #      COMMENTO ABRAHAM Da qua in poi ci sono i cambiamenti nel reading del file
        #     line_final = "" COMMENTO ABRAHAM è la linea finale che passerò al world
        #     for char in line:   COMMENTO ABRAHAM controllo se un singolo carattere è un \n <---- da linea 77
        #         if char != "\n":
        #             line_final += f"{char}"
                    
        #     world.append(list(line_final))
        for line in f.read().splitlines():
            world.append(list(line))

def initGoals():
    global world
    global goals
    # for i in range(len(world)):
    #     print(world[i])
    #     for j in range(len(world[i])):
    #         if j == GOAL:
    #             goals.append(list(j))
    print(world)
    for i in range(len(world)):
        for j in range(len(world[i])):
            if world[i][j] == GOAL:
                goals.append([i, j])            #problema del mangiaggio di goal
    return goals

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
    world[posi+i][posj+j] = PLAYER
    if isGoal(posi, posj):
        world[posi][posj] = GOAL
    else:
        world[posi][posj] = VOID

def movePlayer(i,j):
    posi,posj = getplayerpos()

    if world[posi+i][posj+j] == VOID:
        doMove(posi,posj,i,j)


    elif world[posi+i][posj+j] == GOAL:
        doMove(posi,posj,i,j)


    elif world[posi+i][posj+j] == BOX:
        if world[posi + (2*i)][posj + (2*j)] == VOID:
            world[posi + (2*i)][posj +(2*j)] = BOX
            doMove(posi,posj,i,j)
             
        elif world[posi+ (2*i)][posj+ (2*j)] == GOAL:
            world[posi+ (2*i)][posj + (2*j)] = TRAGUARDO
            doMove(posi,posj,i,j)
    

    elif world[posi+i][posj+j] == TRAGUARDO:
        if world[posi+(2*i)][posj+(2*j)] == VOID:
            world[posi+(2*i)][posj+(2*j)] = BOX
            doMove(posi, posj, i, j)

        elif world[posi+(2*i)][posj+(2*j)] == GOAL:
            world[posi+(2*i)][posj+(2*j)] = TRAGUARDO
            doMove(posi, posj, i, j)


    elif world[posi+i][posj+j] == WALL:
        pass

def move_left():
    movePlayer(0, -1)
def move_right():
    movePlayer(0, 1)
def move_up():
    movePlayer(-1,0)
def move_down():
    movePlayer(1,0)

    
def getScreenSize():
    j = 0
    for i in range(len(world)):
        j = len(world[i]) if len(world[i]) > j else j
    return j * BOX_SIZE, len(world) * BOX_SIZE

def allTraguardo():
    allTrag= []
    for i in range(len(world)):
        for j in range (len(world[i])):
            if world[i][j] == TRAGUARDO:
                allTrag.append(world[i][j])
    if len(allTrag) == len(goals):
        return True
    else:
        return False


def drawWorld(screen):

    #mettere qua le varie immagini con:
    img_wall = pygame.transform.scale(pygame.image.load('wallpixel.png'), BOX_SIZE)
    img_void = pygame.transform.scale(pygame.image.load('Black-Square.png'), BOX_SIZE)
    img_char = pygame.transform.scale(pygame.image.load('omino ometto.png'), BOX_SIZE)
    img_goal = pygame.transform.scale(pygame.image.load('goal.png'), BOX_SIZE)
    img_traguardo = pygame.transform.scale(pygame.image.load('Scatoletta 3 verde.png'), (BOX_SIZE))
    img_scatola = pygame.transform.scale(pygame.image.load('scatoletta 3.png'), BOX_SIZE)
    # image_XXX = pygame.image.load('da dove')
    images = {BOX: img_scatola,WALL: img_wall, PLAYER: img_char, TRAGUARDO: img_traguardo, GOAL: img_goal, VOID: img_void }

    for i in range (len(world)):## COMMENTO ABRAHAM se metti solo len(world) i sarà maggiore dell'i massimo della matrice
        for j in range (len(world[i])): ## COMMENTO ABRAHAM stessa cosa
            screen.blit(images[world[i][j]], (j*BOX_SIZE[0], i*BOX_SIZE[1])) ## COMMENTO ABRAHAM ora dobbiamo far sì che '\n' sparisca, visto che non è una key del dizionario "images" ----> riga 41 
            #nel blit metterò le varie immagini
            font = pygame.font.SysFont(pygame.font.get_default_font(),int(WINDOW_SIZES[1]), bold = True, italic = False)
            nxt_img = font.render("premi e per andare al prossimo livello, premi w per andare al livello precedente", True, (255,255,255))
            nxt_img = pygame.transform.scale(nxt_img, ((nxt_img.get_width())/20, (nxt_img.get_height())/10))
            screen.blit(nxt_img,((WINDOW_SIZES[0] - nxt_img.get_width())/5,( WINDOW_SIZES[1]- nxt_img.get_height())))

        if allTraguardo():
                    screen.fill((29,48,95))
                    # screen.draw_text("HAI VINTO", )
                    # screen.draw_text("premi spazio per giocare di nuovo", )
                    # font = pygame.font.truetype(r'C:\Users\System-Pc\Desktop\arial.ttf', 20) 
                    # text = 'HAI \n VINTO'
                    # screen.draw.text((5, 5), text, font = font, align ="left")
                    font = pygame.font.SysFont(pygame.font.get_default_font(),int(WINDOW_SIZES[1]), bold = True, italic = False)
                    win_img = font.render("HAI VINTO", True, (255,255,255))
                    win_img = pygame.transform.scale(win_img, ((win_img.get_width())/3, (win_img.get_height())/3))
                    screen.blit(win_img,((WINDOW_SIZES[0] - win_img.get_width())/3,( WINDOW_SIZES[1]- win_img.get_height())/2 ))
                    win_height = win_img.get_height()
                    rest_img = font.render("premi r per restartare", True, (0,255,255))
                    rest_img = pygame.transform.scale(rest_img, ((rest_img.get_width())/10, (rest_img.get_height())/10))
                    screen.blit(rest_img,((WINDOW_SIZES[0] - rest_img.get_width())/2,( WINDOW_SIZES[1]- rest_img.get_height())/2+win_height+10))
                   
                    
    pygame.display.update()


goals = []
def main():
    world = initWorld()
    goals = initGoals()

    # def initWorld():
    #     with open('level1.txt', 'r' , encoding = 'utf8')as f:
    #         # for line in f.read():
    #         #     ## COMMENTO ABRAHAM Da qua in poi ci sono i cambiamenti nel reading del file
    #         #     line_final = "" ## COMMENTO ABRAHAM è la linea finale che passerò al world
    #         #     for char in line: ##  COMMENTO ABRAHAM controllo se un singolo carattere è un \n <---- da linea 77
    #         #         if char != "\n":
    #         #             line_final += f"{char}"
                        
    #         #     world.append(list(line_final))
    #         for line in f.read().splitlines():
                # world.append(list)

    # def initGoals():
    #     for i in range(len(world)):
    #         print(world[i])
    #         for j in range(len(world[i])):
    #             if world[i][j] == GOAL:
    #                 goals.append(i, j)

    # def getScreenSize():
    #     j = 0
    #     for i in range(len(world)):
    #         j = len(world[i]) if len(world[i]) > j else j
    #     return j * BOX_SIZE, len(world) * BOX_SIZE

    def restart(file):
        global world
        world= []
        with open(file, 'r' , encoding = 'utf8')as f:
            for line in f.read().splitlines():
                world.append(list(line))
        return world

    global file
    while True:
        screen.fill((0, 0 ,0))
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
                elif event.key == pygame.K_r:
                    restart(file)     
                elif event.key == pygame.K_e:
                    if file == "level1.txt":
                        file = "level2.txt"
                        restart(file) 
                    elif file == "level2.txt":
                        file = "level3.txt"
                        restart(file)
                    elif file == "level3.txt":
                        pass
                elif event.key == pygame.K_w:
                    if file == "level2.txt":
                        file = "level1.txt"
                        restart(file) 
                    elif file == "level3.txt":
                        file = "level2.txt"
                        restart(file)
                    elif file == "level1.txt":
                        pass
                    
        drawWorld(screen) ## COMMENTO ABRAHAM: lo avevi messo all'esterno del while
            


main()





