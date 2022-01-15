import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((50,50))
screen.fill((255,255,255))

screen.set_at((10,10),(255,0,0))
screen.set_at((20,20),(0,255,0))
screen.set_at((20,10),(0,0,255))
pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()