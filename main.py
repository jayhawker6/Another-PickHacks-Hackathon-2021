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
# Pygame Paramaters #
bg = pygame.image.load("./Resources/Assets/field.png")
winfill = pygame.image.load("./Resources/Assets/field.png")
image = pygame.image.load("./Resources/Assets/CircBorder.png")

cantGiveCredit = False
pygame.init()
pygame.mixer.init()
pygame.font.init()
###START HERE###
promptBack = pygame.Rect((0, 0), (0, 0))
prompt = pygame.image.load("./Resources/Assets/Tractor.png")
prompt1 = pygame.image.load("./Resources/Buttons/p3.png")
promptButton = pygame.Rect((0, 0), (0, 0))
#window where the game occurs
# should we make window size smaller, the loan and job buttons are
# barely visible
winSize = winx, winy = 640, 480
window = pygame.display.set_mode((winSize))
tractor = pygame.image.load("./Resources/Assets/Tractor.png")
hay = pygame.image.load("./Resources/Assets/hay.png")
# CASH MANAGMENT #
loanS = 0
moves = 0
cash = 99999999990.00
playArea = pygame.Rect((0, 0), (winSize))
collect = pygame.Rect(
    (random.randint(32, (480 - 32)), random.randint(32, (480 - 32))), (32, 32))
col1 = 10
col2 = 0
rect = pygame.Rect((0, 0), (32, 32))
bankAccount = pygame.Rect((0, 380), (32, 32))
interest = 0.25
myfont = pygame.font.SysFont(None, 32)
netWorth = myfont.render("Balance: $%s, Debt: $%s" % (cash, loanS), 1,
                         (255, 255, 0))
isLoan = False
isJob = False
collection = 0
interestRate = 0.00
selected = 0
screenCollect = 0
promptBack = pygame.Rect((0, 0), (64, 32))
# GAME PROGRESS #
button1 = pygame.Rect(((winx - 66), 20), (62, 20))
button2 = pygame.Rect(((winx - 50), 50), (46, 20))
button3 = pygame.Rect(((winx - 66), 20), (0, 0))
tutorial = pygame.Rect((20, 270), (0, 0))
img1 = pygame.image.load("./Resources/Buttons/b1.png")
img2 = pygame.image.load("./Resources/Buttons/b3.png")
img3 = pygame.image.load("./Resources/Buttons/b2.png")
img4 = pygame.image.load("./Resources/Buttons/p5.png")
img5 = pygame.image.load("./Resources/Buttons/p6.png")
dlc = 0
dlcPrice = 20
curse = pygame.Rect((0, 0), (1, 1))
job = 0
showPrompt = False
ball = pygame.Rect((0, 0), (128, 128))


def iDontEvenKnowAnyMore():
    window.fill((0, 0, 0))
    gameWin = pygame.Rect((0, 0), (569, 320))
    button1 = pygame.Rect(((winx - 66), 20), (62, 20))
    button2 = pygame.Rect(((winx - 50), 50), (46, 20))
    netWorth = myfont.render(
        """Balance: $%s, Debt: $%s, DLC: #%s %s""" %
        (cash, loanS, dlc, showPrompt), 1, (255, 255, 0))
    window.blit(image, gameWin)
    window.blit(img1, button1)
    window.blit(img2, button2)
    window.blit(netWorth, bankAccount)


def startButton():
    global button3
    pos = ((285 - (64 / 2)), (160 - (20 / 2)))
    button3 = pygame.Rect(pos, (62, 20))
    window.blit(img3, button3)


def menu():
    global prompt, promptBack, prompt1, promptButton, button1, button2, job, showBall
    if isJob:
        job = random.randint(0,3)
        workJob()
    elif cantGiveCredit:
        pos = ((285 - (64 / 2)), (160 - (64 / 2)))
        prompt = pygame.image.load("./Resources/Buttons/p4.png")
        promptBack = pygame.Rect(pos, ((64, 64)))
        promptButton.y = -420
        iDontEvenKnowAnyMore()
        window.blit(prompt, promptBack)
    elif dlc < 1:
        iDontEvenKnowAnyMore()
        promptSize(128, 64)
#prompt 1
    elif dlc < 2:
        iDontEvenKnowAnyMore()
        startButton()
        promptButton.y = -420
        if showPrompt:
            promptSize(128, 64)


#prompt 2
    elif dlc < 3:
        iDontEvenKnowAnyMore()
        startButton()
        promptButton.y = -420
        if showBall:
            showBall()
            window.blit(img4, ball)
        if showPrompt:
            promptSize(128, 64)
    else:
        iDontEvenKnowAnyMore()
        startButton()
        promptButton.y = -420
        if showBall:
            moveBall()
            window.blit(img4, ball)
        window.blit(img5, tutorial)


