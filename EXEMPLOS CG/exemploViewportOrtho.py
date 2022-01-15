import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

offsetx = 0.0
offsety = 0.0
wid = 600
hei = 600

def drawAxis(offset):
    glColor3f(1.0, 1.0, 0)
    glBegin(GL_LINES)
    glVertex2f(-wid,0+offset)
    glVertex2f(wid,0+offset)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0+offset,-hei)
    glVertex2f(0+offset,hei)
    glEnd()
    glColor3f(1.0, 0.0, 0.0)
    
def drawPicture():
    glBegin(GL_QUADS)
    glVertex2f(-100, -100)
    glVertex2f( 100, -100)
    glVertex2f( 100,  100)
    glVertex2f(-100,  100)
    glEnd()
	
    #glBegin(GL_QUADS)
    #glVertex2f(   0, 0)
    #glVertex2f( 100, 0)
    #glVertex2f( 100, 100)
    #glVertex2f(   0, 100)
    #glEnd()
    
    #glBegin(GL_QUADS)
    #glVertex2f(100, 100)
    #glVertex2f(200, 100)
    #glVertex2f(200, 200)
    #glVertex2f(100, 200)
    #glEnd()
    
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
  drawAxis(2)
  #glPopMatrix()  
  
  glFlush ()
def keyboard(key, x, y):
  global wid
  global hei

  if ord(key) == 49:#'1'  
    glViewport(0, 0, wid, hei)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, wid, 0.0, hei)
    glutPostRedisplay()
  if ord(key) == 50:#'2' 
    glViewport(0, 0, wid, hei)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-wid/2, wid/2, -hei/2, hei/2)
    glutPostRedisplay()
  if ord(key) == 51: #'3'
    glViewport(0, 0, int(2*wid), int(2*hei))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0, wid, 0.0, hei)
    glutPostRedisplay()
  if ord(key) == 52:#'4' 
    glViewport(0, 0, wid//2, hei//2)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-wid/2, wid/2, -hei/2, hei/2)
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