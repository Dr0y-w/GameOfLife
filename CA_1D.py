from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from game_of_life_ui import Ui_Dialog


class mainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.openGLWidget = self.ui.openGLWidget

    def setupui(self):
        self.openGLWidget.initializeGL()
        self.openGLWidget.resizeGL(800, 600)
        self.openGLWidget.paintGL = self.paintGL

        timer = QTimer(self)
        timer.timeout.connect(self.openGLWidget.update)
        timer.start(10)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glClearColor(0, 0, 0, 1)

        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3fv((0, 0, 0))
        glVertex3fv((1, 0, 0))
        glEnd()

        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()
        gluPerspective(45.0, 4.0 / 3.0, 1, 40)

        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()
        gluLookAt(0, 0, 4,
                  0, 0, 0,
                  0, 1, 0)



app = QApplication(sys.argv)
window = mainWindow()
window.setupui()
window.show()
sys.exit(app.exec_())