def morshu():
    global cantGiveCredit
    cantGiveCredit = True


def showBall():
    global showBall, ball
    pos = ((285 - (128 / 2)), (160 - (180 / 2)))
    ball = pygame.Rect((pos), (128, 128))
    window.blit(img4, ball)


def buyDLC():
    global cash, dlc, showPrompt
    if dlcPrice <= cash:
        cash -= dlcPrice
        dlc += 1
        showPrompt = False
    else:
        morshu()


def moveBall():
    global ball
    for event in pygame.event.get():
        ball.move_ip(0, 5)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                ball.move_ip(0, -50)


def startGame():
    global dlcPrice
    if dlc < 3:
        dlcPrice = 110
    else:
        showBall()


def onClick():
    global curse, dlcPrice, button1, button2, button3, isJob, cantGiveCredit, showPrompt, cash, ball
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            curse.x, curse.y = pygame.mouse.get_pos()
            if curse.colliderect(promptButton):
                buyDLC()
            elif curse.colliderect(button2):
                isJob = True
                cantGiveCredit = False
            elif curse.colliderect(button1):
                loan((random.randint(100, 10000)) / 100)
            elif curse.colliderect(button3):
                if dlc < 2:
                    dlcPrice = 50
                    showPrompt = True
                else:
                    startGame()
            elif curse.colliderect(ball):
                showPrompt = True

        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_9:
        #        cash += 10000


#loans
def loan(loanSize):
    global isLoan, interestRate, cash
    if isLoan == True:
        print('Loan Denied')
    else:
        global cash, interestRate, loanS
        cash += loanSize
        loanS = loanSize * interestRate
        isLoan = True
        print("loan Accepted")
        interestRate = 0.25


def interest():
    global cash, interestRate, loanS
    cash -= (loanS)
    if not (interestRate == 0):
        interestRate += 0.10


def posColl():
    global collection
    collect.left = random.randint(0, (480 - 32))
    collect.top = random.randint(0, (480 - 32))
    collection += 1
    if collect.top > 480 - collect.height:
        collect.top = 480 - collect.height
    if collect.top < 0:
        collect.top = 0
    if collect.left > 480 - collect.width:
        collect.left = 480 - collect.width
    if collect.left < 0:
        collect.left = 0
    print(collect.top)
    print(collect.left)


def moveXY(xDirect, yDirect, hitBox):
	for x in range(0, 10):
	    hitBox.move_ip(xDirect, yDirect)
	    pygame.time.wait(1)
	if hitBox.top > 480 - hitBox.height:
	    hitBox.top = 480 - hitBox.height
	if hitBox.top < 0:
	    hitBox.top = 0
	if hitBox.left > 480 - hitBox.width:
	    hitBox.left = 480 - hitBox.width
	if hitBox.left < 0:
	    hitBox.left = 0

def moveCollect(xDirect, yDirect):
	xFact = xDirect
	yFact = yDirect
	for x in range(0,10):	
		collect.move_ip(xFact, yFact)
		pygame.time.wait(1)
	if collect.top > 480 - collect.height:
		collect.top = 480 - collect.height
		yFact = -yFact
		collect.move_ip(xFact, yFact)
	if collect.top < 0:
		collect.top = 0
		yFact = -yFact
		collect.move_ip(xFact, yFact)
	if collect.left > 480 - collect.width:
		collect.left = 480 - collect.width
		xFact = -xFact
		collect.move_ip(xFact, yFact)
	if collect.left < 0:
		collect.left = 0
		xFact = -xFact
		collect.move_ip(xFact, yFact)
	#print(yFact)


def payment(pay):
    global cash
    cash += pay


def jobZero():
    global isJob, collection
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveXY(0, -5, rect)
            elif event.key == pygame.K_s:
                moveXY(0, 5, rect)
            elif event.key == pygame.K_a:
                moveXY(-5, 0, rect)
            elif event.key == pygame.K_d:
                moveXY(5, 0, rect)
        if rect.colliderect(collect):
            posColl()
            print(collection)
        if collection > 9:
            payment(10)
            collection = 0
            isJob = False
        window.blit(bg, playArea)
        window.blit(tractor, rect)
        window.blit(hay, collect)


def jobOne():
    global isJob, collection
    collection = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveXY(0, -3, collect)
            elif event.key == pygame.K_s:
                moveXY(0, 3, collect)
            elif event.key == pygame.K_a:
                moveXY(-3, 0, collect)
            elif event.key == pygame.K_d:
                moveXY(3, 0, collect)
        if rect.colliderect(rect):
            posColl()
            print(collection)
        if collection > 2:
            payment(10)
            collection = 0
            isJob = False
        window.blit(bg, playArea)
        window.blit(tractor, rect)
        window.blit(hay, collect)

	
