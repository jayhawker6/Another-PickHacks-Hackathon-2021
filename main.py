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
# Pygame Paramaters #
bg = pygame.image.load("./Resources/Assets/feild.png")
#winfill = pygame.image.load("./Resources/Assets/field.png")
image = pygame.Surface((32, 32))
image.fill((255, 255, 100))

pygame.init()

###START HERE###

#window where the game occurs
winSize = winx, winy = 480, 480
window = pygame.display.set_mode((winSize))
tractor = pygame.image.load("./Resources/Assets/Tractor.png")
hay = pygame.image.load("./Resources/Assets/hay.png")
# CASH MANAGMENT #
loanSize = random.random()
cash = 0.00
playArea = pygame.Rect((0, 0), (winSize))
collect = pygame.Rect(
    (random.randint(32, (winx - 32)), random.randint(32,
                                                     (winx - 32))), (32, 32))
rect = pygame.Rect((0, 0), (32, 32))
isLoan = False
collection = 0
interestRate = 0.00
cursor
# GAME PROGRESS #

dlc = 0


#loans
def loan(loanSize):
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
    cash -= (loanSize * interestRate)
    if not (interestRate == 0):
        interestRate += 0.01


def posColl():
	global collection
	collect.left = random.randint(0, (winx - 32))
	collect.top = random.randint(0, (winy - 32))
	collection += 1
	if collect.top > winy - collect.height:
	    collect.top = winy - collect.height
	if collect.top < 0:
	    collect.top = 0
	if collect.left > winx - collect.width:
	    collect.left = winx - collect.width
	if collect.left < 0:
	    collect.left = 0 
	print(collect.top)
	print(collect.left)	

def moveXY(xDirect, yDirect):
    for x in range(0, 10):
        rect.move_ip(xDirect, yDirect)
        pygame.time.wait(1)
    if rect.top > winy - rect.height:
        rect.top = winy - rect.height
    if rect.top < 0:
        rect.top = 0
    if rect.left > winx - rect.width:
        rect.left = winx - rect.width
    if rect.left < 0:
        rect.left = 0


def payment(pay):
    global cash
    cash += pay


def jobZero():

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveXY(0, -3)
            elif event.key == pygame.K_s:
                moveXY(0, 3)
            elif event.key == pygame.K_a:
                moveXY(-3, 0)
            elif event.key == pygame.K_d:
                moveXY(3, 0)
        if rect.colliderect(collect):
            posColl()
            print(collection)
        if collection > 9:
            break

        window.blit(bg, playArea)
        window.blit(tractor, rect)
        window.blit(hay, collect)


def jobOne():
    collection = 0
    jobZero()
    payment(10)


def drawCirc(a):
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        pygame.draw.circle(20, 220, 15+a,30,30,30)
        a +=1
    if pressed[pygame.K_DOWN]:
        a -=1
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)


def jobTwo():
	moves = 0
	drawCirc(moves)	
	if moves > 9:
		payment(5)
	else:
	    jobTwo()
	if moves < 0:
	    print("You have failed at this job, try another one")
	    return False


def jobThree():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveXY(0, -3)
            elif event.key == pygame.K_RIGHT:
                moveXY(0, 3)
        if rect.colliderect(collect):
            posColl()
            print(collection)
        if collection > 9:
            break

        window.blit(bg, playArea)
        window.blit(tractor, rect)
        window.blit(hay, collect)


def workJob():
    interest()
    job = 0  #random.randint(0, 5)
    if job == 0:
        jobZero()
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
def menu():
	pass
def getMouseCollision():
	for event in pygame.event.get():


#loops through the game
while True:
    workJob()
    #buyGame()
    pygame.display.update()
