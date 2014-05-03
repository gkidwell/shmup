""" scorebar.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell

    This class creates a Scorebar at the top of the screen, displaying the Protagonist's remaining Shields and Score.
    This code was heavily based on the Scoreboard class found on page 312 of the Game Programming book by Harris.
    """

import pygame

class Scorebar(pygame.sprite.Sprite):
    def __init__(self,disp):
        # Initialize the scorebar at the top of the screen, with a font size of 50, a shield count of 3, and a score of 0.
        self.screen = disp
        pygame.sprite.Sprite.__init__(self)
        self.shields = 3
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)

    def update(self):
        # Update the current shield amount and score, with a font color of Medium Spring Green.
        self.text = "Shields: %d              Score: %d" %(self.shields, self.score)
        self.image = self.font.render(self.text, 1, (0, 250, 154))
        self.rect = self.image.get_rect()
