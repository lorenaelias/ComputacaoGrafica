#incompleto terminar com base no algoritmo do caderno

import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))
screen.fill((0,0,0))
pygame.display.flip()

white=(255,255,255)

#Esta funcao funciona apenas 
#para o primeiro quadrante
def midpointcircle(radius):
	
	#carrega no fb o pixel (x1,y1)
	screen.set_at((x1,y1),white)
	#computa os deltas necessarios
	dx    = x2 - x1
	dy    = y2 - y1
	dy2   = 2*dy
	dydx2 = dy2 - 2*dx
	pant  = dy2 - dx
	x = x1
	y = y1
	
	for i in range(dx):
		if pant < 0:
			screen.set_at((x+1,y),white)
			pant = pant + dy2 
		else:
			screen.set_at((x+1,y+1),white)
			pant = pant + dydx2
			y += 1;
		x += 1;
	pygame.display.flip()

def showEightQuadrants(x, y):
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	screen.set_at((x,y),white)
	
	
	
bresenham(10,10,50,50)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()