import sys
from pygame.locals import *

from OpenGL import *

#metodo que faz todo o trabalho
#deve chamar as rotinas do opengl para mostrar algo
def display():
    #limpa os buffers the cor e profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    #aqui vao as instrucoes de renderizacao
    #tudo aqui vai para um frame buffer (off-screen)
   

    # troca os buffers (renderizacao-apresentacao)
    glutSwapBuffers()

#rotina que inicializa o biblioteca glut (freeglut)   
glutInit(sys.argv)

# cria uma janela double-buffer RGBA
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

# Cria uma janela e define um titulo
glutCreateWindow('teste')

#"amarra" a funcao de apresentacao
glutDisplayFunc(display)

# roda a funcao principal do glut
glutMainLoop()
