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
cash = 0.00
playArea = pygame.Rect((0, 0), (winSize))
collect = pygame.Rect(
    (random.randint(32, (480 - 32)), random.randint(32, (480 - 32))), (32, 32))
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
img1 = pygame.image.load("./Resources/Buttons/b1.png")
img2 = pygame.image.load("./Resources/Buttons/b3.png")
img3 = pygame.image.load("./Resources/Buttons/b2.png")
dlc = 0
dlcPrice = 20
curse = pygame.Rect((0, 0), (1, 1))
job = 0
showPrompt = False

#ball_game_area = pygame.Rect(())
def iDontEvenKnowAnyMore():
    window.fill((0, 0, 0))
    gameWin = pygame.Rect((0, 0), (569, 320))
    button1 = pygame.Rect(((winx - 66), 20), (62, 20))
    button2 = pygame.Rect(((winx - 50), 50), (46, 20))
    netWorth = myfont.render("""Balance: $%s, Debt: $%s""" % (cash, loanS), 1,
                             (255, 255, 0))
    window.blit(image, gameWin)
    window.blit(img1, button1)
    window.blit(img2, button2)
    window.blit(netWorth, bankAccount)


def startButton():
    pos = ((285 - (64 / 2)), (160 - (20 / 2)))
    button3 = pygame.Rect(pos, (62, 20))
    window.blit(img3, button3)


def menu():
	global prompt, promptBack, prompt1, promptButton, button1, button2, job
	if isJob:
		job = 0  #random.randint(0, 5)
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
		if showPrompt:
			promptSize(128, 64)
    #prompt 2
	elif dlc < 3:
		iDontEvenKnowAnyMore()
		startButton()

    #prompt 3
	elif dlc < 4:
		promptSize(128, 64)
		iDontEvenKnowAnyMore()
    #prompt 4
	elif dlc < 5:
		promptSize(128, 64)
		iDontEvenKnowAnyMore()
	else:
		#execute 'Main Game' code here
		pass


def morshu():
    global cantGiveCredit
    cantGiveCredit = True


def showBall():
    ball = pygame.Rect((), (128, 128))


def buyDLC():
    global cash, dlc
    if dlcPrice <= cash:
        cash -= dlcPrice
        dlc += 1
    else:
        morshu()


def startGame():
    if dlc < 3:
        dlcPrice = 110
        promptSize(127, 64)
    else:
        showBall()
    pass


def onClick():
    global curse, dlcPrice, button1, button2, button3, isJob, cantGiveCredit
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            curse.x, curse.y = pygame.mouse.get_pos()
            if curse.colliderect(promptButton):
                buyDLC()
            elif curse.colliderect(button2):
                isJob = True
                cantGiveCredit = False
            elif curse.colliderect(button1):
                loan((random.randint(1000, 100000)) / 100)
            elif curse.colliderect(button3):
                if dlc < 2:
                    dlcPrice = 50
                    promptSize(128, 64)
                else:
                    startGame()


#loans
def loan(loanSize):
    global isLoan, interest, cash
    if isLoan == True:
        print('Loan Denied')
    else:
        global cash, interestRate, loanS
        cash += loanSize
        loanS = loanSize * interestRate
        isLoan = True
        print("loan Accepted")
        interestRate = 0.1


def interest():
    global cash, interestRate, loanS
    cash -= (loanS)
    if not (interestRate == 0):
        interestRate += 0.01


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
    global screenCollect
    for x in range(0, 10):
        hitBox.move_ip(xDirect, yDirect)
        pygame.time.wait(1)
    if hitBox.top > 480 - hitBox.height:
        hitBox.top = 480 - hitBox.height
        screenCollect += 1
    if hitBox.top < 0:
        hitBox.top = 0
        screenCollect += 1
    if hitBox.left > 480 - hitBox.width:
        hitBox.left = 480 - hitBox.width
        screenCollect += 1
    if hitBox.left < 0:
        hitBox.left = 0
        screenCollect += 1


def payment(pay):
    global cash
    cash += pay


def jobZero():
    global isJob, collection
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                moveXY(0, -3, rect)
            elif event.key == pygame.K_s:
                moveXY(0, 3, rect)
            elif event.key == pygame.K_a:
                moveXY(-3, 0, rect)
            elif event.key == pygame.K_d:
                moveXY(3, 0, rect)
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
    collection = 0
    jobZero()
    payment(10)


# function that multiplies the tractors on the screen if you press #	the up key
def multiTract(a):	
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_UP]:
		window.blit(tractor, rect)
		moveXY(a,a,rect)
	if pressed[pygame.K_DOWN]:
		a -= 1
	window.blit(bg, playArea)
	window.blit(tractor, rect)
	window.blit(hay, collect)


def jobTwo():
    # control var
    moves = 1
    # multiplies the tractors on the scree
    multiTract(moves)
    # successfully completed the job
    if moves > 9:
        payment(2)
    # recursively calls the function
    else:
        jobTwo()
        # failure message

    if moves < 0:
        print("You have failed at this job, try another one")


def jobThree():
    col = 0
    x, y = 0, 0
    pressed = pygame.key.get_pressed()

    while col > 9:
        moveXY(x, y, rect)
        x += 4
        y += 4

        if pressed[pygame.K_UP]:
            moveXY(0, 3, collect)
        if pressed[pygame.K_DOWN]:
            moveXY(0, -3, collect)
        if pressed[pygame.K_LEFT]:
            moveXY(-3, 0, collect)
        if pressed[pygame.K_RIGHT]:
            moveXY(3, 0, collect)

        if rect.colliderect(collect):
            col += 1

    payment(5)
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)


def jobFour():
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
            break
            print("You have failed to complete this job")
        else:
            col -= 1
    if col < 2:
        payment(10)
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)


def jobFive():
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
        if screenCollect == 20:
            print("Congratulations, you passed! You still lose $5")
        else:
            print("You failed, you lose $5")

    payment(-5)
    window.blit(bg, playArea)
    window.blit(tractor, rect)
    window.blit(hay, collect)


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
    elif job == 4:
        jobFour()
    elif job == 5:
        jobFive()
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
