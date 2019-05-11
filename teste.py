import pygame, sys

# inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((900, 600))
screen.fill([255, 255, 255])

# cores
white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
black = [0, 0, 0]
listaCores = [black, red, blue, green, white, (128, 0, 128), (255, 20, 147), (255, 255, 0), (0, 255, 255),
              (255, 0, 255), (128, 128, 128), (210, 105, 30), (56, 176, 222), (1, 250, 42), (255, 215, 0),
              (180, 82, 205)]
MenuColor = [200, 200, 200]
colorNum = 1

def floodFill(x, y):
    screen.set_at((x,y), listaCores[colorNum])
    if (screen.get_at((x, y - 1)) == white and y > 0):
        floodFill(x, y - 1)
    if (screen.get_at((x + 1, y)) == white and x < 900):
        floodFill(x + 1, y)
    if (screen.get_at((x,y+1)) == white and y < 600):
        floodFill(x, y + 1)
    if (screen.get_at((x - 1, y)) == white and x > 0):
        floodFill(x - 1, y)

def desenha_circulo(pos):
    deafultBack = screen.copy()
    screen.blit(deafultBack, (0, 0))
    pygame.draw.circle(screen, black, (pos[0], pos[1]), 30, 2)
    floodFill(pos[0],pos[1])
    screen.blit(deafultBack, (0, 0), (0, 0, 900, 100))

def click_handle(pos):
    desenha_circulo(pos)

while 1:

    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_on = True
            click_handle(mousePos)

    pygame.display.update()