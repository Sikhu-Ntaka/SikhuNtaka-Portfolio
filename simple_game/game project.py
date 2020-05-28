# This is a game with a single player and three enemy objects, the goal of the
# game is to avoid collision with enemy objects, in additon there is a prize
# object, if player collides with prize object, player wins, if player collides
# with enemy object, player loses game

import pygame as py # Import game library as and recall it as shorthand, py
import random       # Import random number generator

# Ininitialize pygame modules

py.init()

# Set the screen width and height

screen_width = 1040
screen_height = 680
screen = py.display.set_mode((screen_width, screen_height))

# This creates the player, the three enemy objects and the prize object
# and attaches imgages to them

player = py.image.load("player.jpg")
enemy1 = py.image.load("enemy.png")
enemy2 = py.image.load("enemy2.png")
enemy3 = py.image.load("monster.jpg")
prize = py.image.load("prize.jpg")

# This gets the height and width of all the respective images used, this is to be
# used to ensure the players/enemies don't move beyond the screen boundaries

player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(player_height))
print("This is the width of the player image: " +str(player_width))

# Set the initial position of player and all the enemies as variables 

playerXPosition = 100
playerYPosition = 50

# Make the three enemy and the prize start off at random different positions
# off the screen

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

prizeXPosition = screen_width
prizeYPosition = random.randint(0, screen_height - prize_height)

# Checks if the key up, down, left or right key is pressed. It is initialized
# as boolean variable False as it is currently not pressed.

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# This is the loop structure of the game

while 1:    # This loop will loop over the code below unit the user/player quits

    screen.fill(0)                                                      # Clears the screen
    screen.blit( player, (playerXPosition, playerYPosition))            # Draws player image to screen at specified point
    screen.blit(enemy1, (int(enemy1XPosition), int(enemy1YPosition)))
    screen.blit(enemy2, (int(enemy2XPosition), int(enemy2YPosition)))
    screen.blit(enemy3, (int(enemy3XPosition), int(enemy3YPosition)))
    screen.blit(prize, (int(prizeXPosition), int(prizeYPosition)))

    py.display.flip()           # Updates the screen

    # This event checks if the user has quit the program and exits program
    for event in py.event.get():

        if event.type == py.QUIT:
            py.quit()
            exit(0)
    # This event checks if the user has pressed a key down (i.e, if it is pressed
    # by the user.

        if event.type == py.KEYDOWN:

            # Test if is the key wanted using boolean variable defined earlier
            # K_UP, K_DOWN, K_LEFT, K_RIGHT are all keyboard constants
            # representing up, down, left and right arrows
            
            if event.key == py.K_UP:
                keyUp = True
            if event.key == py.K_DOWN:
                keyDown = True
            if event.key == py.K_RIGHT:
                keyRight = True
            if event.key == py.K_LEFT:
                keyLeft = True

    # This checks if the keys are up (not pressed down) and if the key released
    # is the one intended

        if event.type == py.KEYUP:

            if event.key == py.K_UP:
                keyUP = False
            if event.key == py.K_DOWN:
                keyDown = False
            if event.key == py.K_RIGHT:
                keyRight = False
            if event.key == py.K_LEFT:
                keyLeft = False

    # The co-ordinate system is defined such that (0, 0) is at the top left hand
    # corner, the player moves right and down for positive x and y

    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1     
    

    # This block of code ensures that the player does not move out of the screen by
    # restricting movement based on x and y co-ordinates and the size of the player
    # image
            
    if keyLeft == True:
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition += 1

    # In order to check for collision of the enemies/prize with the player.
    # bounding boxes around the images are defined, which track movement of image
    # Used to test if player/enemies/prize collide with each other
    # If they do then there is a collision.       
            
    playerBox = py.Rect(player.get_rect())            

    # The position of the player is trackd by the following

    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    # Set boundaries for enemies and prize

    enemy1Box = py.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = int(enemy1XPosition)
    
    enemy2Box = py.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = int(enemy2XPosition)
    
    enemy3Box = py.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = int(enemy3XPosition)
    
    prizeBox = py.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = int(prizeXPosition)

    # Testing collision of the boxes, if player collides with any of the enemies
    # player loses the game

    if playerBox.colliderect(enemy1Box):

        print("You lose!")

        py.quit()
        exit(0)
        
    if playerBox.colliderect(enemy2Box):

        print("You lose!")

        py.quit()
        exit(0)

        
    if playerBox.colliderect(enemy3Box):
        print("You lose!")

        py.quit()
        exit(0)
        
    if playerBox.colliderect(prizeBox):

        print("You win!")

        py.quit()
        exit(0)

    # If the enemy icons move out of the screen the player wins
    
    if enemy1XPosition < 0 - enemy1_width:

        print("You win!")

        py.quit()
        exit(0)

    if enemy2XPosition < 0 - enemy2_width:

        print("You win!")

        py.quit()
        exit(0)
    if enemy3XPosition < 0 - enemy3_width:

        print("You win!")

        py.quit()
        exit(0)
# This  defines the movement of the enemies across the screen

    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.05
    enemy3XPosition -= 0.20
    prizeXPosition  -= 0.01

        

   














