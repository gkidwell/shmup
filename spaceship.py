""" spaceship.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This class creates the spaceship sprite, used as the Protagonist in the sidescroller.
    """
import pygame, os

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,disp):
        # Initialize the sprite, 75 pixels to the right of the left edge, and 300 pixels down from the top edge.
        pygame.init()
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "ship.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = 75
        self.rect.centery = 300
        self.dx = 30
        self.dy = 30
        self.upKey = False
        self.downKey = False

    def update(self):
        # When the Up and Down keys are pressed (and held), the sprite moves in the appropriate direction.
        # It will not go beyond the top and bottom of the screen.
        if self.upKey == True:
            # While moving up, the image changes.
            self.image = pygame.image.load(os.path.join("images", "shipbankup.png"))
            self.rect.centery -= self.dy
            if self.rect.top < 0:
                self.rect.top = 0
        elif self.downKey == True:
            # While moving down, the image changes.
            self.image = pygame.image.load(os.path.join("images", "shipbankdown.png"))
            self.rect.centery += self.dy
            if self.rect.bottom > self.screen.get_height():
                self.rect.bottom = self.screen.get_height()
        # While not moving up or down, be certain that it is the default image.
        elif self.image != pygame.image.load(os.path.join("images", "ship.png")):
            self.image = pygame.image.load(os.path.join("images", "ship.png"))
