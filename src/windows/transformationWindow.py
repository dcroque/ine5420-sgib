from typing import Union
import numpy as np
from structs import TransformOperation, Point, Line, Wireframe
from viewPortOperation import collapseMatrix

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TransformcpTOhc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_TransformationWindow(QDialog):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 450)
        self.groupTransformations = QGroupBox(Dialog)
        self.groupTransformations.setObjectName(u"groupTransformations")
        self.groupTransformations.setGeometry(QRect(0, 0, 191, 301))
        self.listTrans = QListWidget(self.groupTransformations)
        self.listTrans.setObjectName(u"listTrans")
        self.listTrans.setGeometry(QRect(10, 40, 171, 251))
        self.groupRotation = QGroupBox(Dialog)
        self.groupRotation.setObjectName(u"groupRotation")
        self.groupRotation.setGeometry(QRect(200, 0, 251, 161))
        self.inputRotX = QTextEdit(self.groupRotation)
        self.inputRotX.setObjectName(u"inputRotX")
        self.inputRotX.setGeometry(QRect(10, 50, 71, 41))
        self.label_3 = QLabel(self.groupRotation)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 21, 41))
        self.inputRotY = QTextEdit(self.groupRotation)
        self.inputRotY.setObjectName(u"inputRotY")
        self.inputRotY.setGeometry(QRect(90, 50, 71, 41))
        self.label_4 = QLabel(self.groupRotation)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 20, 21, 41))
        self.inputRotZ = QTextEdit(self.groupRotation)
        self.inputRotZ.setObjectName(u"inputRotZ")
        self.inputRotZ.setGeometry(QRect(170, 50, 71, 41))
        self.label_5 = QLabel(self.groupRotation)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(170, 20, 21, 41))
        self.inputRotDegrees = QTextEdit(self.groupRotation)
        self.inputRotDegrees.setObjectName(u"inputRotDegrees")
        self.inputRotDegrees.setGeometry(QRect(10, 110, 71, 41))
        self.label_12 = QLabel(self.groupRotation)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 90, 71, 21))
        self.rotButtonPoint = QPushButton(self.groupRotation)
        self.rotButtonPoint.setObjectName(u"rotButtonPoint")
        self.rotButtonPoint.setGeometry(QRect(90, 120, 51, 31))
        self.label_13 = QLabel(self.groupRotation)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(90, 90, 161, 21))
        self.rotButtonObject = QPushButton(self.groupRotation)
        self.rotButtonObject.setObjectName(u"rotButtonObject")
        self.rotButtonObject.setGeometry(QRect(140, 120, 51, 31))
        self.rotButtonOrigin = QPushButton(self.groupRotation)
        self.rotButtonOrigin.setObjectName(u"rotButtonOrigin")
        self.rotButtonOrigin.setGeometry(QRect(190, 120, 51, 31))
        self.groupTranslation = QGroupBox(Dialog)
        self.groupTranslation.setObjectName(u"groupTranslation")
        self.groupTranslation.setGeometry(QRect(200, 160, 251, 141))
        self.label_8 = QLabel(self.groupTranslation)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 20, 21, 41))
        self.label_7 = QLabel(self.groupTranslation)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 20, 21, 41))
        self.inputTransZ = QTextEdit(self.groupTranslation)
        self.inputTransZ.setObjectName(u"inputTransZ")
        self.inputTransZ.setGeometry(QRect(170, 50, 71, 41))
        self.label_6 = QLabel(self.groupTranslation)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 20, 21, 41))
        self.inputTransY = QTextEdit(self.groupTranslation)
        self.inputTransY.setObjectName(u"inputTransY")
        self.inputTransY.setGeometry(QRect(90, 50, 71, 41))
        self.inputTransX = QTextEdit(self.groupTranslation)
        self.inputTransX.setObjectName(u"inputTransX")
        self.inputTransX.setGeometry(QRect(10, 50, 71, 41))
        self.transAdd = QPushButton(self.groupTranslation)
        self.transAdd.setObjectName(u"transAdd")
        self.transAdd.setGeometry(QRect(10, 100, 231, 31))
        self.groupScaling = QGroupBox(Dialog)
        self.groupScaling.setObjectName(u"groupScaling")
        self.groupScaling.setGeometry(QRect(200, 300, 251, 141))
        self.inputScaleX = QTextEdit(self.groupScaling)
        self.inputScaleX.setObjectName(u"inputScaleX")
        self.inputScaleX.setGeometry(QRect(10, 50, 71, 41))
        self.label_10 = QLabel(self.groupScaling)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 20, 21, 41))
        self.inputScaleZ = QTextEdit(self.groupScaling)
        self.inputScaleZ.setObjectName(u"inputScaleZ")
        self.inputScaleZ.setGeometry(QRect(170, 50, 71, 41))
        self.inputScaleY = QTextEdit(self.groupScaling)
        self.inputScaleY.setObjectName(u"inputScaleY")
        self.inputScaleY.setGeometry(QRect(90, 50, 71, 41))
        self.label_9 = QLabel(self.groupScaling)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(170, 20, 21, 41))
        self.label_11 = QLabel(self.groupScaling)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(90, 20, 21, 41))
        self.scaleAdd = QPushButton(self.groupScaling)
        self.scaleAdd.setObjectName(u"scaleAdd")
        self.scaleAdd.setGeometry(QRect(10, 100, 231, 31))
        self.transDelete = QPushButton(Dialog)
        self.transDelete.setObjectName(u"transDelete")
        self.transDelete.setGeometry(QRect(10, 310, 181, 31))
        self.transFinish = QPushButton(Dialog)
        self.transFinish.setObjectName(u"transFinish")
        self.transFinish.setGeometry(QRect(10, 370, 181, 31))
        self.transCancel = QPushButton(Dialog)
        self.transCancel.setObjectName(u"transCancel")
        self.transCancel.setGeometry(QRect(10, 410, 181, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupTransformations.setTitle(QCoreApplication.translate("Dialog", u"Transformations", None))
        self.groupRotation.setTitle(QCoreApplication.translate("Dialog", u"Rotation", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Z", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Degrees", None))
        self.rotButtonPoint.setText(QCoreApplication.translate("Dialog", u"Point", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Add Rotation around:", None))
        self.rotButtonObject.setText(QCoreApplication.translate("Dialog", u"Object", None))
        self.rotButtonOrigin.setText(QCoreApplication.translate("Dialog", u"Origin", None))
        self.groupTranslation.setTitle(QCoreApplication.translate("Dialog", u"Translation", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Z", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.transAdd.setText(QCoreApplication.translate("Dialog", u"Add translation", None))
        self.groupScaling.setTitle(QCoreApplication.translate("Dialog", u"Scaling", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Z", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Y", None))
        self.scaleAdd.setText(QCoreApplication.translate("Dialog", u"Add scaling", None))
        self.transDelete.setText(QCoreApplication.translate("Dialog", u"Delete transformation", None))
        self.transFinish.setText(QCoreApplication.translate("Dialog", u"Transform", None))
        self.transCancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

    def __init__(self, parent) -> None:
        super().__init__()
        self.mainWindow = parent
        self.transformations = []

    def setupButtons(self) -> None:
        self.transDelete.clicked.connect(lambda: self.delete())
        self.transCancel.clicked.connect(lambda: self.finish())
        self.transFinish.clicked.connect(lambda: self.finish(add = True))

        self.rotButtonObject.clicked.connect(lambda: self.addRot(rotObj = True))
        self.rotButtonOrigin.clicked.connect(lambda: self.addRot(rotOrigin = True))
        self.rotButtonPoint.clicked.connect(lambda: self.addRot(rotPoint = True))
        self.transAdd.clicked.connect(lambda: self.addTrans())
        self.scaleAdd.clicked.connect(lambda: self.addScale())

    def addRot(self, rotObj = False, rotOrigin = False, rotPoint = False):
        consoleLog = "Add rotation: "
        label = "Rot"
        op = -1
        isFloat = True
        if rotOrigin:
            op = 2
            label += "Origin("
        elif rotObj:
            op = 3
            label += "Obj("
        elif rotPoint:
            op = 4
            label += "Point("
            coord = [None]*3
            coord[0] = self.inputRotX.toPlainText()
            coord[1] = self.inputRotY.toPlainText()
            coord[2] = self.inputRotZ.toPlainText()

            for i in range(len(coord)):
                try:
                    coord[i] = float(coord[i])
                    label += f"{coord[i]:.0f},"
                except:
                    if i == 2:
                        coord[i] = 0
                        consoleLog += "Error! Non-float value for Z, setting as 0"
                        label += f"{coord[i]:.0f},"
                    else:
                        isFloat = False
                        consoleLog += "Error! Non-float value"    
        else:
            pass

        degrees = None
        try:
            degrees = float(self.inputRotDegrees.toPlainText())
            label += f"{degrees:.0f}°)"
        except:
            isFloat = False
            consoleLog += "Error! Non-float value for degrees"

        if isFloat:
            point = Point(0,0,0)
            if rotPoint:
                point = Point(coord[0], coord[1], coord[2])                
            consoleLog += f"{label}"
            self.transformations.append(TransformOperation(point = point, degree = degrees, operation = op))
            self.listTrans.addItem(label)
        self.logMessage(consoleLog)

    def addTrans(self):
        label = "Trans("
        consoleLog = "Add translation: "
        op = 0
        coord = [None]*3
        coord[0] = self.inputTransX.toPlainText()
        coord[1] = self.inputTransY.toPlainText()
        coord[2] = self.inputTransZ.toPlainText()

        isFloat = True
        for i in range(len(coord)):
            try:
                coord[i] = float(coord[i])
                label += f"{coord[i]:.0f},"
            except:
                if i == 2:
                    coord[i] = 0
                    consoleLog += "Error! Non-float value for Z, setting as 0"
                    label += f"{coord[i]:.0f},"
                else:
                    isFloat = False
                    consoleLog += "Error! Non-float value"

        if isFloat:
            label = label[:-1]+")"
            consoleLog += f"{label}"
            point = Point(coord[0], coord[1], coord[2])
            self.transformations.append(TransformOperation(point = point, operation = op))
            self.listTrans.addItem(label)
        self.logMessage(consoleLog)
    
    def addScale(self):
        label = "Scale("
        consoleLog = "Add scale: "
        op = 1
        coord = [None]*3
        coord[0] = self.inputScaleX.toPlainText()
        coord[1] = self.inputScaleY.toPlainText()
        coord[2] = self.inputScaleZ.toPlainText()

        isFloat = True
        for i in range(len(coord)):
            try:
                coord[i] = float(coord[i])
                label += f"{coord[i]:.0f},"
            except:
                if i == 2:
                    coord[i] = 0
                    consoleLog += "Error! Non-float value for Z, setting as 0"
                    label += f"{coord[i]:.0f},"
                else:
                    isFloat = False
                    consoleLog += "Error! Non-float value"

        if isFloat:
            label = label[:-1]+")"
            consoleLog += f"{label}"
            point = Point(coord[0], coord[1], coord[2])
            self.transformations.append(TransformOperation(point = point, operation = op))
            self.listTrans.addItem(label)
        self.logMessage(consoleLog)

    def finish(self, add = False):
        consoleLog = "Finishing: "
        if add:
            index = -1
            for element in self.mainWindow.listObjects.selectedIndexes():
                index = element.row()
            obj = self.mainWindow.displayFile[index]
            new_obj = self.transformObject(obj)
            self.mainWindow.displayFile[index] = new_obj
        else:
            consoleLog += "No actions"

        self.logMessage(consoleLog)

        self.close()

    def delete(self):
        for element in self.listTrans.selectedIndexes():
            consoleLog = f"Delete item: Deleting item {element.row()} from wireframe list"
            self.listTrans.takeItem(element.row())
            self.transformations.pop(element.row())
            self.logMessage(consoleLog)

    def logMessage(self, message) -> None:
        message = f"[TRANSFORMATION] {message}"
        self.mainWindow.logMessage(message)

    def transformObject(self, obj: Union[Point, Line, Wireframe]) -> Union[Point, Line, Wireframe]:
        resultMatrix = collapseMatrix(self.transformations, obj.centre())
        if type(obj) == Wireframe:
            new_obj_points = []
            for point in obj.coordinates:
                pointMtx = point.toMatrix()
                new_point = np.matmul(pointMtx, resultMatrix)
                point_append = Point(0,0,0)
                point_append.matrixToPoint(new_point)
                new_obj_points.append(point_append)
            return Wireframe(new_obj_points, obj.name)