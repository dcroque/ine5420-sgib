from structs import Point, Line, Wireframe
from typing import Union

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewPointszzvZj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_NewWireframe(QDialog):
    def setupUi(self, NewWireframe):
        if not NewWireframe.objectName():
            NewWireframe.setObjectName(u"NewWireframe")
        NewWireframe.resize(439, 280)
        NewWireframe.setModal(False)
        self.groupBox = QGroupBox(NewWireframe)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 201, 221))
        self.listPoints = QListWidget(self.groupBox)
        self.listPoints.setObjectName(u"listPoints")
        self.listPoints.setGeometry(QRect(10, 30, 181, 181))
        self.groupBox_2 = QGroupBox(NewWireframe)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(210, 10, 221, 221))
        self.inputZ = QTextEdit(self.groupBox_2)
        self.inputZ.setObjectName(u"inputZ")
        self.inputZ.setGeometry(QRect(150, 130, 61, 41))
        self.inputX = QTextEdit(self.groupBox_2)
        self.inputX.setObjectName(u"inputX")
        self.inputX.setGeometry(QRect(10, 130, 61, 41))
        self.inputY = QTextEdit(self.groupBox_2)
        self.inputY.setObjectName(u"inputY")
        self.inputY.setGeometry(QRect(80, 130, 61, 41))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 61, 22))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 110, 61, 22))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 110, 61, 22))
        self.label_3.setFont(font)
        self.buttonAdd = QPushButton(self.groupBox_2)
        self.buttonAdd.setObjectName(u"buttonAdd")
        self.buttonAdd.setGeometry(QRect(151, 180, 61, 31))
        self.inputName = QTextEdit(self.groupBox_2)
        self.inputName.setObjectName(u"inputName")
        self.inputName.setGeometry(QRect(10, 60, 201, 41))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 201, 22))
        self.label_4.setFont(font)
        self.buttonFinish = QPushButton(NewWireframe)
        self.buttonFinish.setObjectName(u"buttonFinish")
        self.buttonFinish.setGeometry(QRect(350, 240, 81, 31))
        self.buttonCancel = QPushButton(NewWireframe)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(260, 240, 81, 31))
        self.buttonDeletePoint = QPushButton(NewWireframe)
        self.buttonDeletePoint.setObjectName(u"buttonDeletePoint")
        self.buttonDeletePoint.setGeometry(QRect(0, 240, 121, 31))

        self.retranslateUi(NewWireframe)

        QMetaObject.connectSlotsByName(NewWireframe)
    # setupUi

    def retranslateUi(self, NewWireframe):
        NewWireframe.setWindowTitle(QCoreApplication.translate("NewWireframe", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewWireframe", u"Points", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("NewWireframe", u"New point", None))
        self.label.setText(QCoreApplication.translate("NewWireframe", u"X", None))
        self.label_2.setText(QCoreApplication.translate("NewWireframe", u"Z", None))
        self.label_3.setText(QCoreApplication.translate("NewWireframe", u"Y", None))
        self.buttonAdd.setText(QCoreApplication.translate("NewWireframe", u"Add", None))
        self.label_4.setText(QCoreApplication.translate("NewWireframe", u"Wireframe name", None))
        self.buttonFinish.setText(QCoreApplication.translate("NewWireframe", u"Finish", None))
        self.buttonCancel.setText(QCoreApplication.translate("NewWireframe", u"Cancel", None))
        self.buttonDeletePoint.setText(QCoreApplication.translate("NewWireframe", u"Delete point", None))
    # retranslateUi

################################################################################

    def __init__(self, parent) -> None:
        super().__init__()
        self.mainWindow = parent
        self.object = None
        self.points = []

    def setupButtons(self) -> None:
        self.buttonAdd.clicked.connect(lambda: self.addPoint())
        self.buttonCancel.clicked.connect(lambda: self.finish())
        self.buttonFinish.clicked.connect(lambda: self.finish(add = True))
        self.buttonDeletePoint.clicked.connect(lambda: self.deletePoint())

    def addPoint(self) -> None: 
        consoleLog = "Add point: "

        coord = [None]*3
        coord[0] = self.inputX.toPlainText()
        coord[1] = self.inputY.toPlainText()
        coord[2] = self.inputZ.toPlainText()

        isFloat = True
        for i in range(len(coord)):
            try:
                coord[i] = float(coord[i])
            except:
                if i == 2:
                    coord[i] = 0
                    consoleLog += "Error! Non-float value for Z, setting as 0"
                else:
                    isFloat = False
                    consoleLog += "Error! Non-float value"

        if isFloat:
            consoleLog += f"Adding point ({coord[0]:.2f},{coord[1]:.2f},{coord[2]:.2f})"
            self.listPoints.addItem(f"({coord[0]:.2f},{coord[1]:.2f},{coord[2]:.2f})")
            self.points.append(Point(coord[0], coord[1], coord[2]))

        self.logMessage(consoleLog)

    def deletePoint(self) -> None:
        for element in self.listPoints.selectedIndexes():
            consoleLog = f"Delete item: Deleting item {element.row()} from wireframe list"
            self.listPoints.takeItem(element.row())
            self.logMessage(consoleLog)

    def assembleObject(self) -> Union[None, Point, Line, Wireframe]:
        nPoints = len(self.points)
        if nPoints == 0:
            return None
        elif nPoints == 1:
            return self.points[0]
        elif nPoints == 2:
            return Line(self.points[0], self.points[1])
        else:
            return Wireframe(self.points, self.inputName.toPlainText())

    def finish(self, add: bool = False) -> None:
        consoleLog = "Finishing: "
        if add:
            self.logMessage(self.inputName.toPlainText())
            if self.inputName.toPlainText() == "":
                self.mainWindow.listObjects.addItem("Wireframe")
            else:
                self.mainWindow.listObjects.addItem(self.inputName.toPlainText())
            obj = self.assembleObject()
            if obj is not None:
                self.mainWindow.displayFile.append(obj)
        else:
            consoleLog += "No actions"

        self.logMessage(consoleLog)

        self.close()

    def logMessage(self, message) -> None:
        message = f"[NEW WIREFRAME] {message}"
        self.mainWindow.logMessage(message)

class NewWireframeWindow:
    def __init__(self, parent) -> None:
        self.window = Ui_NewWireframe(parent)
        self.window.setupUi(self.window)
        self.window.setupButtons()

    def exec(self) -> None:
        self.window.show()
        self.window.exec()