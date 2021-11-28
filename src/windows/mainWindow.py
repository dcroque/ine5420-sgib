import sys
from datetime import datetime
from typing import List, Union
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from structs import Line, Point, Wireframe, DisplayFile
from viewPortOperation import viewPortTransform
from windows.newWireframe import Ui_NewWireframe
from windows.transformationWindow import Ui_TransformationWindow
import defaultConfig as default

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowdmKYeC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupNavigation = QGroupBox(self.centralwidget)
        self.groupNavigation.setObjectName(u"groupNavigation")
        self.groupNavigation.setGeometry(QRect(0, 300, 171, 291))
        self.navButtonUp = QPushButton(self.groupNavigation)
        self.navButtonUp.setObjectName(u"navButtonUp")
        self.navButtonUp.setGeometry(QRect(60, 40, 51, 31))
        self.navButtonDown = QPushButton(self.groupNavigation)
        self.navButtonDown.setObjectName(u"navButtonDown")
        self.navButtonDown.setGeometry(QRect(60, 70, 51, 31))
        self.navButtonLeft = QPushButton(self.groupNavigation)
        self.navButtonLeft.setObjectName(u"navButtonLeft")
        self.navButtonLeft.setGeometry(QRect(10, 50, 51, 41))
        self.navButtonRight = QPushButton(self.groupNavigation)
        self.navButtonRight.setObjectName(u"navButtonRight")
        self.navButtonRight.setGeometry(QRect(110, 50, 51, 41))
        self.navButtonOut = QPushButton(self.groupNavigation)
        self.navButtonOut.setObjectName(u"navButtonOut")
        self.navButtonOut.setGeometry(QRect(120, 100, 31, 21))
        self.navButtonIn = QPushButton(self.groupNavigation)
        self.navButtonIn.setObjectName(u"navButtonIn")
        self.navButtonIn.setGeometry(QRect(20, 100, 31, 21))
        self.navButtonIn.setCheckable(False)
        self.navButtonIn.setAutoDefault(False)
        self.navButtonIn.setFlat(False)
        self.groupRotation = QGroupBox(self.groupNavigation)
        self.groupRotation.setObjectName(u"groupRotation")
        self.groupRotation.setGeometry(QRect(10, 120, 151, 101))
        self.rotButtonZ = QPushButton(self.groupRotation)
        self.rotButtonZ.setObjectName(u"rotButtonZ")
        self.rotButtonZ.setGeometry(QRect(110, 60, 41, 31))
        self.rotButtonX = QPushButton(self.groupRotation)
        self.rotButtonX.setObjectName(u"rotButtonX")
        self.rotButtonX.setGeometry(QRect(10, 60, 41, 31))
        self.rotButtonY = QPushButton(self.groupRotation)
        self.rotButtonY.setObjectName(u"rotButtonY")
        self.rotButtonY.setGeometry(QRect(60, 60, 41, 31))
        self.inputDegrees = QTextEdit(self.groupRotation)
        self.inputDegrees.setObjectName(u"inputDegrees")
        self.inputDegrees.setGeometry(QRect(60, 30, 91, 31))
        self.label = QLabel(self.groupRotation)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 51, 31))
        self.label_2 = QLabel(self.groupNavigation)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 230, 67, 22))
        self.zoomButtonPlus = QPushButton(self.groupNavigation)
        self.zoomButtonPlus.setObjectName(u"zoomButtonPlus")
        self.zoomButtonPlus.setGeometry(QRect(70, 230, 41, 21))
        self.zoomButtonMinus = QPushButton(self.groupNavigation)
        self.zoomButtonMinus.setObjectName(u"zoomButtonMinus")
        self.zoomButtonMinus.setGeometry(QRect(120, 230, 41, 21))
        self.groupObjects = QGroupBox(self.centralwidget)
        self.groupObjects.setObjectName(u"groupObjects")
        self.groupObjects.setGeometry(QRect(0, 0, 171, 301))
        self.objButtonNew = QPushButton(self.groupObjects)
        self.objButtonNew.setObjectName(u"objButtonNew")
        self.objButtonNew.setGeometry(QRect(10, 220, 71, 31))
        self.objButtonDelete = QPushButton(self.groupObjects)
        self.objButtonDelete.setObjectName(u"objButtonDelete")
        self.objButtonDelete.setGeometry(QRect(90, 220, 71, 31))
        self.listObjects = QListWidget(self.groupObjects)
        self.listObjects.setObjectName(u"listObjects")
        self.listObjects.setGeometry(QRect(10, 30, 151, 181))
        self.objButtonTransform = QPushButton(self.groupObjects)
        self.objButtonTransform.setObjectName(u"objButtonTransform")
        self.objButtonTransform.setGeometry(QRect(10, 260, 151, 31))
        self.log = QTextBrowser(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(180, 450, 611, 141))
        self.groupViewport = QtWidgets.QLabel(self.centralwidget)
        self.groupViewport.setObjectName(u"groupViewport")
        self.groupViewport.setGeometry(QRect(180, 0, 611, 441))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.navButtonIn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupNavigation.setTitle(QCoreApplication.translate("MainWindow", u"Navigation", None))
        self.navButtonUp.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.navButtonDown.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.navButtonLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.navButtonRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.navButtonOut.setText(QCoreApplication.translate("MainWindow", u"Out", None))
        self.navButtonIn.setText(QCoreApplication.translate("MainWindow", u"In", None))
        self.groupRotation.setTitle(QCoreApplication.translate("MainWindow", u"Rotation", None))
        self.rotButtonZ.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.rotButtonX.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.rotButtonY.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Graus: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Zoom:", None))
        self.zoomButtonPlus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.zoomButtonMinus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.groupObjects.setTitle(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.objButtonNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.objButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.objButtonTransform.setText(QCoreApplication.translate("MainWindow", u"Transform", None))
        self.groupViewport.setText(QCoreApplication.translate("MainWindow", u"Viewport", None))
    # retranslateUi

################################################################################

    def __init__(self, argv: List[str]):
        self.app = QApplication(argv)
        self.mainWindow = QMainWindow()
        self.setupUi(self.mainWindow)
        self.setUpPixmap()
        self.setupButtons()
        self.displayFile = []
        self.matrixList = []

        self.windowSize = [default.XW_MIN, default.YW_MIN, default.XW_MAX, default.YW_MAX]
        self.nav = [0, 0]
        self.zoom = 1

        # OBJETO DE TESTE 
        self.displayFile.append(Wireframe([Point(0,0), Point(100,0), Point(100,100), Point(0,100)], "Test"))
        self.listObjects.addItem("Test")

    def exec(self):
        self.drawDisplayFile()
        self.mainWindow.show()
        sys.exit(self.app.exec_())

    def setupButtons(self):
        self.navButtonUp.clicked.connect(lambda: self.navigation(up = True))
        self.navButtonDown.clicked.connect(lambda: self.navigation(down = True))
        self.navButtonLeft.clicked.connect(lambda: self.navigation(left = True))
        self.navButtonRight.clicked.connect(lambda: self.navigation(right = True))
        self.navButtonOut.clicked.connect(lambda: self.navigation(zoomOut = True))
        self.navButtonIn.clicked.connect(lambda: self.navigation(zoomIn = True))

        self.rotButtonX.clicked.connect(lambda: self.rotate(X = True))
        self.rotButtonY.clicked.connect(lambda: self.rotate(Y = True))
        self.rotButtonZ.clicked.connect(lambda: self.rotate(Z = True))

        self.objButtonNew.clicked.connect(lambda: self.objectAction(new = True))
        self.objButtonDelete.clicked.connect(lambda: self.objectAction(delete = True))

        self.zoomButtonMinus.clicked.connect(lambda: self.objectAction(minus = True))
        self.zoomButtonPlus.clicked.connect(lambda: self.objectAction(plus = True))

        self.objButtonTransform.clicked.connect(lambda: self.objectAction(transform = True))

    def rotate(self, X = False, Y = False, Z = False) -> None:
        consoleLog = "Viewport rotation: "

    def navigation(self, up: bool = False, down: bool = False, left: bool = False, right: bool = False,
     zoomIn: bool = False, zoomOut: bool = False) -> None:
        consoleLog = "Viewport navigation: "
        
        if up:
            consoleLog += f"Move up: X={self.nav[0]}, Y={self.nav[1]}"
            self.nav[1] += 10
        elif down:
            consoleLog += f"Move down: X={self.nav[0]}, Y={self.nav[1]}"
            self.nav[1] -= 10
        elif left:
            consoleLog += f"Move left: X={self.nav[0]}, Y={self.nav[1]}"
            self.nav[0] -= 10
        elif right:
            consoleLog += f"Move right: X={self.nav[0]}, Y={self.nav[1]}"
            self.nav[0] += 10
        elif zoomIn:
            consoleLog += f"Zoom in: {self.zoom:.2f}"
            self.zoom -= 0.1
        elif zoomOut:
            consoleLog += f"Zoom out: {self.zoom:.2f}"
            self.zoom += 0.1
        else:
            pass

        self.calculateWindowsSize()
        self.drawDisplayFile()
        self.logMessage(consoleLog)

    def objectAction(self, new: bool = False, delete: bool = False, minus: bool = False, plus: bool = False, transform: bool = False) -> None:
        consoleLog = "Object action: "
        
        if new:
            consoleLog += "Opening new wireframe window"
        elif delete:
            consoleLog += "Deleting object"
        elif minus:
            consoleLog += "Zooming out object: what's supposed to happen here?"
        elif plus:
            consoleLog += "Zooming in object: what's supposed to happen here?"
        elif transform:
            consoleLog += "Adding transformation for object"
        else:
            pass

        if new:
            self.logMessage(consoleLog)
            self.newWireframe()
        elif delete:
            for element in self.listObjects.selectedIndexes():
                consoleLog += f" {element.row()} from wireframe list"
                self.listObjects.takeItem(element.row())
                self.displayFile.pop(element.row())
                self.logMessage(consoleLog)
        elif transform:
            element = 0
            for element in self.listObjects.selectedIndexes():
                element = element.row()
            self.addTransformation()
        else:
            self.logMessage(consoleLog)
        self.drawDisplayFile()

    def logMessage(self, message: str) -> None:
        fullMessage = f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
        self.log.append(fullMessage)
        print(fullMessage)

    def newWireframe(self) -> None:
        ex = Ui_NewWireframe(self)
        ex.setupUi(ex)
        ex.setupButtons()
        ex.show()
        ex.exec()

    def addTransformation(self) -> None:
        n = len(self.listObjects.selectedIndexes())
        if n:
            ex = Ui_TransformationWindow(self)
            ex.setupUi(ex)
            ex.setupButtons()
            ex.show()
            ex.exec()
        else:
            self.logMessage("Error! Please select one object before adding transformations")

    def setUpPixmap(self) -> None:
        canvas = QtGui.QPixmap(default.XV_MAX, default.YV_MAX)
        canvas.fill(QtGui.QColor("black"))
        self.groupViewport.setPixmap(canvas)
        self.painter = QtGui.QPainter(self.groupViewport.pixmap())
        self.groupViewport.setObjectName("groupViewport")

    def drawPoint(self, point: Point) -> None:
        transformedPoint = viewPortTransform(point, self.windowSize)
        self.groupViewport.update()
        self.painter.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        self.painter.drawPoint(transformedPoint.x, transformedPoint.y)

    def drawLine(self, point1: Point, point2: Point) -> None:
        transformedPoint1 = viewPortTransform(point1, self.windowSize)
        transformedPoint2 = viewPortTransform(point2, self.windowSize)
        self.groupViewport.update()
        self.painter.setPen(QtGui.QPen(QtCore.Qt.red, 2))
        self.painter.drawLine(transformedPoint1.x, transformedPoint1.y, transformedPoint2.x, transformedPoint2.y)

    def drawWireframe(self, drawable: Wireframe) -> None:
        iterations = len(drawable.coordinates)
        for x in range(0, iterations):
            if x == iterations-1:
                self.drawLine(drawable.coordinates[x], drawable.coordinates[0])
            else:
                self.drawLine(drawable.coordinates[x], drawable.coordinates[x+1])

    def addDrawableToDisplayFile(self, drawable: Union[Point, Line, Wireframe]) -> None:
        self.displayFile.add(drawable)

    def calculateWindowsSize(self) -> None:
        if self.zoom < 0.2:
            self.zoom = 0.2
            self.logMessage("Set zoom to 0.2 to prevent overflow!")

        self.windowSize = [default.XW_MIN+self.nav[0], default.YW_MIN+self.nav[1],
         default.XW_MAX+self.nav[0],default.YW_MAX+self.nav[1]]
        self.windowSize = [v*self.zoom for v in self.windowSize]

    def drawDisplayFile(self) -> None:
        self.groupViewport.pixmap().fill(QtGui.QColor("black"))
        self.groupViewport.update()
        for drawable in self.displayFile:
            if type(drawable) == Wireframe:
                self.drawWireframe(drawable)
            if type(drawable) == Line:
                self.drawLine(drawable.point1, drawable.point2)
            if type(drawable) == Point:
                print("Que mané desenha 1D. Para de ser bobo, desenha o que existe.")
                self.drawLine(drawable, drawable)