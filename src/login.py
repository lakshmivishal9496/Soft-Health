# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(363, 487)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 381, 501))
        self.widget.setStyleSheet("background-color:rgb(207, 197, 255);\n"
"border-radius: 9px;")
        self.widget.setObjectName("widget")
        self.b1 = QtWidgets.QPushButton(self.widget)
        self.b1.setGeometry(QtCore.QRect(65, 290, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.b1.setFont(font)
        self.b1.setStyleSheet("QPushButton#b1{\n"
"background-color:rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 13px;\n"
"border-radius : 7px;\n"
"\n"
"}\n"
"QPushButton#b1: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.widget)
        self.b2.setGeometry(QtCore.QRect(65, 380, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.b2.setFont(font)
        self.b2.setStyleSheet("QPushButton#b2{\n"
"background-color:rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 13px;\n"
"border-radius : 7px;\n"
"\n"
"}\n"
"QPushButton#b2: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.b2.setObjectName("b2")
        self.l2_2 = QtWidgets.QLabel(self.widget)
        self.l2_2.setGeometry(QtCore.QRect(160, 350, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.l2_2.setFont(font)
        self.l2_2.setStyleSheet("text-align:center;\n"
"font-size:10px;\n"
"color: rgb(85, 0, 255);\n"
"border-radius:2px;")
        self.l2_2.setObjectName("l2_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(150, 50, 71, 71))
        self.label.setStyleSheet("background-color:url(:/image1/images/logo_200x200.png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/image1/images/logo_200x200.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.b5 = QtWidgets.QPushButton(self.widget)
        self.b5.setGeometry(QtCore.QRect(65, 440, 250, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.b5.setFont(font)
        self.b5.setStyleSheet("QPushButton#b5{\n"
"background-color:rgb(85, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"font-size: 13px;\n"
"border-radius : 7px;\n"
"\n"
"}\n"
"QPushButton#b5: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.b5.setObjectName("b5")
        self.tb1 = QtWidgets.QLineEdit(self.widget)
        self.tb1.setGeometry(QtCore.QRect(65, 150, 250, 35))
        self.tb1.setStyleSheet("background-color: rgba(47,42,52,200);\n"
"color:rgb(255,255,255);\n"
"padding-left: 10px;\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"")
        self.tb1.setAlignment(QtCore.Qt.AlignCenter)
        self.tb1.setObjectName("tb1")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(65, 220, 250, 35))
        self.lineEdit.setStyleSheet("background-color: rgba(47,42,52,200);\n"
"color:rgb(255,255,255);\n"
"padding-left: 10px;\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.l2_3 = QtWidgets.QLabel(self.widget)
        self.l2_3.setGeometry(QtCore.QRect(180, 420, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.l2_3.setFont(font)
        self.l2_3.setStyleSheet("text-align:center;\n"
"font-size:10px;\n"
"color: rgb(85, 0, 255);\n"
"border-radius:2px;")
        self.l2_3.setObjectName("l2_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(50, 130, 281, 211))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color:rgba(255, 255, 255, 60);\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox.raise_()
        self.b1.raise_()
        self.b2.raise_()
        self.l2_2.raise_()
        self.label.raise_()
        self.b5.raise_()
        self.tb1.raise_()
        self.lineEdit.raise_()
        self.l2_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "Login"))
        self.b2.setText(_translate("Form", "Sign Up"))
        self.l2_2.setText(_translate("Form", "Need an account?"))
        self.b5.setText(_translate("Form", "Continue as a Guest"))
        self.tb1.setPlaceholderText(_translate("Form", "Enter username...."))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter password....."))
        self.l2_3.setText(_translate("Form", "OR"))
import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
