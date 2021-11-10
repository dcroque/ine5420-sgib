from datetime import datetime

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowBvAHIH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(object):
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
        self.nav_button_up.setObjectName(u"button_up")
        self.nav_button_up.setGeometry(QRect(60, 40, 51, 31))
        self.nav_button_down = QPushButton(self.group_navigation)
        self.nav_button_down.setObjectName(u"button_down")
        self.nav_button_down.setGeometry(QRect(60, 70, 51, 31))
        self.nav_button_left = QPushButton(self.group_navigation)
        self.nav_button_left.setObjectName(u"button_left")
        self.nav_button_left.setGeometry(QRect(10, 50, 51, 41))
        self.nav_button_right = QPushButton(self.group_navigation)
        self.nav_button_right.setObjectName(u"button_right")
        self.nav_button_right.setGeometry(QRect(110, 50, 51, 41))
        self.nav_button_out = QPushButton(self.group_navigation)
        self.nav_button_out.setObjectName(u"button_out")
        self.nav_button_out.setGeometry(QRect(120, 100, 31, 21))
        self.nav_button_in = QPushButton(self.group_navigation)
        self.nav_button_in.setObjectName(u"button_in")
        self.nav_button_in.setGeometry(QRect(20, 100, 31, 21))
        self.nav_button_in.setCheckable(False)
        self.nav_button_in.setAutoDefault(False)
        self.nav_button_in.setFlat(False)
        self.group_objects = QGroupBox(self.centralwidget)
        self.group_objects.setObjectName(u"group_objects")
        self.group_objects.setGeometry(QRect(0, 0, 171, 301))
        self.button_obj_new = QPushButton(self.group_objects)
        self.button_obj_new.setObjectName(u"button_obj_new")
        self.button_obj_new.setGeometry(QRect(10, 220, 71, 31))
        self.button_obj_delete = QPushButton(self.group_objects)
        self.button_obj_delete.setObjectName(u"button_obj_delete")
        self.button_obj_delete.setGeometry(QRect(90, 220, 71, 31))
        self.button_obj_save = QPushButton(self.group_objects)
        self.button_obj_save.setObjectName(u"button_obj_save")
        self.button_obj_save.setGeometry(QRect(10, 260, 71, 31))
        self.button_obj_load = QPushButton(self.group_objects)
        self.button_obj_load.setObjectName(u"button_obj_load")
        self.button_obj_load.setGeometry(QRect(90, 260, 71, 31))
        self.listWidget = QListWidget(self.group_objects)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(10, 30, 151, 181))
        self.log = QTextBrowser(self.centralwidget)
        self.log.setObjectName(u"log")
        self.log.setGeometry(QRect(180, 450, 611, 141))
        self.group_viewport = QGroupBox(self.centralwidget)
        self.group_viewport.setObjectName(u"group_viewport")
        self.group_viewport.setGeometry(QRect(180, 0, 611, 441))
        self.viewport_size = QPushButton(self.group_viewport)
        self.viewport_size.setObjectName(u"viewport_size")
        self.viewport_size.setGeometry(QRect(10, 30, 591, 401))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.setupButtons()

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
        self.button_obj_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.button_obj_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.button_obj_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.button_obj_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.group_viewport.setTitle(QCoreApplication.translate("MainWindow", u"Viewport", None))
        self.viewport_size.setText(QCoreApplication.translate("MainWindow", u"viewport", None))
    # retranslateUi

################################################################################

    def setupButtons(self):
        self.nav_button_up.clicked.connect(lambda: self.navigation(up = True))
        self.nav_button_down.clicked.connect(lambda: self.navigation(down = True))
        self.nav_button_left.clicked.connect(lambda: self.navigation(left = True))
        self.nav_button_right.clicked.connect(lambda: self.navigation(right = True))
        self.nav_button_out.clicked.connect(lambda: self.navigation(zoom_out = True))
        self.nav_button_in.clicked.connect(lambda: self.navigation(zoom_in = True))

    def navigation(self, up = False, down = False, left = False, right = False, zoom_in = False, zoom_out = False):
        console_log = "Viewport navigation: "
        
        if up == True:
            console_log += "Move up"
        elif down == True:
            console_log += "Move down"
        elif left == True:
            console_log += "Move left"
        elif right == True:
            console_log += "Move right"
        elif zoom_in == True:
            console_log += "Zoom in"
        elif zoom_out == True:
            console_log += "Zoom out"
        else:
            pass

        self.log_message(console_log)

    def log_message(self, message):
        full_message = f"[{datetime.now().strftime('%H:%M:%S')}] {message}"
        self.log.append(full_message)
        print(full_message)