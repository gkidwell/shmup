""" laser.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This class is used for both the protagonist's and enemies' lasers.
    """
import pygame, os
# Global constants.
good = 1
bad = 2

class Laser(pygame.sprite.Sprite):
    # Initialize the sprite off screen.
    def __init__(self,disp,affiliation):
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        # If the affiliation parameter is 'good,' make it a green laser with a speed to the right of 25.
        if affiliation == good:
            self.image = pygame.image.load(os.path.join("images", "greenlaser.png"))
            self.dx = 25
        # If the affiliation parameter is 'bad,' make it a red laser with a speed to the left of 15.
        elif affiliation == bad:
            self.image = pygame.image.load(os.path.join("images", "redlaser.png"))
            self.dx = -15
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = -100
        self.rect.centery = -100
        self.spaceKey = False
        self.moving = False
        self.affiliation = affiliation

    def update(self):
        # This prevents the user from firing more than one laser at once.
        if self.spaceKey == True:
            self.moving = True
            self.spaceKey = False

        # If the laser is 'moving,' have it move at its speed.
        # If it moves beyond the respective sides of the screen, have it reset.
        if self.moving == True:
            self.rect.centerx += self.dx
            if self.affiliation == good:
                if self.rect.left > self.screen.get_width():
                    self.reset()
            elif self.affiliation == bad:
                if self.rect.right < 0:
                    self.reset()

    def reset(self):
        # Redraw the sprite off screen.
        self.rect.centerx = -100
        self.moving = False
