import sys
import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QWidget
from PyQt5.uic import loadUi
import sqlite3
import re
import personality_quiz


class LoginApp(QDialog):
    # Deals with login screen for the app

    # load the UI file using an relative path
    def __init__(self):
        super(LoginApp, self).__init__()
        loadUi(r"static\login.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_register)
        self.b5.clicked.connect(self.guest_login)

    def login(self):
        un = self.tb1.text()
        pw = self.tb2.text()
        # connect to the database and
        # check if the username and password are valid
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM login \
                       WHERE username = ? AND password = ?', (un, pw))
        user = cursor.fetchone()
        # check if username and password are provided
        if not un or not pw:
            QMessageBox.warning(self, "Login Error",
                                "Username and password are required")
            return

        # display an error message if the username and password are not valid
        if user is None:
            QMessageBox.warning(self, "Login Error",
                                "Invalid username or password")
            return

        # display a message box asking the user
        #  if they want to take a personality assessment
        widget.setCurrentIndex(4)

        db.close()
        self.tb1.setText("")
        self.tb2.setText("")

    def show_register(self):
        widget.setCurrentIndex(1)

    def guest_login(self):
        widget.setCurrentIndex(3)


class RegApp(QDialog):
    def __init__(self):
        super(RegApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\register.ui", self)

        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)

    def verify_password(self, password):
        if len(password) < 8 and (re.search('[0-9]', password) is None or re.search('[A-Z]', password) is None or re.search('[a-z]', password) is None or re.search('[@#&]', password) is None):
            return "Password must contain: \n " + "*minimum 8 characters,\n " +  "*a number \n " + "*a uppercase letter \n"+ "*a lowercase letter \n"+ "*a special character \n"
        else:
            return None

    def reg(self):
        un = self.tb3.text()
        pw = self.tb4.text()
        em = self.tb5.text()
        repw = self.tb6.text()
        # print(un)
        # print(pw)
        # print(em)
        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS login (
                           username TEXT,
                           password TEXT,
                           email TEXT)
                       ''')

        error_message = self.verify_password(pw)
        if not un or not pw or not em:
            QMessageBox.warning(self, "Registration Error",
                                "Please fill in all the fields")
        else:
            if error_message:
                QMessageBox.warning(self, "Registration Error", error_message)
            elif pw != repw:
                QMessageBox.warning(self, "Registration Error",
                                    "Passwords do not match.")
            else:
                cursor.execute('''
                    INSERT INTO login (username, password, email)
                    VALUES (?,?,?)
                    ''', (un, pw, em))
                db.commit()
                db.close()
                QMessageBox.information(self, "Login Output",
                                        "User registered successfully.\
                                        Please login to continue.")
            QApplication.processEvents()
            self.tb3.setText("")
            self.tb4.setText("")
            self.tb5.setText("")
            self.tb6.setText("")

    def show_login(self):
        widget.setCurrentIndex(0)


class HomeApp(QDialog):
    def __init__(self):
        super(HomeApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\home.ui", self)
        self.b5_2.clicked.connect(self.show_back)
        self.b5.clicked.connect(self.p_test)
        self.b8.clicked.connect(self.show_quotes)

    def show_quotes(self):
        widget.setCurrentIndex(6)

    def show_back(self):
        widget.setCurrentIndex(0)

    def p_test(self):
        widget.setCurrentIndex(5)

# class PersonalityApp(QDialog):
#     def __init__(self):
#         super(PersonalityApp, self).__init__()
#         # pass super class LoginApp to parent class
#         loadUi(r"static\personality.ui", self)
#         self.logout.clicked.connect(self.show_back)

#     def show_back(self):
#         widget.setCurrentIndex(0)


class PersonalityApp(QDialog):
    def __init__(self):
        super(PersonalityApp, self).__init__()
        loadUi(r"static\personality.ui", self)
        self.logout.clicked.connect(self.show_back)
        self.questions = personality_quiz.questions
        self.current_question = 0
        self.selected_answers = []
        self.result = ''
        self.display_question()

        self.next_btn.clicked.connect(self.next_question)
        self.back_btn.clicked.connect(self.previous_question)
        self.main_btn.clicked.connect(self.show_main_menu)
    
    def reset(self):
        self.current_question = 0
        self.selected_answers = []
        self.result = ''
        self.display_question()

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
                if self.current_question == 0:
                    self.next_btn.setDisabled(True)
                else:
                    self.display_question()
                    self.radioButton1.setAutoExclusive(False)
                    self.radioButton2.setAutoExclusive(False)
                    self.radioButton1.setChecked(False)
                    self.radioButton2.setChecked(False)
                    self.radioButton1.setAutoExclusive(True)
                    self.radioButton2.setAutoExclusive(True)
            else:
                self.show_result()
        else:
            QMessageBox.warning(self, "Error", "Please select an option.")

    def previous_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.selected_answers.pop()
            self.display_question()
            self.radioButton1.setChecked(False)
            self.radioButton2.setChecked(False)

    def show_result(self):
        if len(self.selected_answers) < len(self.questions):
            QMessageBox.warning(self, "Error", "Please answer all the questions.")
            return
        else:
            self.result = self.selected_answers[0] + self.selected_answers[1] + self.selected_answers[2] + self.selected_answers[3]
            personality_result = personality_quiz.personality_list.get(self.result)
            recommendation = personality_quiz.personality_recommendation.get(self.result)

            message_box = QMessageBox()
            message_box.setWindowTitle("Personality Result")

            # Set the text format to display HTML
            message_box.setTextFormat(QtCore.Qt.RichText)

            # Construct the message using HTML formatting
            message = f"<p><b>Your personality result is:</b> {self.result} - {personality_result}</p>"
            message += f"<p><b>Recommendation for you:</b></p>"
            message += f"<p>{recommendation}</p>"

            message_box.setText(message)

            # Add a custom Ok button and apply stylesheet
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(131, 53, 151); color: white; font-weight: bold; padding: 5px 10px;")

            message_box.exec_()
        self.show_main_menu()
        self.current_question = 0
            #self.show_recommendation()
            # return self.result      

    def show_back(self):
        widget.setCurrentIndex(0)
    # def show_recommendation(self):
    #     widget.setCurrentIndex(6)
        # recom = RecommendationApp()
        # recom.display_recommendation(self.result)

    def show_main_menu(self):
        self.reset()
        widget.setCurrentIndex(4)

    


# class RecommendationApp(QDialog):
#     def __init__(self):
#         super(RecommendationApp, self).__init__()
#         # pass super class Recommendation to parent class
#         loadUi(r"static\recommendation.ui", self)
#         self.logout.clicked.connect(self.goback)
#         # self.b1.clicked.connect(self.display_recommendation)
#         personality_type = PersonalityApp()
#         # p_type = personality_type.show_result()
#     def display_recommendation(self, personality_result):
#         # Assuming `personality_result` is the variable storing the personality type
#         recommendation = personality.personality_recommendation.get(personality_result)
#         if recommendation:
#             self.recom_area.setText(recommendation)
#         else:
#             self.recom_area.setText("No recommendation found for this personality type.")

#     def goback(self):
#         widget.setCurrentIndex(0)

class QuotesApp(QDialog):
    def __init__(self):
        super(QuotesApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\quotes.ui", self)
        self.main_btn.clicked.connect(self.show_main_menu)
        self.logout.clicked.connect(self.show_logout)
    def show_main_menu(self):
        widget.setCurrentIndex(4)

    def show_logout(self):
        widget.setCurrentIndex(0)


class mainMenuApp(QDialog):
    def __init__(self):
        super(mainMenuApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\mainmenu.ui", self)
        self.b9.clicked.connect(self.menu)
        self.b5_2.clicked.connect(self.show_back)
        self.b5.clicked.connect(self.show_personality)

    def show_personality(self):
        personalityform.current_question = 0
        widget.setCurrentIndex(5)

    def show_back(self):
        widget.setCurrentIndex(0)

    def menu(self):
        widget.setCurrentIndex(2)


class GuestApp(QDialog):
    def __init__(self):
        super(GuestApp, self).__init__()
        # pass super class GuestApp to parent class
        loadUi(r"static\guest.ui", self)
        self.quotes_btn.clicked.connect(self.show_quotes)
        self.signupmore_btn.clicked.connect(self.show_sign_up)

    def show_quotes(self):
        widget.setCurrentIndex(6)

    def show_sign_up(self):
        widget.setCurrentIndex(1)


class Verify:
    def __init__(self, password):
        self.password = password

    def compare(self, other_password):
        return self.password == other_password


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
# Connects both login and register widgets together
loginform = LoginApp()
registrationform = RegApp()
Homeform = HomeApp()
guestform = GuestApp()
mainMenuform = mainMenuApp()
personalityform = PersonalityApp()
quotes = QuotesApp()
# recommendationform = RecommendationApp()
widget.addWidget(loginform)
widget.addWidget(registrationform)
widget.addWidget(Homeform)
widget.addWidget(guestform)
widget.addWidget(mainMenuform)
widget.addWidget(personalityform)
widget.addWidget(quotes)
# widget.addWidget(recommendationform)
widget.setCurrentIndex(0)
widget.setFixedWidth(1024)
widget.setFixedHeight(768)

widget.show()
sys.exit(app.exec_())
