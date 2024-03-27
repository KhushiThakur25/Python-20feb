import pygame
import random
pygame.init()

screenWidth = 1000
screenHeight = 500

size = screenWidth ,screenHeight

screen = pygame.display.set_mode(size)
white = 255,255,255
yellow = 255,255,0
w,h = 50,50
bg = pygame.image.load('bgg.png')

frogImg = pygame.image.load('frog1.png')
frogWidth = frogImg.get_width()
frogHeight = frogImg.get_height()

def homeScreen():
    font = pygame.font.SysFont(None,100)
    text = font.render("Welcome to the jungle",True,yellow)

    font_2 = pygame.font.SysFont(None,70)
    text_2 = font_2.render("Press SPACE to start the game",True,white)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE  :
                    game()
        screen.blit(bg,(0,0))
        screen.blit(text,(100,100))
        screen.blit(text_2,(50,300))
        pygame.display.update()

def score(counter):
    font = pygame.font.SysFont(None,50)
    text = font.render(f"Score:{counter}",True,yellow)
    screen.blit(text,(100,10))


def gameOver():
    font = pygame.font.SysFont(None,200)
    text = font.render("Game Over..",True,yellow)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(text,(100,100))
        pygame.display.update()



def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,white,[snakeList[i][0],snakeList[i][1],w,h])

def game():
    move_x = 0
    move_y = 0
    speed = 2
    x,y = 0,0
    counter = 0
    
    snakeLength = 1

    snakeList = []
    frogX = random.randint(1,screenWidth-frogWidth)
    frogY = random.randint(1,screenHeight-frogHeight)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x += speed
                    move_y = 0
                elif event.key == pygame.K_LEFT:
                    move_x -= speed
                    move_y = 0
                elif event.key == pygame.K_UP:
                    move_y -= speed
                    move_x = 0
                elif event.key == pygame.K_DOWN:
                    move_y += speed
                    move_x = 0

     
        

        screen.blit(bg,(0,0))
        screen.blit(frogImg,(frogX,frogY))
        score(counter)
        frogRect = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
        snakeRect = pygame.draw.rect(screen,white,[x,y,w,h])
        x += move_x
        y += move_y

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)
        drawSnake(snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        if x > screenWidth:
            x = -w
        elif x < -w:
            x = screenWidth
        elif y > screenHeight:
            y = -h
        elif y < -h:
            y = screenHeight

        if snakeRect.colliderect(frogRect):
            frogX = random.randint(1,screenWidth-frogWidth)
            frogY = random.randint(1,screenHeight-frogHeight)
            snakeLength += 40
            counter += 1


        for i in snakeList[:-1]:
            if i == snakeList[-1]:
                gameOver()

        pygame.display.flip()

homeScreen()