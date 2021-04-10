import pygame

###START HERE###
pygame.init()
window = pygame.display.set_mode((400,400))
dlc = 0

def buyGame()
while 1:
  


  x, y = 100, 100
  left = pygame.mouse.get_pressed()
  
  pygame.draw.rect(window,(255, 255, 100),((x - 100),(y - 100),(x + 25),(y+25)))

  if left:
    x += 5 


  pygame.display.update()