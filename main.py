#
#👋 Hi, I’m @jayhawker6
#👀 I’m interested in Python, Dart, Java, And Kotlin.
#🌱 I’m currently learning Kotlin.
#💞️ I’m looking to collaborate on My small game i've been working on, ByteBase.
#📫 You can reach me by messaging or creating bug/issue reports or pull requests.
#-And remember kids:
#
#"People who care about code effeciency are weebs.
#My code is ugly and yours can be too!"
#
#      -Ghandi
#

import pygame
import random
import time

winfill = (0, 0, 0)
image = pygame.Surface((32, 32))
image.fill((255, 255, 100))
###START HERE###
pygame.init()
window = pygame.display.set_mode((400, 400))
cash = 0.00
interestRate = 0.00
dlc = 0
rect = pygame.Rect((0, 0), (32, 32))
isLoan = False


#loans
def loan(loan):
    global isLoan, interest, cash
    if isLoan == True:
        print('Loan Denied')
    else:
        global cash, interestRate
        cash += loan
        isLoan = True
        interest = 0.05


def interest():
    global cash, interestRate
    cash -= (loan * interestRate)
    if not (interestRate == 0):
        interestRate += 0.01


def moveXY(xDirect, yDirect):
    for x in range(0, 10):
        rect.move_ip(xDirect, yDirect)


def moveBlock():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveXY(0, -1)
            elif event.key == pygame.K_s:
                moveXY(0, 1)
            elif event.key == pygame.K_a:
                moveXY(-1, 0)
            elif event.key == pygame.K_d:
                moveXY(1, 0)
        window.fill(winfill)
        window.blit(image, rect)


def workJob():
    interest()
    job = random.randint(0, 5)
    if job == 0:
        moveBlock()
    elif job == 1:
        pass
    elif job == 2:
        pass
    elif job == 3:
        pass
    elif job == 4:
        pass
    elif job == 5:
        pass
    else:
        quit("SOMETHING'S WRONG IN THE JOB FUNCTION STATEMENT YOU DWEEB!")


#function that allows you to start the game
def buyGame():
    if not (dlc > 0):
        pygame.draw.rect(window, (255, 255, 100), (100, 100, 25, 15))
    else:
        #run next funtion
        pass


#loops through the game
while True:
    workJob()
    #buyGame()
    pygame.display.update()
