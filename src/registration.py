# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    ''' The ui widget class'''
    def setupUi(self, Form):
        ''' Initialize the ui widget class'''
        Form.setObjectName("Form")
        Form.resize(380, 480)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 380, 480))
        self.widget.setStyleSheet(
            "background-color:rgb(207, 197, 255);\n" "border-radius: 9px;"
        )
        self.widget.setObjectName("widget")
        self.tb3 = QtWidgets.QLineEdit(self.widget)
        self.tb3.setGeometry(QtCore.QRect(65, 150, 250, 35))
        self.tb3.setStyleSheet(
            "background-color: rgba(47,42,52,200);\n"
            "color:rgb(255,255,255);\n"
            "padding-left: 10px;\n"
            "border-bottom-color: rgba(46,82,101,255);\n"
            ""
        )
        self.tb3.setAlignment(QtCore.Qt.AlignCenter)
        self.tb3.setObjectName("tb3")
        self.tb4 = QtWidgets.QLineEdit(self.widget)
        self.tb4.setGeometry(QtCore.QRect(65, 210, 250, 35))
        self.tb4.setStyleSheet(
            "background-color: rgba(47,42,52,200);\n"
            "color:rgb(255,255,255);\n"
            "padding-left: 10px;\n"
            "border-bottom-color: rgba(46,82,101,255);\n"
            ""
        )
        self.tb4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tb4.setAlignment(QtCore.Qt.AlignCenter)
        self.tb4.setObjectName("tb4")
        self.b3 = QtWidgets.QPushButton(self.widget)
        self.b3.setGeometry(QtCore.QRect(65, 340, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.b3.setFont(font)
        self.b3.setStyleSheet(
            "QPushButton#b3{\n"
            "background-color:rgb(85, 0, 127);\n"
            "color: rgb(255, 255, 255);\n"
            "font-size: 13px;\n"
            "border-radius : 7px;\n"
            "\n"
            "}\n"
        )
        self.b3.setObjectName("b3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(140, 40, 101, 91))
        self.label_3.setStyleSheet("background-color:url(images/user1.jpg);")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("images/user1.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.tb5 = QtWidgets.QLineEdit(self.widget)
        self.tb5.setGeometry(QtCore.QRect(65, 270, 250, 35))
        self.tb5.setStyleSheet(
            "background-color: rgba(47,42,52,200);\n"
            "color:rgb(255,255,255);\n"
            "padding-left: 10px;\n"
            "border-bottom-color: rgba(46,82,101,255);\n"
            ""
        )
        self.tb5.setAlignment(QtCore.Qt.AlignCenter)
        self.tb5.setObjectName("tb5")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(164, 60, 61, 51))
        self.label.setStyleSheet("background-color:url(:/newPrefix/images/user1.jpg);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/images/user1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        '''Initialize the  form'''
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tb3.setPlaceholderText(_translate("Form", "Enter username here........."))
        self.tb4.setPlaceholderText(_translate("Form", "Enter password  here........."))
        self.b3.setText(_translate("Form", "Submit"))
        self.tb5.setPlaceholderText(
            _translate("Form", "Enter email here.........       ")
        )


