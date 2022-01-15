import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

offsetx = 0.0
offsety = 0.0

def drawOneLine(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def init():
    glClearColor(0.0, 0.0, 0.7, 0.0)
    glShadeModel(GL_FLAT)

def display():
  glClear(GL_COLOR_BUFFER_BIT)
  
  glColor(1.0, 0.0, 0.0) 
  
  glLineWidth(5.0)
  
  glMatrixMode(GL_MODELVIEW)
  glLoadIdentity()
  glTranslatef(offsetx,offsety,0.0)
  
  drawOneLine (0.0,0.0,100.0,100.0)
  drawOneLine (0.0,50.0,100.0,150.0)
  
  glFlush ()
  return 
  
def keyboard(key, x, y):
  global offsetx
  global offsety
  global rotx
  global roty
  #print(str(ord(key)))
  if ord(key) == 97:#'a'  
    offsetx = offsetx -1.0
  if ord(key) == 100:#'d'  
    offsetx = offsetx + 1.0
  if ord(key) == 119: #'w' 
    offsety = 1.0
  if ord(key) == 115:#'s'  
    offsety = -1.0
    
  glutPostRedisplay() 
    
def reshape(w, h):
  glViewport(0, 0, w, h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  gluOrtho2D(0.0, w, 0.0, h)
  
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(400, 400)
glutInitWindowPosition(100, 100)
glutCreateWindow('Lines')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()