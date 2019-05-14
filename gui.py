import sys
import math
import pygame

from features.primitives import linha, retangulo, quadrado, circulo, bezierIngenuo, curvabotao
from utils import color, dimen

bucketImg = pygame.transform.scale(pygame.image.load('res/bucket.png'), (50, 50))
iconImg = pygame.transform.scale(pygame.image.load('res/icon.png'), (32, 32))

# initialize pygame
pygame.init()
screen = pygame.display.set_mode(dimen.screen_size)
screen.fill(color.white)
pygame.display.set_icon(iconImg)
colorNum = 0

# control variables
mousePosition = (0, 0)
menuButtons = []
primitiveNum = 0


def menu_init():
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


# faz o botao ficar verde quando for selecionado
def muda_botao(pos):
    global primitiveNum
    global colorNum
    print(pos)
    a = -1

    for i in range(len(menuButtons)):
        if pos[0] >= menuButtons[i][0] and pos[0] <= menuButtons[i][2] and pos[1] >= menuButtons[i][1] and pos[1] <= \
                menuButtons[i][3]:
            a = i
            if i != 7:
                primitiveNum = i

    if a == 7:
        colorNum += 1
        if colorNum == len(color.colorList):
            colorNum = 0
        aux = (dimen.width // 30) + 700
        pygame.draw.rect(screen, color.colorList[colorNum],
                         pygame.Rect((dimen.width // 30) + 700, (dimen.width // 30), 50, 50))  # Botao Externo Linha

    elif a != -1:
        for i in range(len(menuButtons) - 1):
            aux = menuButtons[i][0]
            if a == i:
                pygame.draw.rect(screen, color.terciaryColor,
                                 pygame.Rect(menuButtons[i][0], menuButtons[i][1], 50, 50))  # Botao Externo Linha
                draw_icon(i)
                screen.blit(bucketImg, (630, 30))
                pygame.draw.rect(screen, color.green, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))
            else:
                pygame.draw.rect(screen, color.secondaryColor,
                                 pygame.Rect(menuButtons[i][0], menuButtons[i][1], 50, 50))  # Botao Externo Linha
                draw_icon(i)
                screen.blit(bucketImg, (630, 30))
                pygame.draw.rect(screen, color.primaryColor, pygame.Rect(aux, (dimen.width // 30) + 50, 50, 5))

    pygame.display.update()


def desenha_linha(pos):
    defaultBack = screen.copy()
    while 1:
        for e in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            screen.blit(defaultBack, (0, 0))
            linha(pos[0], pos[1], x, y, color.colorList[colorNum], False)
            screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
            if (e.type == pygame.MOUSEBUTTONUP):
                return


def desenha_retangulo(pos):
    defaultBack = screen.copy()
    while 1:
        for e in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            screen.blit(defaultBack, (0, 0))
            retangulo(pos[0], pos[1], x, y, color.colorList[colorNum], False)
            screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
            if (e.type == pygame.MOUSEBUTTONUP):
                return


def desenha_quadrado(pos):
    defaultBack = screen.copy()
    while 1:
        for e in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            screen.blit(defaultBack, (0, 0))

            ## S é uma variavel que controla o desenho do quadrado quando invertemos o lado do desenho
            s = abs(y - pos[1]) // (y - pos[1]) if y != pos[1] else 1
            if (x < pos[0]):
                s *= -1
            quadrado(pos[0], pos[1], x, pos[1] + ((x - pos[0]) * s), color.colorList[colorNum], False)
            screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
            if (e.type == pygame.MOUSEBUTTONUP):
                return


def desenha_circulo(pos):
    defaultBack = screen.copy()

    while 1:
        for e in pygame.event.get():
            x, y = pygame.mouse.get_pos()
            screen.blit(defaultBack, (0, 0))
            raio = int(math.sqrt(((x - pos[0]) ** 2) + ((y - pos[1]) ** 2)))
            circulo(pos[0], pos[1], raio, color.colorList[colorNum], False)
            screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
            if (e.type == pygame.MOUSEBUTTONUP):
                return


def desenha_polilinha():
    while 1:
        for e in pygame.event.get():
            if (e.type == pygame.MOUSEBUTTONDOWN):
                poli_aux(pygame.mouse.get_pos())
                return


def poli_aux(pos):
    defaultBack = screen.copy()
    while 1:
        for e in pygame.event.get():

            x, y = pygame.mouse.get_pos()
            screen.blit(defaultBack, (0, 0))
            linha(pos[0], pos[1], x, y, color.colorList[colorNum], False)
            screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
            if (e.type == pygame.MOUSEBUTTONDOWN):
                pygame.display.update()
                defaultBack = screen.copy()
                pos = (x, y)
                aux = pygame.mouse.get_pressed()
                if aux[2] == 1:
                    return


# implementar como o floodFill sera chamado
def preenche(pos):
    defaultBack = screen.copy()
    while 1:
        for e in pygame.event.get():
            screen.blit(defaultBack, (0, 0))
            if pos[1] > 100:
                flood_Fill(screen, pos[0], pos[1], color.colorList[colorNum])
            screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
            if e.type == pygame.MOUSEBUTTONUP:
                return


# replaces all points of same starting colour,
# with a new colour, up to a border with
# different starting colour
def flood_Fill(surface, x, y, newColor):
    pilha = [(x, y)]
    corOriginal = surface.get_at((x, y))  # cor de fundo original

    while len(pilha) > 0:
        x, y = pilha.pop()

        if surface.get_at((x, y)) != corOriginal:
            continue
        print("(", x, ",", y, ")")
        surface.set_at((x, y), newColor)
        if (x + 1) <= 899:
            pilha.append((x + 1, y))  # poe o pixel da direita na pilha para ser preenchido
        if (x - 1) >= 0:
            pilha.append((x - 1, y))  # poe o pixel da esquerda na pilha para ser preenchido
        if (y + 1) <= 599:
            pilha.append((x, y + 1))  # poe o pixel de baixo na pilha para ser preenchido
        if (y - 1) >= 100:
            pilha.append((x, y - 1))  # poe o pixel de cima na pilha para ser preenchido


def desenha_curva():
    sig = True
    while sig:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                sig = False
                break

    while 1:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                pos2 = pygame.mouse.get_pos()
                bezierIngenuo(pos, pos2, color.colorList[colorNum])
                return
    pygame.display.flip()


def click_handle(pos):
    if pos[1] <= 100:
        muda_botao(pos)
    elif primitiveNum == 4:
        poli_aux(pos)
    if primitiveNum == 0:
        desenha_linha(pos)
    if primitiveNum == 1:
        desenha_retangulo(pos)
    if primitiveNum == 2:
        desenha_quadrado(pos)
    if primitiveNum == 3:
        desenha_circulo(pos)
    if primitiveNum == 5:
        desenha_curva()
    if primitiveNum == 6:
        preenche(pos)


def borracha(pos):
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                screen.set_at((pos[0], pos[1]), color.white)
                return


menu_init()
print(menuButtons)
linha(0, 100, 900, 100, color.primaryColor,
      True)  # essa linha é importante pra nao deixar a coloração vazar quando a figura não está totalmente
# contida na tela de desenho

while 1:
    defaultMenu = pygame.Surface(dimen.screen_size)

    mousePosition = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_handle(mousePosition)

    pygame.display.update()
