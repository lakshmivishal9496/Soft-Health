import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi, loadUiType
import sqlite3
import re
from personality import Personality


class PersonalityTestApp(QDialog):
    def __init__(self):
        super(PersonalityTestApp, self).__init__()
        loadUi(r"static\personality.ui", self)
        self.logout.clicked.connect(self.show_back)
        self.questions = [
            {
                'question': 'You feel more energetic when:',
                'options': ['Socializing with others', 'Spending time alone'],
                'traits': ['E', 'I']
            },
            {
                'question': 'You focus more on:',
                'options': ['Facts and details', 'Big picture and possibilities'],
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
            # Add more questions here...
        ]
        self.current_question = 0
        self.selected_answers = []

        self.display_question()

        self.next_btn.clicked.connect(self.next_question)
        self.back_btn.clicked.connect(self.previous_question)
        self.main_btn.clicked.connect(self.show_main_menu)

    def display_question(self):
        question = self.questions[self.current_question]
        self.Question_No.setText(f"Question {self.current_question + 1}")
        self.Question_area.setText(question['question'])
        self.radioButton1.setText(question['options'][0])
        self.radioButton2.setText(question['options'][1])

    def next_question(self):
        selected_answer = ""
        if self.radioButton1.isChecked():
            selected_answer = self.questions[self.current_question]['traits'][0]
        elif self.radioButton2.isChecked():
            selected_answer = self.questions[self.current_question]['traits'][1]
        
        if selected_answer:
            self.selected_answers.append(selected_answer)
            self.current_question += 1

            if self.current_question < len(self.questions):
                self.display_question()
                self.radioButton1.setChecked(False)
                self.radioButton2.setChecked(False)
            else:
                self.show_result()
        else:
            QMessageBox.warning(self, "Error", "Please select an option.")

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.display_question()
            self.radioButton1.setChecked(False)
            self.radioButton2.setChecked(False)

    def show_result(self):
        if len(self.selected_answers) < len(self.questions):
            QMessageBox.warning(self, "Error", "Please answer all the questions.")
            return

        result = self.selected_answers[0] + self.selected_answers[1] + self.selected_answers[2] + self.selected_answers[3]  # Call the appropriate function to calculate the personality result

        # Display the result or perform any other actions based on the result
        QMessageBox.information(self, "Personality Result", f"Your personality result is: {result}")
        self.show_back()

    def show_back(self):
        widget.setCurrentIndex(0)

    def show_main_menu(self):
        widget.setCurrentIndex(4)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
personalityform = PersonalityTestApp()
widget.addWidget(personalityform)
widget.setCurrentIndex(0)
