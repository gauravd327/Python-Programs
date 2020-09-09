import pygame
import random

pygame.init()

win_width = 600
win_height = 400

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
running = True

# Defining x and y variables for the food and snake
snakeX = 50
snakeY = 50
sxChange = 0
syChange = 0

foodX = random.randint(51, 551)
foodY = random.randint(51, 351)

score = 0
snakeList = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        # Controls
        if keys[pygame.K_LEFT]:
            sxChange = -5
            syChange = 0

        elif keys[pygame.K_RIGHT]:
            sxChange = 5
            syChange = 0

        elif keys[pygame.K_UP]:
            sxChange = 0
            syChange = -5

        elif keys[pygame.K_DOWN]:
            sxChange = 0
            syChange = 5

    if snakeX < 0 or snakeX > win_width - 25:
        running = False

    elif snakeY < 0 or snakeY > win_height - 25:
        running = False

    win.fill((0, 0, 0))

    # Displaying the score
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render('Score: ' + str(score), True, (255, 255, 255))
    win.blit(text, (0, 0))

    
    # Drawing the food and the snake
    for x in snakeList:
        pygame.draw.rect(win, (0, 255, 0), (x[0], x[1], 20, 20))

    snake = pygame.draw.rect(win, (0, 255, 0), (snakeX, snakeY, 20, 20))
    food = pygame.draw.rect(win, (255, 0, 0), (foodX, foodY, 15, 15))

    # Checking if the snake touched the food
    eat_apple = False
    if snake.colliderect(food):
        score += 1
        eat_apple = True
        foodX = random.randint(51, 551)
        foodY = random.randint(51, 351)

    snakeList.append([snakeX, snakeY])

    # Changing the x, y co-ordinates of the snake
    snakeX += sxChange
    snakeY += syChange

    #If the snake ate an apple
    if not eat_apple:
        del snakeList[0]

    #Checking if the snake touches itself
    if len(snakeList) > 0:
        if snakeList[0] in snakeList[1:]:
            running = False

    pygame.display.update()
    clock.tick(60)

print("\nSCORE: " + str(score))
pygame.quit()