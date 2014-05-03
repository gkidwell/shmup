""" project2.py
    COMP 399 Fall 09 - Project 2
    Author: Glen Kidwell
    Assignment:
    Create a sidescrolling shoot 'em up video game.

    Controls:
    To move your ship up and down, press and hold the up and down keys respectively.
    To fire a laser at enemy ships, press the space key. (Only one may be on screen at a time.)
    When the game has ended, press R to Restart the game.

    Your ship begins with 3 shields. After the 3 are depleted, one hit will kill you.
    Enemy lasers, as well as collisions with enemy ships, will damage your ship.

    Each time you hit an enemy, you gain 100 points.
    The weak enemies will sometimes drop a Bonus Gem.
    If you collect this Gem, you get 1000 points.

    You are able to destroy enemy lasers with your laser, but it can be difficult.
    """

import pygame, random, os
# Import the other sprite classes for the game.
import shield, scorebar, spaceship, laser, customBackground, enemy, bonusItem
# These are global variables that will be constants.
good = weak = 1
bad = strong = 2

def main():
    # Initialize pygame and the window display.
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("COMP 399 Project 2 - Glen Kidwell")

    # Fill in a background color.
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255,255,255))
    screen.blit(background, (0,0))

    # Initialize instants of all sprites.
    backgroundSprite = customBackground.Background(screen)
    protagonist = spaceship.Spaceship(screen)
    protLaser1 = laser.Laser(screen, good)
    enemyLaser1 = laser.Laser(screen, bad)
    enemyLaser2 = laser.Laser(screen, bad)
    weakEnemy = enemy.Enemy(screen, weak)
    strongEnemy = enemy.Enemy(screen, strong)
    bonus = bonusItem.BonusItem(screen)
    gameScorebar = scorebar.Scorebar(screen)
    shield1 = shield.Shield(screen)
    # Create useful sprite groups.
    goodSprites = pygame.sprite.Group(protagonist, protLaser1)
    badSprites = pygame.sprite.Group(weakEnemy, strongEnemy, enemyLaser1, enemyLaser2)
    backgroundSprites = pygame.sprite.Group(backgroundSprite, gameScorebar)
    allSprites = pygame.sprite.Group(protagonist, protLaser1, enemyLaser1, enemyLaser2, weakEnemy, strongEnemy, bonus, gameScorebar, shield1)

    # Initialize the sound files.
    playerdie = pygame.mixer.Sound(os.path.join("sounds", "playerdie.ogg"))
    enemyhurt = pygame.mixer.Sound(os.path.join("sounds", "enemyhurt.ogg"))
    enemydie = pygame.mixer.Sound(os.path.join("sounds", "enemydie.ogg"))
    shielddeflect = pygame.mixer.Sound(os.path.join("sounds", "shielddeflect.ogg"))
    playerlaser = pygame.mixer.Sound(os.path.join("sounds", "playerlaser.ogg"))
    enemylaser = pygame.mixer.Sound(os.path.join("sounds", "enemylaser.ogg"))
    bonusnoise = pygame.mixer.Sound(os.path.join("sounds", "bonusnoise.ogg"))

    clock = pygame.time.Clock()
    keepGoing = True
    gameOver = False
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            # Cause the game to quit.
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                # Used to make protagonist move up on screen.
                if event.key == pygame.K_UP:
                    protagonist.upKey = True
                # Used to make protagonist move down on screen.
                elif event.key == pygame.K_DOWN:
                    protagonist.downKey = True
                # Used to make protagonist fire a laser.
                elif event.key == pygame.K_SPACE:
                    if protLaser1.moving == False:
                        playerlaser.play()
                        protLaser1.spaceKey = True
                        protLaser1.rect.left = protagonist.rect.right
                        protLaser1.rect.centery = protagonist.rect.centery
            elif event.type == pygame.KEYUP:
                # These allow the user to constantly move up, or down, if the appropriate key is held.
                if protagonist.upKey == True:
                    protagonist.upKey = False
                if protagonist.downKey == True:
                    protagonist.downKey = False

        # If the protagonist touches the bonus item, points are added to the score and a sound is played.
        if protagonist.rect.colliderect(bonus.rect):
            bonusnoise.play()
            gameScorebar.score += 1000
            bonus.reset()
            
        # If the protagonist touches enemy lasers or enemy sprites
        # protagonist's shields decrease,
        # a shield is displayed in protagonist's position briefly, and
        # a sound plays.
        if pygame.sprite.spritecollideany(protagonist, badSprites):
            shield1.hit = True
            shield1.currentx = protagonist.rect.centerx
            shield1.currenty = protagonist.rect.centery
            shielddeflect.play()
            gameScorebar.shields -=1
            # Enemy lasers are destroyed if touched.
            if protagonist.rect.colliderect(enemyLaser1.rect):
                enemyLaser1.reset()
            if protagonist.rect.colliderect(enemyLaser2.rect):
                enemyLaser2.reset()
            # Enemy sprites are destroyed if touched.
            if protagonist.rect.colliderect(weakEnemy.rect):
                weakEnemy.reset()
            if protagonist.rect.colliderect(strongEnemy.rect):
                strongEnemy.reset()

        # If the protagonist's laser touches enemy lasers or enemy sprites, the protagonist's laser is destroyed.
        if pygame.sprite.spritecollideany(protLaser1, badSprites):
            # If the collision is with a weak enemy, the enemy is destroyed, a sound is played, and points are added.
            if protLaser1.rect.colliderect(weakEnemy.rect):
                # There is a 1/10 chance that, upon destroying a weak enemy, it will drop a Bonus Item.
                if random.randrange(1, 10) == 1:
                    if bonus.moving == False:
                        bonus.rect.centerx = weakEnemy.rect.centerx
                        bonus.rect.centery = weakEnemy.rect.centery
                        bonus.moving = True
                weakEnemy.hp -= 1
                enemydie.play()
                gameScorebar.score += 100
            # If the collision is with a strong enemy, the enemy's hp is decreased, a sound is played, and points are added.
            if protLaser1.rect.colliderect(strongEnemy.rect):
                strongEnemy.hp -= 1
                if strongEnemy.hp == 0:
                    enemydie.play()
                else:
                    enemyhurt.play()
                gameScorebar.score += 100
            # If the colllision is with an enemy laser, the enemy laser is destroyed.
            if protLaser1.rect.colliderect(enemyLaser1.rect):
                enemyLaser1.reset()
            if protLaser1.rect.colliderect(enemyLaser2.rect):
                enemyLaser2.reset()
            protLaser1.reset()

        # If the protagonist's shields are decreased to less than zero, a sound is played and the game ends.
        if gameScorebar.shields < 0:
            gameScorebar.shields = 0
            playerdie.play()
            protagonist.rect.centerx = 1000
            shield1.rect.centerx = 1000
            protagonist.kill()
            shield1.kill()
            keepGoing = False
            gameOver = True

        # This causes a random number to be generated.
        # There is a 1/10 chance that, if a Weak Enemy isn't already on screen, one will appear on the far end of the screen.
        enemyappear = random.randrange(1, 20)
        if enemyappear == 1 or enemyappear == 2:
            weakEnemy.moving = True
        # There is a 1/20 chance that, if a Strong Enemy isn't already on screen, one will appear on the far end of the screen.
        elif enemyappear == 3:
            strongEnemy.moving = True
        # This makes it so that, for example, immediately upon destroying a weak enemy,
        # a second weak enemy does not always instantly appear on the far end of the screen.

        # This causes a random number to be generated.
        enemyattack = random.randrange(1, 25)
        # If a weak enemy is on screen and doesn't have a laser firing,
        # there is a 1/25 chance that it will fire a laser.
        if enemyattack == weak:
            if weakEnemy.moving == True:
                if enemyLaser1.moving == False:
                    enemylaser.play()
                    enemyLaser1.rect.right = weakEnemy.rect.left
                    enemyLaser1.rect.centery = weakEnemy.rect.centery
                    enemyLaser1.moving = True
        # If a strong enemy is on screen and doesn't have a laser firing,
        # there is a 1/25 chance that it will fire a laser.
        elif enemyattack == strong:
            if strongEnemy.moving == True:
                if enemyLaser2.moving == False:
                    enemylaser.play()
                    enemyLaser2.rect.right = strongEnemy.rect.left
                    enemyLaser2.rect.centery = strongEnemy.rect.centery
                    enemyLaser2.moving = True
        # This makes it so that the enemies are not ceaselessly firing,
        # but are firing often enough to be challenging.

        # The sprites are cleared, updated, and drawn to the screen again.
        backgroundSprites.clear(screen, background)
        allSprites.clear(screen, background)
        backgroundSprites.update()
        allSprites.update()
        backgroundSprites.draw(screen)
        allSprites.draw(screen)
        pygame.display.flip()

    # When the loop is exited (game has ended), the sprites (except for the background and scorebar) are removed.        
    allSprites.clear(screen, background)
    while gameOver == True:
        clock.tick(30)
        # The background continues to scroll.
        backgroundSprites.update()
        backgroundSprites.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            # The user is able to quit.
            if event.type == pygame.QUIT:
                gameOver = False
            # The user is able to restart the game by pressing the R key.
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    keepGoing = True
                    gameOver = False
                    main()
    # Python 2.6 seems to need this to get the window to close
    pygame.quit()
    
if __name__ == "__main__":
    main()
