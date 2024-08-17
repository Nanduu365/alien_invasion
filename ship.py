import pygame
from pygame.sprite import Sprite

class Ship (Sprite):
    ''' A class to manage the ship'''
    def __init__(self, ai):
        '''Initialize the ship and set its starting position'''
        super().__init__()
        
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.settings = ai.settings

        #load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)


        #Movement flag
        self.move_right = False
        self.move_left = False

    def update(self):
        '''Update the ship's position based on the movement flag'''
        #Update the ship's x value, not the rect.
        if self.move_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.move_left and (self.rect.left > self.screen_rect.left):
            self.x -= self.settings.ship_speed
        
        #Update rect object from self.x
        self.rect.x = self.x   

    def center_ship(self):
        '''Center the ship on the screen'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def fullscreen_update(self,ai):
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()
        self.settings = ai.settings

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draw the ship at its current location'''
        self.screen.blit(self.image, self.rect)





