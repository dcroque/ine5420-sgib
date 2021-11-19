import sys
from datetime import datetime
from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from structs import Line, Point, Wireframe
from viewPortOperation import viewPortTransform
from windows.newWireframe import Ui_NewWireframe

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
        self.groupObjects = QGroupBox(self.centralwidget)
        self.groupObjects.setObjectName(u"groupObjects")
        self.groupObjects.setGeometry(QRect(0, 0, 171, 301))
        self.objButtonNew = QPushButton(self.groupObjects)
        self.objButtonNew.setObjectName(u"objButtonNew")
        self.objButtonNew.setGeometry(QRect(10, 220, 71, 31))
        self.objButtonDelete = QPushButton(self.groupObjects)
        self.objButtonDelete.setObjectName(u"objButtonDelete")
        self.objButtonDelete.setGeometry(QRect(90, 220, 71, 31))
        self.objButtonSave = QPushButton(self.groupObjects)
        self.objButtonSave.setObjectName(u"objButtonSave")
        self.objButtonSave.setGeometry(QRect(10, 260, 71, 31))
        self.objButtonLoad = QPushButton(self.groupObjects)
        self.objButtonLoad.setObjectName(u"objButtonLoad")
        self.objButtonLoad.setGeometry(QRect(90, 260, 71, 31))
        self.listObjects = QListWidget(self.groupObjects)
        self.listObjects.setObjectName(u"listObjects")
        self.listObjects.setGeometry(QRect(10, 30, 151, 181))
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
        self.groupObjects.setTitle(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.objButtonNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.objButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.objButtonSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.objButtonLoad.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.groupViewport.setText(QCoreApplication.translate("MainWindow", u"Viewport", None))
    # retranslateUi

################################################################################

    def setupButtons(self):
        self.navButtonUp.clicked.connect(lambda: self.navigation(up = True))
        self.navButtonDown.clicked.connect(lambda: self.navigation(down = True))
        self.navButtonLeft.clicked.connect(lambda: self.navigation(left = True))
        self.navButtonRight.clicked.connect(lambda: self.navigation(right = True))
        self.navButtonOut.clicked.connect(lambda: self.navigation(zoomOut = True))
        self.navButtonIn.clicked.connect(lambda: self.navigation(zoomIn = True))

        self.objButtonNew.clicked.connect(lambda: self.objectAction(new = True))
        self.objButtonDelete.clicked.connect(lambda: self.objectAction(delete = True))
        self.objButtonSave.clicked.connect(lambda: self.objectAction(save = True))
        self.objButtonLoad.clicked.connect(lambda: self.objectAction(load = True))

    def navigation(self, up = False, down = False, left = False, right = False, zoomIn = False, zoomOut = False):
        consoleLog = "Viewport navigation: "
        
        if up:
            consoleLog += "Move up"
        elif down:
            consoleLog += "Move down"
        elif left:
            consoleLog += "Move left"
        elif right:
            consoleLog += "Move right"
        elif zoomIn:
            consoleLog += "Zoom in"
        elif zoomOut:
            consoleLog += "Zoom out"
        else:
            pass

        self.logMessage(consoleLog)

    def objectAction(self, new = False, delete = False, save = False, load = False):
        consoleLog = "Object action: "
        
        if new:
            consoleLog += "Opening new wireframe window"
        elif delete:
            consoleLog += "Deleting object"
        elif save:
            consoleLog += "Save object (NOT IMPLEMENTED)"
        elif load:
            consoleLog += "Load object (NOT IMPLEMENTED)"
        else:
            pass

        if new:
            self.logMessage(consoleLog)
            self.newWireframe()
        elif delete:
            for element in self.listObjects.selectedIndexes():
                consoleLog += f" {element.row()} from wireframe list"
                self.listObjects.takeItem(element.row())
                self.logMessage(consoleLog)
        else:
            self.logMessage(consoleLog)

    def logMessage(self, message):
        fullMessage = f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
        self.log.append(fullMessage)
        print(fullMessage)

    def newWireframe(self):
        ex = Ui_NewWireframe(self)
        ex.setupUi(ex)
        ex.setupButtons()
        ex.show()
        ex.exec()

    def setUpPixmap(self):
        canvas = QtGui.QPixmap(611, 401)
        canvas.fill(QtGui.QColor("black"))
        self.groupViewport.setPixmap(canvas)
        self.painter = QtGui.QPainter(self.groupViewport.pixmap())
        self.groupViewport.setObjectName("groupViewport")

    
    def drawLine(self, point1: Point, point2: Point) -> None:
        transformedPoint1 = viewPortTransform(point1)
        transformedPoint2 = viewPortTransform(point2)
        self.displayFrame.update()
        self.painter.setPen(QtGui.QPen(QtCore.Qt.red, 5))
        self.painter.drawLine(transformedPoint1.x, transformedPoint1.y, transformedPoint2.x, transformedPoint2.y)

    def drawWireframe(self, drawable: Wireframe) -> None:
        for x in range(0, len(drawable) - 1):
            self.drawLine(drawable[x], drawable[x+1])

class MainWindow:
    def __init__(self, argv: List[str]):
        self.app = QApplication(argv)
        self.mainWindow = Ui_MainWindow()
        self.mainWindow.setupUi(self.mainWindow)
        self.mainWindow.setUpPixmap()
        self.mainWindow.setupButtons()

    def exec(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())