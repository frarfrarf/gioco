
#non sono sicura che funzioni perchè per qualche motivo non mi va pygame, non assicuro nulla,se ci sono problrmi dillo 
#anch se non potendolo eseguire non saprei come risolverli

import pygame, sys
from pygame.locals import *

class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image= image
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.base_color, self.hovering_color = base_color, self.hovering_color
        self.text_input=text_input
        self.text=self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image=self.text
        self.rect=self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.test_rect= self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.botton):
            return True
        return False
    
    def changeColor(self,position):
         if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.botton):
             self.text= self.font.render(self.text_input, True, self.hovering_color)
         else:
             self.text= self.font.render(self.text_input, True, self.base_color)


def livello1():
    pygame.display.set_caption("Livello 1")

    while True:
        LIVELLO1_MOUSE_POS= pygame.mouse.get_pos()

        SCREEN.fill("black")

        #questa dovrebbe essere la schermayta per il primo livello quindi ora agiiungo il bottone per tornare indietro, 
        # per il resto colleghiamo succesivamente il livello?
        LIVELLO1_BACK = Button(image=None, pos=(640, 460),
                               text_input="TORNA INDIETRO", font= get_font(75), base_color="White", hovering_color="Green" )
        
        LIVELLO1_BACK.changeColor(LIVELLO1_MOUSE_POS)
        LIVELLO1_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LIVELLO1_BACK.checkForInput(LIVELLO1_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def livello2():
    pygame.display.set_caption("Livello 2")

    while True:
        LIVELLO2_MOUSE_POS= pygame.mouse.get_pos()

        SCREEN.fill("black")

        #questa dovrebbe essere la schermayta per il secondo livello quindi ora agiiungo il bottone per tornare indietro, 
        # per il resto colleghiamo succesivamente il livello?
        LIVELLO2_BACK = Button(image=None, pos=(640, 460),
                               text_input="TORNA INDIETRO", font= get_font(75), base_color="White", hovering_color="Green" )
        
        LIVELLO2_BACK.changeColor(LIVELLO2_MOUSE_POS)
        LIVELLO2_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LIVELLO2_BACK.checkForInput(LIVELLO2_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

def livello3():
    pygame.display.set_caption("Livello 3")

    while True:
        LIVELLO3_MOUSE_POS= pygame.mouse.get_pos()

        SCREEN.fill("black")

        #questa dovrebbe essere la schermayta per il terzo livello quindi ora agiiungo il bottone per tornare indietro, 
        # per il resto colleghiamo succesivamente il livello?
        LIVELLO3_BACK = Button(image=None, pos=(640, 460),
                               text_input="TORNA INDIETRO", font= get_font(75), base_color="White", hovering_color="Green" )
        
        LIVELLO3_BACK.changeColor(LIVELLO3_MOUSE_POS)
        LIVELLO3_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LIVELLO3_BACK.checkForInput(LIVELLO3_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()

def main_menu():

    pygame.display.set_caption("menu")

    while True:
        SCREEN.blit(BG, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU",True, "b68f40")
        MENU_RECT = MENU_TEXT.get_rect (center= (640, 100))

        LIVELLO1_BUTTON= Button(image=pygame.image.load("assets/LIVELLO1 rect.png"), pos=(640,250),
                                text_input="LIVELLO 1", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        LIVELLO2_BUTTON= Button(image=pygame.image.load("assets/LIVELLO2 rect.png"), pos=(640,400),
                                text_input="LIVELLO 2", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        LIVELLO3_BUTTON= Button(image=pygame.image.load("assets/LIVELLO1 rect.png"), pos=(640,550),
                                text_input="LIVELLO 3", font=get_font(75), base_color="#d7fcd4", hovering_color="white")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [LIVELLO1_BUTTON, LIVELLO2_BUTTON, LIVELLO3_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LIVELLO1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    livello1()
                if LIVELLO2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    livello2()
                if LIVELLO3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    livello3()
                
        pygame.display.update()
        
main_menu()        


