shmup
=====

Python sidescrolling shoot 'em up game, written using pygame

project2.py
Bridgewater State University
COMP 399 Fall 09 - Project 2
Author: Glen Kidwell
Assignment:
Create a sidescrolling shoot 'em up video game.

To run the game, open 'project2.py' with Python 2.6.	


Controls
========

To move your ship up and down, press and hold the up and down keys respectively.
To fire a laser at enemy ships, press the space key. (Only one may be on screen at a time.)
When the game has ended, press R to Restart the game.

Your ship begins with 3 shields. After the 3 are depleted, one hit will kill you.
Enemy lasers, as well as collisions with enemy ships, will damage your ship.

Each time you hit an enemy, you gain 100 points.
The weak enemies will sometimes drop a Bonus Gem.
If you collect this Gem, you get 1000 points.

You are able to destroy enemy lasers with your laser, but it can be difficult.


The protagonist is a green spaceship, which fires green lasers.
The enemies are UFOs (1 Hit Point) and Rockets (2 Hit Points). They fire red lasers.
When hit (if you have shields), a light blue shield briefly appears.


Method
======

I created a scrolling background, using a panoramic image.

I created a scorebar at the top to indicate shields and score.

Most sprites, except for the background, scorebar, and protagonist, are drawn off screen and moved for use later.

I then created the protagonist spaceship. When the up and down keys are pressed, it moves up and down (and the image changes appropriately). When the space key is pressed, it fires a green laser to the right.

I then created the enemy sprite class, which can be used to create one of two enemy types. One has one hit point and travels slowly to the left. One has two hit points and travels faster to the left. Both will randomly fire red lasers to the left. There vertical position is randomly chosen. If you destroy the enemies with your laser, you gain points, and both the laser and enemy disappear. If you destroy an enemy laser with your laser, you gain no points and both lasers disappear.

When the weaker enemy is destroyed, it will randomly drop a bonus item, which increases points when collected.

When you are hit by an enemy laser or enemy, your shield count goes down. When your three shields are depleted, you can be hit once more. After that, the game ends.

When the game ends, the background cotinues to scroll and scorebar is displayed, but everything else is removed. The R key can now be used to restart the game.
