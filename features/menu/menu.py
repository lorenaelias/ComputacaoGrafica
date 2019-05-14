import pygame

from features.graphic_primitives.primitives import linha, retangulo, quadrado, circulo, curvabotao
from features.gui import screen, menuButtons, bucketImg
from utils import color, dimen


def menu_inicialization():
    global colorNum
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(0, 0, dimen.width, 100))  # Menu cinza principal

    aux = (dimen.width // 30)
    pygame.draw.rect(screen, color.terciaryColor,
                     pygame.Rect((dimen.width // 30), (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.green,
                     pygame.Rect((dimen.width // 30), (dimen.width // 30) + 50, 50, 5))  # Botao Linha
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (aux + 50)))
    draw_icon(0)

    aux = (dimen.width // 30) + 100
    pygame.draw.rect(screen, color.secondaryColor,
                     pygame.Rect((dimen.width // 30) + 100, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))
    draw_icon(1)

    aux = (dimen.width // 30) + 200
    pygame.draw.rect(screen, color.secondaryColor,
                     pygame.Rect((dimen.width // 30) + 200, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))
    draw_icon(2)

    aux = (dimen.width // 30) + 300
    pygame.draw.rect(screen, color.secondaryColor,
                     pygame.Rect((dimen.width // 30) + 300, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))
    draw_icon(3)

    aux = (dimen.width // 30) + 400
    pygame.draw.rect(screen, color.secondaryColor,
                     pygame.Rect((dimen.width // 30) + 400, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))
    draw_icon(4)

    aux = (dimen.width // 30) + 500
    pygame.draw.rect(screen, color.secondaryColor,
                     pygame.Rect((dimen.width // 30) + 500, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))
    draw_icon(5)

    aux = (dimen.width // 30) + 600
    pygame.draw.rect(screen, color.secondaryColor,
                     pygame.Rect((dimen.width // 30) + 600, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))
    draw_icon(6)

    aux = (dimen.width // 30) + 700
    pygame.draw.rect(screen, color.colorList[colorNum],
                     pygame.Rect((dimen.width // 30) + 700, (dimen.width // 30), 50, 50))  # Botao Externo Linha
    menuButtons.append((aux, (dimen.width // 30), (aux + 50), (dimen.width // 30) + 50))


def draw_icon(primitive):
    if primitive == 0:
        linha(40, 70, 70, 40, color.black, True)
    if primitive == 1:
        retangulo(134, 40, 176, 70, color.black, True)
    if primitive == 2:
        quadrado(242, 42, 270, 70, color.black, True)
    if primitive == 3:
        circulo(355, 55, 15, color.black, True)
    if primitive == 4:
        linha(440, 70, 450, 40, color.black, True)
        linha(450, 40, 460, 70, color.black, True)
        linha(460, 70, 470, 40, color.black, True)
    if primitive == 5:
        curvabotao((535, 35), (550, 60), (575, 75), color.black)
    if primitive == 6:
        screen.blit(bucketImg, (630, 30))
