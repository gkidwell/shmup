""" shield.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This creates a shield sprite.
    If the Protagonist has shields remaining, the shield image briefly appears where the Protagonist was when attacked.
    This indicates that the Protagonist has been attacked.
    """
import pygame, os

class Shield(pygame.sprite.Sprite):
    def __init__(self,disp):
        # Initialize the sprite off screen.
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "shield.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.currentx = -100
        self.rect.centery = self.currenty = -100
        self.hit = False
        self.delay = 0

    def update(self):
        # When the Protagonist has been 'hit,' display the shield where the Protagonist was (even if it moves away).
        # The delay is so that the shield is on screen long enough to be seen by the user.
        if self.hit == True:
            self.rect.centerx = self.currentx
            self.rect.centery = self.currenty
            self.delay += 1
            if self.delay == 3:
                self.reset()

    def reset(self):
        # Redraw the shield off screen.
        self.hit = False
        self.delay = 0
        self.rect.centerx = -100
        self.rect.centery = -100
