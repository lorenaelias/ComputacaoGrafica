import numpy
import pygame

screen_size = (800, 600)

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Variaveis de estilo
background = white
foreground = black

pygame.init()
screen = pygame.display.set_mode(screen_size)
layer = pygame.surface.Surface(screen_size)
layer.blit(screen, (0, 0))

pygame.display.set_caption('Trabalho computacao grafica')
screen.fill(background)
layer.fill(white)
pygame.display.flip()


def _linhaH(x0, y0, x1, y1, color, menu):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2 * dy - dx
    y = y0
    for x in range(dx):
        if(menu == True):
            screen.set_at((x + x0, y), color)
        else:
            if(y > 100):       # tentativa para nao desenhar linha no menu a nao ser que seja no icone
                screen.set_at((x + x0, y), color)
        if D > 0:
            y = y + yi
            D = D - 2 * dx
        D = D + 2 * dy


def _linhaV(x0, y0, x1, y1, color, menu):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x0
    for y in range(dy):
        if (menu == True):
            screen.set_at((x, y + y0), color)
        else:
            if (y + y0 > 100):      # tentativa para nao desenhar linha no menu a nao ser que seja no icone
                screen.set_at((x, y + y0), color)
        if D > 0:
            x = x + xi
            D = D - 2 * dy
        D = D + 2 * dx


def testalinha(x0, y0, x1, y1, color, menu):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            _linhaH(x1, y1, x0, y0, color, menu)
        else:
            _linhaH(x0, y0, x1, y1, color, menu)
    else:
        if y0 > y1:
            _linhaV(x1, y1, x0, y0, color, menu)
        else:
            _linhaV(x0, y0, x1, y1, color, menu)


def linha(x0, y0, x1, y1, color, menu):
    testalinha(x0, y0, x1, y1, color, menu)
    pygame.display.flip()

def circulo(x0, y0, r, color, menu):
    x = 0
    y = r
    d = 1 - r
    circuloAux(x, y, x0, y0, color, menu)
    while y > x:
        if d < 0:
            d = d + (2 * x) + 3
        else:
            d = d + 2 * (x - y) + 5
            y = y - 1
        x = x + 1
        circuloAux(x, y, x0, y0, color, menu)
    pygame.display.flip()


def circuloAux(x, y, x0, y0, color, menu):
    if(menu == True):
        screen.set_at((x + x0, y + y0), color)
        screen.set_at((x0 - y, x + y0), color)
        screen.set_at((x0 - y, y0 - x), color)
        screen.set_at((x0 - x, y0 - y), color)
        screen.set_at((x0 - x, y + y0), color)
        screen.set_at((x + x0, y0 - y), color)
        screen.set_at((y + x0, y0 - x), color)
        screen.set_at((y + x0, x + y0), color)
    else:
        if(y+y0 > 100):
            screen.set_at((x + x0, y + y0), color)
        if(x+y0 > 100):
            screen.set_at((x0 - y, x + y0), color)
        if(y0-x > 100):
            screen.set_at((x0 - y, y0 - x), color)
        if(y0-y > 100):
            screen.set_at((x0 - x, y0 - y), color)
        if(y+y0 > 100):
            screen.set_at((x0 - x, y + y0), color)
        if(y0-y > 100):
            screen.set_at((x + x0, y0 - y), color)
        if(y0-x > 100):
            screen.set_at((y + x0, y0 - x), color)
        if(x+y0 > 100):
            screen.set_at((y + x0, x + y0), color)


def retangulo(x, y, w, h, color, menu):
    testalinha(x, y, w, y, color,menu)
    testalinha(w, y, w, h, color,menu)
    testalinha(w, h, x, h, color,menu)
    testalinha(x, h, x, y, color,menu)
    pygame.display.flip()


def quadrado(x, y, w, h, color,menu):
    testalinha(x, y, w, y, color,menu)
    testalinha(w, y, w, h, color,menu)
    testalinha(w, h, x, h, color,menu)
    testalinha(x, h, x, y, color,menu)
    pygame.display.flip()

def bezierIngenuo(p1, p4, cor):
    defaultBack = screen.copy()
    while 1:
        for e in pygame.event.get():

            if (e.type == pygame.MOUSEBUTTONDOWN):
                # screen.blit(defaultBack, (0, 0), (0, 0, 900, 100))
                screen.blit(defaultBack, (0, 0))
                aux = pygame.mouse.get_pressed()

                if aux[2] == 1:  # clique com o botao direito para sair
                    print("ACABOU DE FAZER A CURVAAAA")
                    screen.blit(teste, (0, 0))

                    return
                else:
                    p3 = pygame.mouse.get_pos()
                    for t in numpy.arange(0, 1, 0.0001):
                        omt = 1 - t
                        omt2 = omt * omt
                        omt3 = omt2 * omt
                        t2 = t * t
                        t3 = t2 * t
                        x = omt3 * p1[0] + ((3 * omt2) * t * p1[0]) + (3 * omt * t2 * p3[0]) + t3 * p4[0]
                        y = omt3 * p1[1] + ((3 * omt2) * t * p1[1]) + (3 * omt * t2 * p3[1]) + t3 * p4[1]
                        x = int(numpy.floor(x))
                        y = int(numpy.floor(y))
                        if (y > 100):
                            screen.set_at((x, y), cor)
                    pygame.display.flip()
                    teste = screen.copy()

def curvabotao(p1,p2,p3,color):
    for t in numpy.arange(0,1,0.001):
        omt  = 1-t
        omt2 = omt*omt
        omt3 = omt2*omt
        t2   = t*t
        t3   = t2*t
        x    = omt3 * p1[0] + ((3*omt2)*t*p1[0]) + (3*omt*t2*p2[0]) +t3*p3[0]
        y    = omt3 * p1[1] + ((3*omt2)*t*p1[1]) + (3*omt*t2*p2[1]) +t3*p3[1]
        x    = int(numpy.floor(x))
        y    = int(numpy.floor(y))
        screen.set_at((x,y), color)
    pygame.display.flip()
