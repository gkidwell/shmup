""" enemy.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This class is used for both enemy sprites.
    """
import pygame, random, os
# Global constants
weak = 1
strong = 2

class Enemy(pygame.sprite.Sprite):
    # Initialize the sprite off screen.
    def __init__(self,disp,enemytype):
        pygame.init()
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        # If the enemytype paremeter is 'weak,' give it an enemy type of weak, a particular image, a speed of 2.5, and 1 Hit Point.
        if enemytype == weak:
            self.enemytype = weak
            self.image = pygame.image.load(os.path.join("images", "enemy1.png"))
            self.dx = 2.5
            self.hp = 1
        # If the enemytype paremeter is 'strong,' give it an enemy type of strong, a particular image, a speed of 5, and 2 Hit Points.
        if enemytype == strong:
            self.enemytype = strong
            self.image = pygame.image.load(os.path.join("images", "enemy2.png"))
            self.dx = 5
            self.hp = 2
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        # Place it just to the right of the screen.
        self.rect.left = self.screen.get_width()
        # Place it, horizontally, in a random position.
        self.rect.centery = random.randrange(0, self.screen.get_height())
        self.moving = False

    def update(self):
        # If it is 'moving,' have it move to the left at its speed.
        if self.moving == True:
            self.rect.centerx -= self.dx
            if self.rect.right < 0:
                self.reset()
        # If its Hit Points have been depleted, have it reset.
        if self.hp == 0:
            self.reset()

    def reset(self):
        # Redraw it off screen, and reset its Hit Points
        self.rect.left = self.screen.get_width()
        self.rect.centery = random.randrange(0, self.screen.get_height())
        self.moving = False
        if self.enemytype == weak:
            self.hp = 1
        elif self.enemytype == strong:
            self.hp = 2
