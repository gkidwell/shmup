""" bonusItem.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This is the BonusItem class, for creating a Bonus Gem in the sidescrolling game.
    The item is drawn off screen, and the game later places it appropriately.
    """

import pygame, os

class BonusItem(pygame.sprite.Sprite):
    # Initialize the sprite off screen.
    def __init__(self,disp):
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "bonus.png"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 10
        self.rect.centerx = -100
        self.rect.centery = -100
        self.moving = False

    # If the sprite is 'moving,' move the sprite to the left.
    # It resets if it goes off screen again.
    def update(self):
        if self.moving == True:
            self.rect.centerx -= self.dx
            if self.rect.right < 0:
                self.reset()

    # Redraw the image off screen, not moving.
    def reset(self):
        self.rect.centerx = -100
        self.rect.centery = -100
        self.moving = False
