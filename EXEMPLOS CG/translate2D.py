from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'ball_glut'
incx1 = 0.0
yy = 0.0
def main():
    ds = (600,600)
    incx = 0
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600,600)
    glutCreateWindow(name)
    #gluPerspective(45, (ds[0]/ds[1]), 0.1, 50.0)
    #glTranslatef(0.0,0.0, -5)
    
    glClearColor(0.,0.,0.5,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboardHdl)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,10,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    
    glutMainLoop()
    return

def display():
    global incx1
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glPushMatrix()
    color = [1.0,0.,0.,1.]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    
    #glMatrixMode(GL_MODELVIEW)
    #glLoadIdentity()
    glTranslatef(incx1,0,0)
    #glutSolidCube(1)
    glutSolidSphere(2,20,20)	
    #glutWireSphere(2,20,20)
    #glPopMatrix()
    glutSwapBuffers()
    return

def keyboardHdl( key, x, y):
    global incx1
    #print(str(ord(key)))
    #print(key == chr(97))
    #print(key == "a")
    if key in ('r', 'R'):
        print(key)
    if(key == chr(97)):
        incx1 = incx1 - 1.0
        print(str(incx1))        
    if(key == chr(100)):
        incx1 = incx1 + 1.0
        print(str(incx1))
    return    
        
if __name__ == '__main__': main()