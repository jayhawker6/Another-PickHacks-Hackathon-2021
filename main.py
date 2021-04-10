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
bg = pygame.image.load("./Resources/Assets/field.png")
winfill = pygame.image.load("./Resources/Assets/field.png")
image = pygame.Surface((569, 320))
image.fill((255, 255, 100))

pygame.init()

###START HERE###
prompt = pygame.Rect((0,0), (0,0))
prompt = pygame.image.load("./Resources/Assets/Tractor.png")
#window where the game occurs
winSize = winx, winy = 640, 480
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
selected = 0
prompt = pygame.Rect((0, 0), (64, 32))
# GAME PROGRESS #
 
img1 = pygame.image.load("./Resources/Buttons/b1.png")
img2 = pygame.image.load("./Resources/Buttons/b3.png")
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

'''
def moveCollect(xDir, yDir):
    for x in range(0, 10):
        collect.move_ip(xDir, yDir)
        pygame.time.wait(1)
    if collect.top > winy - rect.height:
        collect.top = winy - rect.height
    if collect.top < 0:
        collect.top = 0
    if collect.left > winx - rect.width:
        collect.left = winx - rect.width
    if collect.left < 0:
        collect.left = 0

'''
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
        pygame.draw.circle(20, 220, 15 + a, 30, 30, 30)
        a += 1
    if pressed[pygame.K_DOWN]:
        a -= 1
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

''''

def jobThree():
    col = 0
    x, y = 0,0
    pressed = pygame.key.get_pressed()
    
    while col > 9:
        moveXY(x,y)
        x +=cursor.top
        y +=cursor.bottom

        if pressed[pygame.K_UP]:
            moveCollect(0,3)
        if pressed[pygame.K_DOWN]:
            moveCollect(0,-3)
        if pressed[pygame.K_LEFT]:
            moveCollect(-3,0)
        if pressed[pygame.K_RIGHT]:
            moveCollect(3,0)

        if rect.colliderect(collect):
            postColl()
            col +=1

    pay(5)    
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)


def jobFour():
    col = 9
    x, y = 0,0
    pressed = pygame.key.get_pressed()
    
    while col < 2:
        moveXY(x,y)
        x +=cursor.top
        y +=cursor.bottom

        if pressed[pygame.K_UP]:
            moveCollect(0,3)
        if pressed[pygame.K_DOWN]:
            moveCollect(0,-3)
        if pressed[pygame.K_LEFT]:
            moveCollect(-3,0)
        if pressed[pygame.K_RIGHT]:
            moveCollect(3,0)

        if rect.colliderect(collect):
            postColl()
            col +=1
        else:
            col -=1
    pay(10)    
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)

def jobFive():
    col = 0
    x, y = 0,0
    pressed = pygame.key.get_pressed()
    
    while col < 9:
        moveXY(x,y)
        x +=cursor.top
        y +=cursor.bottom

        if pressed[pygame.K_UP]:
            moveCollect(0,3)
        if pressed[pygame.K_DOWN]:
            moveCollect(0,-3)
        if pressed[pygame.K_LEFT]:
            moveCollect(-3,0)
        if pressed[pygame.K_RIGHT]:
            moveCollect(3,0)

        if rect.colliderect(collect):
            postColl()
            col +=1

    pay(10)    
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)

'''


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
def promptSize(width, height, path):
	global prompt, prompt
	pos = ((285-(width/2)), (160-(height)))
	prompt = pygame.image.load(path)
	prompt = pygame.Rect(pos, ((width,height)))
	

def menu():
	global prompt, prompt
	gameWin = pygame.Rect((0, 0), (569, 320))
	if dlc < 1:
		promptSize(128, 64, "./Resources/Buttons/p3.png")

	    #prompt 1
	elif dlc < 2:
	    promptSize(2, 2, "./Resources/Buttons/p2.png")
		#prompt 2
	elif dlc < 3:
	    promptSize(2, 2, "./Resources/Buttons/p3.png")
		#prompt 3
	elif dlc < 4:
	    promptSize(2, 2, "./Resources/Buttons/p4.png")
		#prompt 4
	elif dlc < 5:
		promptSize(2, 2, "./Resources/Buttons/p5.png")
	else:
		#execute 'Main Game' code here
		pass
	button1 = pygame.Rect(((winx-66),20), (62, 20))

	button2 = pygame.Rect(((winx-50),50), (46, 20))
	window.blit(image, gameWin)
	window.blit(prompt, prompt)
	window.blit(img1, button1)
	window.blit(img2, button2)
	
#prompt 5



def selection():
    global selected
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if selected > 0:
                    selected -= 1
            elif event.key == pygame.K_d:
                if selected < 2:
                    selected += 1


#loops through the game
while True:
	menu()
    #workJob()
    #buyGame()
	pygame.display.update()