def jobTwo():
	global isJob, col1
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moveXY(0, 3, rect)
			elif event.key == pygame.K_DOWN:
				moveXY(0, -3, rect)
			elif event.key == pygame.K_LEFT:
				moveXY(-3, 0, rect)
			elif event.key == pygame.K_RIGHT:
				moveXY(3, 0, rect)
		if rect.colliderect(collect):
			col1 -= 1
		elif collect.top > 480 - collect.height:
			col1 +=1
		elif collect.top < 0:
			col1 +=1
		elif collect.left > 480 - collect.width:
			col1 +=1
		elif collect.left < 0:
			col1 +=1	
		if col1 > 20:
			payment(10)
			isJob = False
		elif col1 < 1:
			print("You failed to pass the game! Sorry, buy one of our dlc tickets to play again")
			isJob = False
		window.blit(bg, playArea)
		window.blit(tractor, rect)
		window.blit(hay, collect)
		moveCollect(-2,-2)


def jobThree():
	global isJob, col2
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				moveXY(0, 3, rect)
			elif event.key == pygame.K_DOWN:
				moveXY(0, -3, rect)
			elif event.key == pygame.K_LEFT:
				moveXY(-3, 0, rect)
			elif event.key == pygame.K_RIGHT:
				moveXY(3, 0, rect)
		if rect.colliderect(collect):
			col2 += 1

		if col2 > 10:
			payment(5)
			isJob = False
		window.blit(bg, playArea)
		window.blit(tractor, rect)
		window.blit(hay, collect)
		moveCollect(-3,-3)
	

'''
def jobFour():
    global isJob
    col = 9
    x, y = 0, 0
    pressed = pygame.key.get_pressed()
    while col < 2:
        moveXY(x, y, rect)
        x += 4
        y += 4
        if pressed[pygame.K_UP]:
            moveXY(0, 3, collect)
        elif pressed[pygame.K_DOWN]:
            moveXY(0, -3, collect)
        elif pressed[pygame.K_LEFT]:
            moveXY(-3, 0, collect)
        elif pressed[pygame.K_RIGHT]:
            moveXY(3, 0, collect)
        elif rect.colliderect(collect):
            col += 1
        elif col > 15:
            print("You have failed to complete this job")
            isJob = False
        else:
            col -= 1
        window.blit(bg, playArea)
        window.blit(tractor, rect)
        window.blit(hay, collect)
    if col < 2:
        payment(10)
        isJob = False


def jobFive():
    global isJob, screenCollect
    x, y = 0
    screenCollect = 0
    pressed = pygame.key.get_pressed()
    while screenCollect < 20:
        moveXY(x, y, rect)
        x += 4
        y += 4
        if pressed[pygame.K_UP]:
            moveXY(0, 3)
        elif pressed[pygame.K_DOWN]:
            moveXY(0, -3)
        elif pressed[pygame.K_LEFT]:
            moveXY(-3, 0)
        elif pressed[pygame.K_RIGHT]:
            moveXY(3, 0)
        elif rect.colliderect(collect):
            screenCollect -= 1
        else:
            screenCollect += 1
        window.blit(bg, playArea)
        window.blit(tractor, rect)
        window.blit(hay, collect)
    if screenCollect == 20:
        print("Congratulations, you passed! You still lose $5")
    else:
        print("You failed, you lose $5")
    isJob = False
    payment(-5)
	'''


def workJob():
	global job
	interest()
	if job == 0:
		jobZero()
	elif job == 1:
		jobOne()
	elif job == 2:
		jobTwo()
	elif job == 3:
		jobThree()
	else:
	    quit("SOMETHING'S WRONG IN THE JOB FUNCTION STATEMENT YOU DWEEB!")


#function that allows you to start the game
#Delete Mabye
def buyGame():
    if not (dlc > 0):
        pygame.draw.rect(window, (255, 255, 100), (100, 100, 25, 15))
    else:
        #run next funtion
        pass


def promptSize(width, height):
    global prompt, promptBack, prompt1, promptButton
    pos = ((285 - (width / 2)), (160 - (height / 2)))
    posB = ((285 - (78 / 2)), (160 - (height - 40) / 2) + 16)
    prompt = pygame.image.load("./Resources/Buttons/p3.png")
    promptBack = pygame.Rect(pos, ((width, height)))
    prompt1 = pygame.image.load("./Resources/Buttons/p2.png")
    promptButton = pygame.Rect((posB), ((width, height)))
    window.blit(prompt, promptBack)
    window.blit(prompt1, promptButton)


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
    # pygame.mixer.Sound.play(pygame.mixer.Sound("./Resources/Sounds/WindowXPError.ogg"))
    onClick()
    #workJob()
    #buyGame()
    pygame.display.update()
