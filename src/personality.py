# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personality.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PersonalityTest(object):
    def setupUi(self, PersonalityTest):
        PersonalityTest.setObjectName("PersonalityTest")
        PersonalityTest.resize(1024, 768)
        PersonalityTest.setStyleSheet("background-color:rgb(235, 226, 244);\n"
"border-radius: 9px;")
        self.logout = QtWidgets.QPushButton(PersonalityTest)
        self.logout.setGeometry(QtCore.QRect(800, 50, 175, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.logout.setFont(font)
        self.logout.setStyleSheet("QPushButton#logout{\n"
"background-color:rgb(192, 192, 192,200);\n"
"color:rgb(124, 0, 186);\n"
"font-size: 12px;\n"
"border-radius : 7px;\n"
"\n"
"color: rgb(100, 79, 130);\n"
"\n"
"\n"
"}\n"
"QPushButton#logout: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.logout.setObjectName("logout")
        self.groupBox = QtWidgets.QGroupBox(PersonalityTest)
        self.groupBox.setGeometry(QtCore.QRect(190, 350, 625, 300))
        self.groupBox.setStyleSheet("background-color:rgb(192, 192, 192,150);")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.next_btn = QtWidgets.QPushButton(self.groupBox)
        self.next_btn.setGeometry(QtCore.QRect(220, 225, 175, 40))
        font = QtGui.QFont()
        font.setFamily("Sura")
        font.setPointSize(-1)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet("QPushButton#next_btn{\n"
"background-color:rgb(131, 53, 151);\n"
"color: white;\n"
"font-family: Sura;\n"
"font-size: 15px;\n"
"border-radius : 7px;\n"
"\n"
"}\n"
"QPushButton#next_btn: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.next_btn.setObjectName("next_btn")
        self.back_btn = QtWidgets.QPushButton(self.groupBox)
        self.back_btn.setGeometry(QtCore.QRect(20, 225, 175, 40))
        font = QtGui.QFont()
        font.setFamily("Sura")
        font.setPointSize(-1)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet("QPushButton#back_btn{\n"
"background-color:rgb(131, 53, 151);\n"
"color: white;\n"
"font-family: Sura;\n"
"font-size: 15px;\n"
"border-radius : 7px;\n"
"\n"
"}\n"
"QPushButton#back_btn: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.back_btn.setObjectName("back_btn")
        self.main_btn = QtWidgets.QPushButton(self.groupBox)
        self.main_btn.setGeometry(QtCore.QRect(420, 225, 175, 40))
        font = QtGui.QFont()
        font.setFamily("Sura")
        font.setPointSize(-1)
        self.main_btn.setFont(font)
        self.main_btn.setStyleSheet("QPushButton#main_btn{\n"
"background-color:rgb(131, 53, 151);\n"
"color: white;\n"
"font-family: Sura;\n"
"font-size: 15px;\n"
"border-radius : 7px;\n"
"\n"
"}\n"
"QPushButton#main_btn: pressed {\n"
"background-color: rgb(117, 71, 255);\n"
"}")
        self.main_btn.setObjectName("main_btn")
        self.Question_No = QtWidgets.QLineEdit(self.groupBox)
        self.Question_No.setGeometry(QtCore.QRect(80, 30, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Sura")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(25)
        self.Question_No.setFont(font)
        self.Question_No.setStyleSheet("background-color:rgb(192, 192, 192,0);\n"
"\n"
"color: rgb(100, 79, 130);\n"
"font-size: 26px;\n"
"border-radius : 7px;\n"
"font-family:Sura;\n"
"font-weight:200;")
        self.Question_No.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Question_No.setPlaceholderText("")
        self.Question_No.setObjectName("Question_No")
        self.Question_area = QtWidgets.QLineEdit(self.groupBox)
        self.Question_area.setGeometry(QtCore.QRect(90, 100, 550, 20))
        self.Question_area.setStyleSheet("background-color:rgb(192, 192, 192,0);\n"
"\n"
"color: rgb(100, 79, 130);\n"
"font-size: 16px;\n"
"border-radius : 7px;\n"
"font-family:Sura;\n"
"font-weight:400;")
        self.Question_area.setObjectName("Question_area")
        self.radioButton1 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton1.setGeometry(QtCore.QRect(90, 140, 170, 16))
        self.radioButton1.setStyleSheet("background-color:rgb(192, 192, 192,0);\n"
"font-size: 12px;\n"
"\n"
"color: rgb(100, 79, 130);\n"
"\n"
"border-radius : 7px;\n"
"font-family:Sura;\n"
"font-weight:200;")
        self.radioButton1.setObjectName("radioButton1")
        self.radioButton2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton2.setGeometry(QtCore.QRect(90, 170, 170, 16))
        self.radioButton2.setStyleSheet("background-color:rgb(192, 192, 192,0);\n"
"font-size: 12px;\n"
"font-family: Sura;\n"
"color: rgb(100, 79, 130);\n"
"\n"
"border-radius : 7px;\n"
"font-weight:200;")
        self.radioButton2.setObjectName("radioButton2")
        self.label = QtWidgets.QLabel(PersonalityTest)
        self.label.setGeometry(QtCore.QRect(420, 100, 191, 181))
        self.label.setStyleSheet("background-image:url(logo_200x200.png);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(PersonalityTest)
        QtCore.QMetaObject.connectSlotsByName(PersonalityTest)
    
            # Connect signals to slots
        self.back_btn.clicked.connect(self.previous_question)
        self.next_btn.clicked.connect(self.next_question)
        self.main_btn.clicked.connect(self.show_result)
        self.logout.clicked.connect(self.logout_action)
        self.questions = [
            {
                'question': 'You feel more energetic when:',
                'options': ['Socializing with others', 'Spending time alone'],
                'traits': ['E', 'I']
            },
            {
                'question': 'When making decisions, you usually rely on:',
                'options': ['Facts and details', 'Intuition and gut feelings'],
                'traits': ['S', 'N']
            },
            {
                'question': 'You usually make decisions based on:',
                'options': ['Logical analysis', 'Personal values and emotions'],
                'traits': ['T', 'F']
            },
            {
                'question': 'You prefer:',
                'options': ['A structured and organized lifestyle', 'A spontaneous and flexible lifestyle'],
                'traits': ['J', 'P']
            }
        ]
        self.results = []
        self.init_ui()

    def init_ui(self):
        self.current_question = 0
        self.display_question(self.current_question)
    
    def display_question(self, question_number):
        self.Question_No.setText(f'Question {question_number + 1}')
        self.Question_area.setText(self.questions[question_number]['question'])
        self.radioButton1.setText(self.questions[question_number]['options'][0])
        self.radioButton2.setText(self.questions[question_number]['options'][1])
        self.radioButton1.setChecked(False)
        self.radioButton2.setChecked(False)

    def process_answer(self):
        if self.radioButton1.isChecked():
            self.results.append(self.questions[self.current_question]['traits'][0])
        elif self.radioButton2.isChecked():
            self.results.append(self.questions[self.current_question]['traits'][1])
        else:
            pass

    def show_result(self):
        self.process_answer()
        self.clear_question()
        self.Question_No.setText('Your personality type is:')
        self.Question_area.setText(''.join(self.results))
        self.Question_area.setStyleSheet("background-color:rgb(192, 192, 192,0);\n"
"\n"
"color: rgb(100, 79, 130);\n"
"font-size: 16px;\n"
"border-radius : 7px;\n"
"font-family:Sura;\n"
"font-weight:400;")
        self.Question_area.setAlignment(QtCore.Qt.AlignCenter)
        self.Question_area.setReadOnly(True)
        self.Question_area.setFrame(False)
        self.Question_area.setGeometry(QtCore.QRect(90, 100, 521, 20))
        self.Question_area.setObjectName("Question_area")
        self.radioButton1.deleteLater()
        self.radioButton2.deleteLater()
        self.back_btn.deleteLater()
        self.next_btn.deleteLater()
        self.main_btn.deleteLater()
        self.logout.deleteLater()
        self.label.deleteLater()

    def next_question(self):
        self.process_answer()
        self.clear_question()
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question(self.current_question)
        else:
            self.show_result()

    def previous_question(self):
        self.process_answer()
        self.clear_question()
        self.current_question -= 1
        if self.current_question < len(self.questions):
            self.display_question(self.current_question)
        else:
            self.show_result()

    def logout_action(self):
        # self.close()
        from main import LoginApp
        self.login = LoginApp()
        self.login.show()

    def clear_question(self):
        self.Question_area.clear()
        self.radioButton1.setChecked(False)
        self.radioButton2.setChecked(False)

    # def clear_question(self):
    #     self.Question_area.deleteLater()
    #     for button in self.option_buttons:
    #         button.deleteLater()
    #     self.next_btn.deleteLater()

    # def show_result(self):
    #     result_str = ''.join(self.results)
    #     result_label = QtWidgets.QLabel(f"Your personality type is: {result_str}")
    #     self.layout.addWidget(result_label)

    # def process_answer(self):
    #     selected_trait = None
    #     for i, button in enumerate(self.option_buttons):
    #         if button.isChecked():
    #             selected_trait = self.questions[self.current_question]['traits'][i]
    #             break

    #     if selected_trait:
    #         self.results.append(selected_trait)
    #         self.clear_question()
    #         self.current_question += 1

    #         if self.current_question < len(self.questions):
    #             self.display_question(self.current_question)
    #         else:
    #             self.show_result()


    def retranslateUi(self, PersonalityTest):
        _translate = QtCore.QCoreApplication.translate
        PersonalityTest.setWindowTitle(_translate("PersonalityTest", "Form"))
        self.logout.setText(_translate("PersonalityTest", "Logout"))
        self.next_btn.setText(_translate("PersonalityTest", "Next"))
        self.back_btn.setText(_translate("PersonalityTest", "Back"))
        self.main_btn.setText(_translate("PersonalityTest", "Main Menu"))
        self.Question_No.setText(_translate("PersonalityTest", "Question 1"))
        self.Question_area.setText(_translate("PersonalityTest", "You feel more energetic when:"))
        self.radioButton1.setText(_translate("PersonalityTest", "Socializing with others"))
        self.radioButton2.setText(_translate("PersonalityTest", "Spending time alone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PersonalityTest = QtWidgets.QWidget()
    ui = Ui_PersonalityTest()
    ui.setupUi(PersonalityTest)
    PersonalityTest.show()
    sys.exit(app.exec_())
