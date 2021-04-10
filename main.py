import pygame

###START HERE###
pygame.init()
window = pygame.display.set_mode((400,400))
while 1:
  x,y = pygame.mouse.get_pos()
  left, right = pygame.mouse.get_pressed()
  
  pygame.draw.rect(window,(255, 255, 100),((x - 100),(y - 100),(x + 25),(y+25)))

  if left:
    x = y
    
  pygame.display.update()

