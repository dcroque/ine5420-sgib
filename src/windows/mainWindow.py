import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from structs import Line, Point, Wireframe
from viewPortOperation import viewPortTransform
from windows.newWireframe import Ui_NewWireframe


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowFgJYrU.ui'
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
        self.group_navigation = QGroupBox(self.centralwidget)
        self.group_navigation.setObjectName(u"group_navigation")
        self.group_navigation.setGeometry(QRect(0, 300, 171, 291))
        self.nav_button_up = QPushButton(self.group_navigation)
        self.nav_button_up.setObjectName(u"nav_button_up")
        self.nav_button_up.setGeometry(QRect(60, 40, 51, 31))
        self.nav_button_down = QPushButton(self.group_navigation)
        self.nav_button_down.setObjectName(u"nav_button_down")
        self.nav_button_down.setGeometry(QRect(60, 70, 51, 31))
        self.nav_button_left = QPushButton(self.group_navigation)
        self.nav_button_left.setObjectName(u"nav_button_left")
        self.nav_button_left.setGeometry(QRect(10, 50, 51, 41))
        self.nav_button_right = QPushButton(self.group_navigation)
        self.nav_button_right.setObjectName(u"nav_button_right")
        self.nav_button_right.setGeometry(QRect(110, 50, 51, 41))
        self.nav_button_out = QPushButton(self.group_navigation)
        self.nav_button_out.setObjectName(u"nav_button_out")
        self.nav_button_out.setGeometry(QRect(120, 100, 31, 21))
        self.nav_button_in = QPushButton(self.group_navigation)
        self.nav_button_in.setObjectName(u"nav_button_in")
        self.nav_button_in.setGeometry(QRect(20, 100, 31, 21))
        self.nav_button_in.setCheckable(False)
        self.nav_button_in.setAutoDefault(False)
        self.nav_button_in.setFlat(False)
        self.group_objects = QGroupBox(self.centralwidget)
        self.group_objects.setObjectName(u"group_objects")
        self.group_objects.setGeometry(QRect(0, 0, 171, 301))
        self.obj_button_new = QPushButton(self.group_objects)
        self.obj_button_new.setObjectName(u"obj_button_new")
        self.obj_button_new.setGeometry(QRect(10, 220, 71, 31))
        self.obj_button_delete = QPushButton(self.group_objects)
        self.obj_button_delete.setObjectName(u"obj_button_delete")
        self.obj_button_delete.setGeometry(QRect(90, 220, 71, 31))
        self.obj_button_save = QPushButton(self.group_objects)
        self.obj_button_save.setObjectName(u"obj_button_save")
        self.obj_button_save.setGeometry(QRect(10, 260, 71, 31))
        self.obj_button_load = QPushButton(self.group_objects)
        self.obj_button_load.setObjectName(u"obj_button_load")
        self.obj_button_load.setGeometry(QRect(90, 260, 71, 31))
        self.listWidget = QListWidget(self.group_objects)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 30, 151, 181))
        self.log = QTextBrowser(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(180, 450, 611, 141))
        self.group_viewport = QtWidgets.QLabel(self.centralwidget)
        self.group_viewport.setObjectName(u"group_viewport")
        self.group_viewport.setGeometry(QRect(180, 0, 611, 441))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.group_navigation.setTitle(QCoreApplication.translate("MainWindow", u"Navigation", None))
        self.nav_button_up.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.nav_button_down.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.nav_button_left.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.nav_button_right.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.nav_button_out.setText(QCoreApplication.translate("MainWindow", u"Out", None))
        self.nav_button_in.setText(QCoreApplication.translate("MainWindow", u"In", None))
        self.group_objects.setTitle(QCoreApplication.translate("MainWindow", u"Objects", None))
        self.obj_button_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.obj_button_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.obj_button_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.obj_button_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.group_viewport.setText(QCoreApplication.translate("MainWindow", u"Viewport", None))
    # retranslateUi

################################################################################

    def setupButtons(self):
        self.nav_button_up.clicked.connect(lambda: self.navigation(up = True))
        self.nav_button_down.clicked.connect(lambda: self.navigation(down = True))
        self.nav_button_left.clicked.connect(lambda: self.navigation(left = True))
        self.nav_button_right.clicked.connect(lambda: self.navigation(right = True))
        self.nav_button_out.clicked.connect(lambda: self.navigation(zoom_out = True))
        self.nav_button_in.clicked.connect(lambda: self.navigation(zoom_in = True))

        self.obj_button_new.clicked.connect(lambda: self.object_action(new = True))
        self.obj_button_delete.clicked.connect(lambda: self.object_action(delete = True))
        self.obj_button_save.clicked.connect(lambda: self.object_action(save = True))
        self.obj_button_load.clicked.connect(lambda: self.object_action(load = True))

    def navigation(self, up = False, down = False, left = False, right = False, zoom_in = False, zoom_out = False):
        console_log = "Viewport navigation: "
        
        if up:
            console_log += "Move up"
        elif down:
            console_log += "Move down"
        elif left:
            console_log += "Move left"
        elif right:
            console_log += "Move right"
        elif zoom_in:
            console_log += "Zoom in"
        elif zoom_out:
            console_log += "Zoom out"
        else:
            pass

        self.log_message(console_log)

    def object_action(self, new = False, delete = False, save = False, load = False):
        console_log = "Object action: "
        
        if new:
            console_log += "Opening new wireframe window"
        elif delete:
            console_log += "Deleting object"
        elif save:
            console_log += "Save object (NOT IMPLEMENTED)"
        elif load:
            console_log += "Load object (NOT IMPLEMENTED)"
        else:
            pass

        if new:
            self.log_message(console_log)
            self.new_wireframe()
        elif delete:
            for element in self.listWidget.selectedIndexes():
                console_log += f" {element.row()} from wireframe list"
                self.listWidget.takeItem(element.row())
                self.log_message(console_log)

    def log_message(self, message):
        full_message = f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
        self.log.append(full_message)
        print(full_message)

    def new_wireframe(self):
        ex = Ui_NewWireframe(self)
        ex.setupUi(ex)
        ex.setupButtons()
        ex.show()
        ex.exec()

    def setUpPixmap(self):
        canvas = QtGui.QPixmap(611, 401)
        canvas.fill(QtGui.QColor("black"))
        self.group_viewport.setPixmap(canvas)
        self.painter = QtGui.QPainter(self.group_viewport.pixmap())
        self.group_viewport.setObjectName("group_viewport")

    
    def drawLine(self, point1: Point, point2: Point) -> None:
        transformedPoint1 = viewPortTransform(point1)
        transformedPoint2 = viewPortTransform(point2)
        self.displayFrame.update()
        self.painter.setPen(QtGui.QPen(QtCore.Qt.red, 5))
        self.painter.drawLine(transformedPoint1.x, transformedPoint1.y, transformedPoint2.x, transformedPoint2.y)

    def drawWireframe(self, drawable: Wireframe) -> None:
        for x in range(0, len(drawable) - 1):
            self.drawLine(drawable[x], drawable[x+1])