import pygame

class Muro:
    def init(s)
class Personaggio:
    def __init__(self, screen, pos, size) -> None:
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.image = pygame.image.load('')
        self.image = pygame.transform.scale(self.image, size)
        self.vel = [0,0]

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.vel = 1
    def move_right(self):
        self.moving_right = True
    
    def stop_moving_right(self):
        self.moving_right = False

    def move_left(self):
        self.moving_left = True
    
    def stop_moving_left(self):
        self.moving_left = False

    def move_down(self):
        self.moving_down = True
    
    def stop_moving_down(self):
        self.moving_down = False

    def move_up(self):
        self.moving_up = True
    
    def stop_moving_up(self):
        self.moving_up = False
    

    def muovi(self):
        # muovi 
        if self.moving_right:
            self.rect.right += self.vel                                                 #rivedere velocità in caso di collisioni 
            # if self.rect.right > self.screen.get_width():
            #     self.rect.right = self.screen.get_width()
            if self.rect.right
        if self.moving_left:
            self.rect.left -= self.vel
            if self.rect.left < 0:
                self.rect.left = 0
        if self.moving_down:
            self.rect.down -= self.vel
            if self.rect.down < self.screen.get_height():   #da rivedere movimento up and down
                self.rect.down = self.screen.get_height()
        if self.moving_up:
            self.rect.up -= self.vel
            if self.rect.up < 0:
                self.rect.up = 0
        
        def draw(self):
            self.screen.blit(self.image, self.rect)
        