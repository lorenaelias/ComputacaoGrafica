import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

offsetx = 0.0
offsety = 0.0
    
def drawPicture():
    glBegin(GL_QUADS)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()
    
def init():
    glClearColor(0.0, 0.0, 0.7, 0.0)
    glShadeModel(GL_FLAT)

def display():
  glClear(GL_COLOR_BUFFER_BIT)
  
  glColor3f(1.0, 0.0, 0.0) 
  
  #desenha as primitivas e aplica as transformacoes
  #glLoadIdentity()
  #glPushMatrix()
  
  drawPicture()
  #glPopMatrix()  
  
  glFlush ()
def keyboard(key, x, y):
  glTranslatef(150.0 ,150.0,0.0)
  glRotatef(45,0,0,1)
  glTranslatef(-150.0 ,-150.0,0.0)
  glutPostRedisplay()
  return
    
def reshape(w, h):
  global wid
  global hei
  wid = w
  hei = h
  
  #void glViewport(GLint x,  GLint y,  GLsizei width,  GLsizei height);
  glViewport(0, 0, w, h)
  glMatrixMode(GL_PROJECTION)
  glLoadIdentity()
  
  #void gluOrtho2D(GLdouble left,  GLdouble right,  GLdouble bottom,  GLdouble top);
  gluOrtho2D(0.0, w, 0.0, h)
  #gluOrtho2D(-w/2, w/2, -h/2, h/2)
  
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow('Lines')
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()