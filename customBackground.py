""" customBackground.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This is the class to create a scrolling background.
    Because the background was so large, it was made to be a .jpg.
    """
import pygame, os

class Background(pygame.sprite.Sprite):
    # Initialize the sprite.
    def __init__(self,disp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "backgroundimage.jpg"))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.dx = 10
        self.reset()

    # Constantly have the sprite move to the left.
    # If the right side of the image moves beyond the right side of the screen, reset the image.
    def update(self):
        self.rect.left -= self.dx
        if self.rect.right <= 800:
            self.reset()

    # Reset the image's left side to the left side of the screen.
    def reset(self):
        self.rect.left = 0
