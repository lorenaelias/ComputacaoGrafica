import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

offsetx = 0.0
offsety = 0.0
pontos = []
btDown = False

def drawPoints():
    glBegin(GL_POINTS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    
    for p in pontos:
        glVertex2f(p[0],p[1])
    
    glEnd()

def init():
    glClearColor(0.0, 0.0, 0.7, 0.0)
    glShadeModel(GL_FLAT)

def display():
  glClear(GL_COLOR_BUFFER_BIT)
  
  glColor3f(1.0, 0.0, 0.0) 
  
  #desenha as primitivas e aplica as transformacoes
  
  glPointSize(5)
  glEnable(GL_POINT_SMOOTH)
  drawPoints()
 
  
  glFlush ()
def keyboard(key, x, y):
  glTranslatef(150.0 ,150.0,0.0)
  glRotatef(45,0,0,1)
  glTranslatef(-150.0 ,-150.0,0.0)
  glutPostRedisplay()
  return
    
def reshape(w, h):
  glViewport(0, 0, w, h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0.0, w, 0.0, h)

def mouseHdl(button, state, x, y):
    global btDown
    
    print(str(x)+','+str(y))
    if (button == GLUT_LEFT_BUTTON) and (state == GLUT_DOWN):
    #if (button == GLUT_LEFT_BUTTON):
    #if (state == GLUT_DOWN):
        #pontos.append((x,y))
        pontos.append((x,600-y))
        glutPostRedisplay()
        btDown = True
    else:
        btDown = False
        
def mouseMotionHdl(x, y):  
    global btDown
    
    if btDown:
        pontos.append((x,600-y))
        glutPostRedisplay()
    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow('Lines')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouseHdl)
glutMotionFunc(mouseMotionHdl);
glutMainLoop()




