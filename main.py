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

###START HERE###
pygame.init()
window = pygame.display.set_mode((400, 400))
dlc = 0

def workJob():
	job = random.randint(0, 4)
	
	pass

def buyGame():
    if not (dlc > 0):
        pygame.draw.rect(window, (255, 255, 100), (100, 100, 25, 15))
    else:
        #run next funtion
        pass


while True:
    buyGame()
    x, y = 100, 100
    left = pygame.mouse.get_pressed()
    if left:
        x += 5
    pygame.display.update()