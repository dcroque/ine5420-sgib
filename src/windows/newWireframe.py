# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewPointyvOGfq.ui'
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
        NewWireframe.resize(355, 280)
        self.groupBox = QGroupBox(NewWireframe)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 120, 221))
        self.list_points = QListWidget(self.groupBox)
        self.list_points.setObjectName(u"list_points")
        self.list_points.setGeometry(QRect(10, 30, 101, 181))
        self.groupBox_2 = QGroupBox(NewWireframe)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(130, 10, 221, 221))
        self.input_z = QTextEdit(self.groupBox_2)
        self.input_z.setObjectName(u"input_z")
        self.input_z.setGeometry(QRect(150, 130, 61, 41))
        self.input_x = QTextEdit(self.groupBox_2)
        self.input_x.setObjectName(u"input_x")
        self.input_x.setGeometry(QRect(10, 130, 61, 41))
        self.input_y = QTextEdit(self.groupBox_2)
        self.input_y.setObjectName(u"input_y")
        self.input_y.setGeometry(QRect(80, 130, 61, 41))
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
        self.button_add = QPushButton(self.groupBox_2)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setGeometry(QRect(151, 180, 61, 31))
        self.input_name = QTextEdit(self.groupBox_2)
        self.input_name.setObjectName(u"input_name")
        self.input_name.setGeometry(QRect(10, 60, 201, 41))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 201, 22))
        self.label_4.setFont(font)
        self.button_finish = QPushButton(NewWireframe)
        self.button_finish.setObjectName(u"button_finish")
        self.button_finish.setGeometry(QRect(271, 240, 81, 31))
        self.button_cancel = QPushButton(NewWireframe)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(180, 240, 81, 31))
        self.button_delete_point = QPushButton(NewWireframe)
        self.button_delete_point.setObjectName(u"button_delete_point")
        self.button_delete_point.setGeometry(QRect(0, 240, 121, 31))

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
        self.button_add.setText(QCoreApplication.translate("NewWireframe", u"Add", None))
        self.label_4.setText(QCoreApplication.translate("NewWireframe", u"Wireframe name", None))
        self.button_finish.setText(QCoreApplication.translate("NewWireframe", u"Finish", None))
        self.button_cancel.setText(QCoreApplication.translate("NewWireframe", u"Cancel", None))
        self.button_delete_point.setText(QCoreApplication.translate("NewWireframe", u"Delete point", None))
    # retranslateUi

################################################################################

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.main_window = parent

    def setupButtons(self):
        self.button_add.clicked.connect(lambda: self.add_point())
        self.button_cancel.clicked.connect(lambda: self.finish())
        self.button_finish.clicked.connect(lambda: self.finish(add = True))
        self.button_delete_point.clicked.connect(lambda: self.delete_point())

    def add_point(self):
        console_log = "Add point: "

        coord = [None]*3
        coord[0] = self.input_x.toPlainText()
        coord[1] = self.input_y.toPlainText()
        coord[2] = self.input_z.toPlainText()

        is_float = True
        for i in range(len(coord)):
            try:
                coord[i] = float(coord[i])
            except:
                is_float = False
                console_log += "Error! Non-float value"

        if is_float:
            console_log += f"Adding point ({coord[0]:.2f},{coord[1]:.2f},{coord[2]:.2f})"
            self.list_points.addItem(f"({coord[0]:.2f},{coord[1]:.2f},{coord[2]:.2f})")

        self.log_message(console_log)

    def delete_point(self):
        for element in self.list_points.selectedIndexes():
            console_log = f"Delete item: Deleting item {element.row()} from wireframe list"
            self.list_points.takeItem(element.row())
            self.log_message(console_log)

    def finish(self, add = False):
        console_log = "Finishing: "
        if add:
            self.log_message(self.input_name.toPlainText())
            if self.input_name.toPlainText() == "":
                self.main_window.listWidget.addItem("Wireframe")
            else:
                self.main_window.listWidget.addItem(self.input_name.toPlainText())
        else:
            console_log += "No actions"

        self.log_message(console_log)

        self.close()

    def log_message(self, message):
        message = f"[NEW WIREFRAME] {message}"
        self.main_window.log_message(message)