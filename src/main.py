'''Main program to run the application'''
import sys
import os
import sqlite3
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QPushButton, QLabel, QScrollArea, QWidget, QVBoxLayout, QDialogButtonBox
from PyQt5.uic import loadUi
import personality_quiz


class ScrollableMessageBox(QDialog):
    def __init__(self, title, text):
        super().__init__()

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon())

        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)

        widget = QWidget(self)
        scroll.setWidget(widget)

        layout = QVBoxLayout(widget)
        label = QLabel(text, self)
        layout.addWidget(label)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(scroll)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok, self)
        buttonBox.button(QDialogButtonBox.Ok).setText("I Understand")
        buttonBox.accepted.connect(self.accept)
        self.layout.addWidget(buttonBox)
        self.setWindowIcon(QIcon('static/images/icon.png'))
        self.setMinimumSize(560, 350)


class LoginApp(QDialog):
    ''' Initialize the widget'''

    # load the UI file using an relative path
    def __init__(self):
        ''' Initialize login screen for the login app'''
        super(LoginApp, self).__init__()
        loadUi(r"static\login.ui", self)
        self.b1.clicked.connect(self.login)
        self.b2.clicked.connect(self.show_register)
        self.b5.clicked.connect(self.guest_login)
        self.tb1.returnPressed.connect(self.login)
        self.tb2.returnPressed.connect(self.login)
        self.agreement_label.mousePressEvent = self.show_user_agreement
        self.privacy_label.mousePressEvent = self.show_privacy_policy

    def show_user_agreement(self, event):
        with open('static/text/user_agreement.txt', 'r') as file:
            agreement_text = file.read()
        dialog = ScrollableMessageBox("User Agreement", agreement_text)
        dialog.exec_()

    def show_privacy_policy(self, event):
        with open('static/text/privacy_policy.txt', 'r', encoding='utf-8-sig') as file:
            privacy_text = file.read()
        dialog = ScrollableMessageBox("Privacy Policy", privacy_text)
        dialog.exec_()

    def show_custom_message(self, message_type, title, message):
        msg = QMessageBox()
        msg.setIcon(message_type)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def login(self):
        ''' Deals with login function for the login app'''
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
            self.show_custom_message(QMessageBox.Warning, "Login Error",
                                     "Username and password are required")
            return

        # display an error message if the username and password are not valid
        if user is None:
            self.show_custom_message(QMessageBox.Warning, "Login Error",
                                     "Invalid username or password")
            return

        # display a message box asking the user
        #  if they want to take a personality assessment
        widget.setCurrentIndex(4)

        db.close()
        self.tb1.setText("")
        self.tb2.setText("")

    def show_register(self):
        ''' Deals with registration screen for the login app'''
        widget.setCurrentIndex(1)

    def guest_login(self):
        ''' Deals with guest login screen for the login app'''
        widget.setCurrentIndex(3)


class RegApp(QDialog):
    ''' Initialize the widget'''
    def __init__(self):
        ''' Initialize registration screen for the registration app'''
        super(RegApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\register.ui", self)

        self.b3.clicked.connect(self.reg)
        self.b4.clicked.connect(self.show_login)
        

        self.tb4.setTabOrder(self.tb4, self.tb6)
        self.tb4.setTabOrder(self.tb6, self.b3)
        self.tb3.returnPressed.connect(self.reg)
        self.tb4.returnPressed.connect(self.reg)
        self.tb6.returnPressed.connect(self.reg)

    def show_custom_message(self, message_type, title, message):
        msg = QMessageBox()
        msg.setIcon(message_type)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setWindowIcon(QIcon('static/images/icon.png'))
        msg.exec_()

    def verify_password(self, password):
        ''' Deals with password validation'''
        char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', '~', ',', '.', ':', '\"', '\'']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        if len(password) < 8:
            return "Password must be at least 8 characters long"
        elif not any(char in password for char in char):
            return  "Password must contain:\n" + "*minimum 8 characters,\n" + "*a number\n" + "*an uppercase letter\n"+ "*a lowercase letter\n"+ "*a special character\n"
        elif not any(num in password for num in numbers):
            return  "Password must contain:\n" + "*minimum 8 characters,\n" + "*a number\n" + "*an uppercase letter\n"+ "*a lowercase letter\n"+ "*a special character\n"
        elif not any(upper_case in password for upper_case in upper):
            return  "Password must contain:\n" + "*minimum 8 characters,\n" + "*a number\n" + "*an uppercase letter\n"+ "*a lowercase letter\n"+ "*a special character\n"
        elif not any(lower_case in password for lower_case in lower):
            return  "Password must contain:\n" + "*minimum 8 characters,\n" + "*a number\n" + "*an uppercase letter\n"+ "*a lowercase letter\n"+ "*a special character\n"
        if password != self.tb6.text():
            return "Passwords must match"
        else:
            return None


    def reg(self):
        ''' Deals with registration'''
        un = self.tb3.text()
        pw = self.tb4.text()
        repw = self.tb6.text()

        db = sqlite3.connect('softhealth.db')
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS login (
                           username TEXT,
                           password TEXT)''')
        
        # Check if username already exists
        cursor.execute("SELECT * FROM login WHERE username=?", (un,))
        result = cursor.fetchone()
        if result:
            QMessageBox.warning(self, "Registration Error", "Username already exists.")
            return

        error_message = self.verify_password(pw)
        if not un or not pw:
            QMessageBox.warning(self, "Registration Error",
                                "Please fill in all the fields")
        else:
            if error_message:
                QMessageBox.warning(self, "Registration Error", error_message)
            elif pw != repw:
                QMessageBox.warning(self, "Registration Error.\nPasswords do not match.")
            else:
                cursor.execute('''
                    INSERT INTO login (username, password)
                    VALUES (?,?)
                    ''', (un, pw))
                db.commit()
                db.close()
                QMessageBox.information(self, "Login Output",
                                        "User registered successfully.\nPlease login to continue.")
                self.show_login()
            QApplication.processEvents()
            self.tb3.setText("")
            self.tb4.setText("")
            self.tb6.setText("")


    def show_login(self):
        ''' Deals with showing login screen for the registration app'''
        widget.setCurrentIndex(0)


class MainMenuapp(QDialog):
    ''' Deals with Home screen for the home app'''
    def __init__(self):
        ''' Initialize the widget'''
        super(MainMenuapp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\main_menu.ui", self)
        self.b5_2.clicked.connect(self.show_back)
        self.b5.clicked.connect(self.p_test)
        self.b8.clicked.connect(self.show_quotes)
        self.b7.clicked.connect(self.show_stress)
        self.b6.clicked.connect(self.show_music)
        self.b11.clicked.connect(self.show_resources)

    def show_quotes(self):
        ''' Deals with showing quotes for the home app'''
        widget.setCurrentIndex(6)

    def show_back(self):
        ''' Deals with back button for the home app'''
        widget.setCurrentIndex(0)

    def p_test(self):
        ''' Deals with personality test for the app'''
        widget.setCurrentIndex(5)

    def show_stress(self):
        ''' Deals with stress relief for the home app'''
        widget.setCurrentIndex(7)

    def show_music(self):
        ''' Deals with music for the home app'''
        widget.setCurrentIndex(10)

        ''' Deals with resources for the home app'''
    def show_resources(self):
        widget.setCurrentIndex(11)


class PersonalityApp(QDialog):
    ''' Deals with personality screen for the app'''
    def __init__(self):
        ''' Initialize the widget'''
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
        ''' Deals with reset option for the personality'''
        self.current_question = 0
        self.selected_answers = []
        self.result = ''
        self.display_question()

    def display_question(self):
        ''' Deals with question for the personlaity app'''

        question = self.questions[self.current_question]
        self.Question_No.setText(f"Question {self.current_question + 1}")
        self.Question_area.setText(question['question'])
        self.radioButton1.setText(question['options'][0])
        self.radioButton2.setText(question['options'][1])

    def next_question(self):
        '''Deals with next button for the personality app'''
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
            message_box = QMessageBox()
            message_box.setWindowIcon(QIcon('static\images\icon.png'))
            message_box.setWindowTitle("Error")
            message_box.setText("Please select an option.")

            # Add a custom Ok button with 3D styling and color
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(131, 53, 151);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_()

    def previous_question(self):
        ''' Set previous question'''
        if self.current_question > 0:
            self.current_question -= 1
            self.selected_answers.pop()
            self.display_question()
            self.radioButton1.setChecked(False)
            self.radioButton2.setChecked(False)

    def show_result(self):
        '''Display the result'''
        if len(self.selected_answers) < len(self.questions):
            QMessageBox.warning(self, "Error", "Please answer all the questions.")
            return
        else:
            self.result = self.selected_answers[0] \
              + self.selected_answers[1] \
              + self.selected_answers[2] \
              + self.selected_answers[3]
            personality_result = personality_quiz.personality_list.get(self.result)
            recommendation = personality_quiz.personality_recommendation.get(self.result)
            quote = personality_quiz.personality_quote.get(self.result)
            message_box = QMessageBox()
            message_box.setWindowIcon(QIcon('static\images\icon.png'))
            message_box.setWindowTitle("Personality Test Result - SoftHealth")
            message_box.setTextFormat(QtCore.Qt.RichText)
            # Construct the message using HTML formatting
            message = f"<b>Your personality result is:</b>\
<br>{self.result} - {personality_result}<br><br>"
            message += f"<b>Recommendation to improve your mental health:</b><br>"
            message += f"{recommendation}<br><br>"
            message += f"<b>Your personality quote:<br></b>"
            message += f"{quote}"
            message_box.setText(message)
            # Add a custom Ok button and apply stylesheet
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(131, 53, 151);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")
            message_box.exec_()
        self.show_main_menu()
        self.current_question = 0

    def show_back(self):
        ''' Show the back button    '''
        widget.setCurrentIndex(0)

    def show_main_menu(self):
        ''' Show the main menu '''
        self.reset()
        widget.setCurrentIndex(2)


class QuotesApp(QDialog):
    ''' Provides the ability to interact with the Quotes'''
    def __init__(self):
        ''' Initialize the widget'''
        super(QuotesApp, self).__init__()
        loadUi(r"static\quotes.ui", self)
        self.logout.clicked.connect(self.show_back)
        self.quotes = ["I'm not a product of my circumstances. I am a product of my decisions.",
                    "It's not what we have in life, but who we have in our life that matters.",
                    "Life is either a daring adventure or nothing at all.",
                    "Your time is limited, don't waste it living someone else's life."]
        self.authors = ["Stephen Covey", "Unknown", "Helen Keller", "Steve Jobs"]
        self.current_quote = 0
        self.display_quote()

        self.next_btn.clicked.connect(self.next_quote)
        self.back_btn.clicked.connect(self.previous_quote)
        self.main_btn.clicked.connect(self.show_main_menu)

    def display_quote(self):
        '''Display the quote'''
        quote = self.quotes[self.current_quote]
        author = self.authors[self.current_quote]
        self.quote_area.setText(quote)
        self.label_2.setText(author)

    def next_quote(self):
        '''Return the next quote'''
        if self.current_quote < len(self.quotes) - 1:
            self.current_quote += 1
            self.display_quote()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("End of Quotes")
            message_box.setText("You have reached the end of the quotes.")
            message_box.setWindowIcon(QIcon('static\images\icon.png'))

            # Add a custom Ok button with 3D styling
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(102, 203, 0);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_()

    def previous_quote(self):
        '''Return the previous quote'''
        if self.current_quote > 0:
            self.current_quote -= 1
            self.display_quote()
        else:
            pass

    def show_back(self):
        ''' Show the back button'''
        self.reset()
        widget.setCurrentIndex(0)

    def show_main_menu(self):
        ''' Menu function'''
        self.reset()
        widget.setCurrentIndex(2)
    
    def reset(self):
        ''' Reset the widget'''
        self.current_quote = 0
        self.display_quote()


class GuestQuotesApp(QDialog):
    def __init__(self):
        '''Initialize the menu'''
        super(GuestQuotesApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\guest_quotes.ui", self)
        self.back_btn.clicked.connect(self.previous_quote)
        self.next_btn.clicked.connect(self.next_quote)
        self.guestMenu_btn.clicked.connect(self.show_guest_menu)
        self.quotes = ["I'm not a product of my circumstances. I am a product of my decisions.",
                    "It's not what we have in life, but who we have in our life that matters.",
                    "Life is either a daring adventure or nothing at all.",
                    "Your time is limited, don't waste it living someone else's life."]
        self.authors = ["Stephen Covey", "Unknown", "Helen Keller", "Steve Jobs"]
        self.current_quote = 0
        self.display_quote()

    def display_quote(self):
        '''Display the quote'''
        quote = self.quotes[self.current_quote]
        author = self.authors[self.current_quote]
        self.quote_area.setText(quote)
        self.label_2.setText(author)
    
    def next_quote(self):
        '''Return the next quote'''
        if self.current_quote < len(self.quotes) - 1:
            self.current_quote += 1
            self.display_quote()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("End of Quotes")
            message_box.setText("You have reached the end of the quotes.")
            message_box.setWindowIcon(QIcon('static\images\icon.png'))

            # Add a custom Ok button with 3D styling
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(102, 203, 0);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_()
    
    def previous_quote(self):
        '''Return the previous quote'''
        if self.current_quote > 0:
            self.current_quote -= 1
            self.display_quote()
        else:
            pass

    def show_guest_menu(self):
        ''' Show the guest menu'''
        self.reset()
        widget.setCurrentIndex(3)
    
    def reset(self):
        ''' Reset the widget'''
        self.current_quote = 0
        self.display_quote()


class UserExercisesApp(QDialog):
    '''Exercises App'''
    def __init__(self):
        '''Construct instance'''
        super(UserExercisesApp, self).__init__()
        loadUi(r"static\exercises.ui", self)
        self.logout.clicked.connect(self.show_back)
        self.main_btn.clicked.connect(self.show_main_menu)
        self.exercises = ["<b>Hit the pillow:</b><br><br> Locate a soft pillow, hit it for half a minute, and afterward reflect on your emotions.",
                          "<b>Deep breathing exercises:</b><br><br> Find a quiet spot, inhale deeply, and exhale completely, focusing on your breath.",
                          "<b>Mind-body practices:</b><br><br> Choose a peaceful space, perform easy yoga poses, and concentrate on your breathing.",
                          "<b>Gratitude journaling:</b><br><br> Acquire a notepad, write down three things you appreciate, and spend time reflecting daily."]
        self.images = ["static/images/001.jpg", "static/images/002.jpg", "static/images/003.jpg", "static/images/004.jpg"]
        self.current_exercise = 0
        self.display_exercise()

        self.next_btn.clicked.connect(self.next_exercise)
        self.back_btn.clicked.connect(self.previous_exercise)
        self.main_btn.clicked.connect(self.show_main_menu)

    def display_exercise(self):
        exercise = self.exercises[self.current_exercise]
        image_path = self.images[self.current_exercise]
        self.Exercise.setText(exercise)
        self.set_image(image_path)

    def set_image(self, image_path):
        style = f"border: 1px solid black; border-radius: 10px; padding: 0px; border-image: url({image_path}) 10 10 10 10 stretch stretch;"
        self.picture.setStyleSheet(style)

    def next_exercise(self):
        if self.current_exercise < len(self.exercises) - 1:
            self.current_exercise += 1
            self.display_exercise()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("End of Exercises")
            message_box.setText("You have reached the end of the exercises.")
            message_box.setWindowIcon(QIcon('static\images\icon.png'))

            # Add a custom Ok button with 3D styling
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(255, 136, 4);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_()

    def previous_exercise(self):
        if self.current_exercise > 0:
            self.current_exercise -= 1
            self.display_exercise()
        else:
            pass
            """message_box = QMessageBox()
            message_box.setWindowTitle("Error")
            message_box.setText("This is the first exercise.")

            # Add a custom Ok button with 3D styling
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(255, 136, 4);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_() """

    def show_main_menu(self):
        ''' Show the main menu'''
        self.reset()
        widget.setCurrentIndex(2)

    def show_back(self):
        ''' Show the back button'''
        self.reset()
        widget.setCurrentIndex(0)
    
    def reset(self):
        ''' Reset the widget'''
        self.current_exercise = 0
        self.display_exercise()


class GuestExerciseApp(QDialog):
    '''Guest Exercise App'''
    def __init__(self):
        '''Construct instance'''
        super(GuestExerciseApp, self).__init__()
        loadUi(r"static\guest_exercises.ui", self)
        self.guestMenu_btn.clicked.connect(self.show_guest_menu)
        self.exercises = ["<b>Hit the pillow:</b><br><br> Locate a soft pillow, hit it for half a minute, and afterward reflect on your emotions.",
                          "<b>Deep breathing exercises:</b><br><br> Find a quiet spot, inhale deeply, and exhale completely, focusing on your breath.",
                          "<b>Mind-body practices:</b><br><br> Choose a peaceful space, perform easy yoga poses, and concentrate on your breathing.",
                          "<b>Gratitude journaling:</b><br><br> Acquire a notepad, write down three things you appreciate, and spend time reflecting daily."]
        self.images = ["static/images/001.jpg", "static/images/002.jpg", "static/images/003.jpg", "static/images/004.jpg"]
        self.current_exercise = 0
        self.display_exercise()

        self.next_btn.clicked.connect(self.next_exercise)
        self.back_btn.clicked.connect(self.previous_exercise)
        self.guestMenu_btn.clicked.connect(self.show_guest_menu)

    def display_exercise(self):
        exercise = self.exercises[self.current_exercise]
        image_path = self.images[self.current_exercise]
        self.Exercise.setText(exercise)
        self.set_image(image_path)

    def set_image(self, image_path):
        style = f"border: 1px solid black; border-radius: 10px; padding: 0px; border-image: url({image_path}) 10 10 10 10 stretch stretch;"
        self.picture.setStyleSheet(style)

    def next_exercise(self):
        if self.current_exercise < len(self.exercises) - 1:
            self.current_exercise += 1
            self.display_exercise()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("End of Exercises")
            message_box.setText("You have reached the end of the exercises.")
            message_box.setWindowIcon(QIcon('static\images\icon.png'))

            # Add a custom Ok button with 3D styling and color
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(255, 136, 4);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_()

    def previous_exercise(self):
        if self.current_exercise > 0:
            self.current_exercise -= 1
            self.display_exercise()
        else:
            pass
            """ message_box = QMessageBox()
            message_box.setWindowTitle("Sorry!")
            message_box.setText("This is the first exercise.")

            # Add a custom Ok button with 3D styling and color
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(255, 136, 4);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")

            message_box.exec_() """
            
    def show_guest_menu(self):
        ''' Show the guest menu'''
        self.reset()
        widget.setCurrentIndex(3)
    
    def reset(self):
        ''' Reset the widget'''
        self.current_exercise = 0
        self.display_exercise()


class UserMusicApp(QDialog):
    '''User Music App'''

    def __init__(self):
        '''Construct instance'''
        super(UserMusicApp, self).__init__()
        loadUi(r"static\music.ui", self)

        self.media_player = QMediaPlayer(self)
        self.music_files = ['Yoga Style - Chris Haugen.mp3', 'Lazy Walk - Cheel.mp3', 'First Dream - Brian Bolger.mp3', 'Interstellar Mood - Nico Staf.mp3']
        self.current_music_index = 0
        self.init_music()
        self.play_btn = self.findChild(QPushButton, 'play_btn')
        self.pause_btn = self.findChild(QPushButton, 'pause_btn')
        self.mute = self.findChild(QPushButton, 'mute')
        self.plus = self.findChild(QPushButton, 'plus')
        self.minus = self.findChild(QPushButton, 'minus')
        self.next_btn = self.findChild(QPushButton, 'next_btn')
        self.back_btn = self.findChild(QPushButton, 'back_btn')
        self.now_playing_label = self.findChild(QLabel, 'now_playing_label')
        self.media_player.stateChanged.connect(self.update_label)

        self.logout.clicked.connect(self.show_back)
        self.main_btn.clicked.connect(self.show_main_menu)

        self.play_btn.clicked.connect(self.play_audio)
        self.pause_btn.clicked.connect(self.pause_audio)
        self.mute.clicked.connect(self.toggle_mute)
        self.plus.clicked.connect(self.increase_volume)
        self.minus.clicked.connect(self.decrease_volume)
        self.next_btn.clicked.connect(self.next_audio)
        self.back_btn.clicked.connect(self.previous_audio)

        self.is_muted = False
        self.media_player.mediaStatusChanged.connect(self.media_status_changed)

    def init_music(self):
        self.load_audio(os.path.join('static', 'music', self.music_files[self.current_music_index]))

    def load_audio(self, file_path):
        self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_path)))
        file_name, _ = os.path.splitext(os.path.basename(file_path))

    def update_label(self, state):
        if state == QMediaPlayer.PlayingState:
            file_name, _ = os.path.splitext(os.path.basename(self.music_files[self.current_music_index]))
            self.now_playing_label.setText(f"Now Playing: {file_name}")

    def play_audio(self):
        self.media_player.play()

    def pause_audio(self):
        self.media_player.pause()
        self.now_playing_label.setText("Paused")

    def toggle_mute(self):
        if self.is_muted:
            # If currently muted, set volume to 25 and switch the flag
            self.media_player.setVolume(50)
            self.is_muted = False
            current_file = os.path.basename(self.music_files[self.current_music_index])
            file_name_without_extension = os.path.splitext(current_file)[0]
            self.now_playing_label.setText(f"Now Playing: {file_name_without_extension}")
        else:
            # If currently not muted, set volume to 0 and switch the flag
            self.media_player.setVolume(0)
            self.is_muted = True
            self.now_playing_label.setText("Muted")

    def increase_volume(self):
        volume = self.media_player.volume()
        volume += 5
        self.media_player.setVolume(volume)
        current_file = os.path.basename(self.music_files[self.current_music_index])
        file_name_without_extension = os.path.splitext(current_file)[0]
        self.now_playing_label.setText(f"Now Playing: {file_name_without_extension}")   

    def decrease_volume(self):
        volume = self.media_player.volume()
        volume -= 5
        self.media_player.setVolume(volume)

    def next_audio(self):
        self.current_music_index += 1
        if self.current_music_index >= len(self.music_files):
            self.current_music_index = 0
        self.load_audio(os.path.join('static', 'music', self.music_files[self.current_music_index]))
        self.play_audio()

    def previous_audio(self):
        if self.current_music_index > 0:
            self.current_music_index -= 1
            self.load_audio(os.path.join('static', 'music', self.music_files[self.current_music_index]))
            self.play_audio()

    def media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.next_audio()

    def show_back(self):
        ''' Show the back button'''
        self.current_music_index = 0
        self.load_audio(os.path.join('static', 'music', self.music_files[self.current_music_index]))
        self.now_playing_label.setText("")
        widget.setCurrentIndex(0)
        self.media_player.stop()

    def show_main_menu(self):
        ''' Show the main menu'''
        self.current_music_index = 0
        self.load_audio(os.path.join('static', 'music', self.music_files[self.current_music_index]))
        self.now_playing_label.setText("")
        widget.setCurrentIndex(2)
        self.media_player.stop()


class ResourcesApp(QDialog):
    def __init__(self):
        '''Initialize the resources widget'''
        super(ResourcesApp, self).__init__()
        loadUi(r"static\resources.ui", self)
        self.copy_link_btn = self.findChild(QPushButton, 'copy_link_btn')

        self.logout.clicked.connect(self.show_back)
        self.main_btn.clicked.connect(self.show_main_menu)
        self.resources = ["<b>The Science of Being Well:</b><br><br> The Science of Being Well" "by Wallace D. Wattles is a self-help book that focuses on the connection between physical health and mental well-being. It emphasizes the importance of cultivating positive thoughts and beliefs to promote well-being.",
                          "<b>The Way of Peace:</b><br><br> The Way of Peace by James Allen is a self-help book that encourages readers to find inner peace and harmony through meditation and positive thinking. It also discusses the importance of cultivating a positive mindset to achieve success in life.",
                          "<b>Youtube video 1:</b><br><br> This video is a self-help guide designed to help readers manage stress and anxiety through a variety of techniques, believing in yourself, self-well-being strategies, and mindfulness practices.",
                          "<b>Youtube video 2:</b><br><br> This video explores the importance of living in the present moment and offers practical guidance for reducing stress and anxiety by focusing on the present rather than dwelling on the past or worrying about the future."]
        self.images = ["static/images/res001.jpg", "static/images/res002.jpg", "static/images/res003.jpg", "static/images/res004.jpg"]
        self.link_list = ["https://amzn.eu/d/5EQoG9W", "https://amzn.eu/d/hboP0rl", "https://youtu.be/R6MasOctLkY", "https://youtu.be/dFJ9csOJ_N8"]
        self.current_link_index = 0
     
        self.current_resource = 0
        self.current_image = 0
        self.display_resource()
        self.next_btn.clicked.connect(self.show_next_resource)
        self.next_btn.clicked.connect(self.next_link)
        self.back_btn.clicked.connect(self.show_previous_resource)
        self.back_btn.clicked.connect(self.previous_link)
        self.main_btn.clicked.connect(self.show_main_menu)
        self.copy_link_btn.mousePressEvent = self.copy_link_btn_clicked  

    def copy_link_btn_clicked(self, event):
        # Copy the first link from the list to the clipboard
        # Here, you can customize to select the link based on your requirement
        link_to_copy = self.link_list[self.current_link_index]
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(link_to_copy, mode=cb.Clipboard)
        self.copy_link_btn.setText('Link Copied!')

    def display_resource(self):
        resource = self.resources[self.current_resource]
        image_path = self.images[self.current_resource]
        self.ResourceArea.setText(resource)
        self.set_image(image_path)

    def set_image(self, image_path):
        style = f"border: 1px solid black; border-radius: 10px; padding: 0px; border-image: url({image_path}) 10 10 10 10 stretch stretch;"
        self.picture.setStyleSheet(style)

    def show_next_resource(self):
        if self.current_resource < len(self.resources) - 1:
            self.current_resource += 1
            self.display_resource()
        else:
            message_box = QMessageBox()
            message_box.setWindowTitle("End of External Resources")
            message_box.setText("You have reached the end of the External Resources.")
            message_box.setWindowIcon(QIcon('static\images\icon.png'))

            # Add a custom Ok button with 3D styling
            ok_button = message_box.addButton(QMessageBox.Ok)
            ok_button.setStyleSheet("background-color: rgb(100, 79, 130);\
                                    color: white; font-weight: bold; \
                                    padding: 5px 10px; border: none; \
                                    border-radius: 5px;")
            message_box.exec_()
        self.copy_link_btn.setText('Click to copy link')

    def next_link(self):
        # Move to the next link in the list, if available
        if self.current_link_index < len(self.link_list) - 1:
            self.current_link_index += 1

    def previous_link(self):
        # Move to the previous link in the list, if available
        if self.current_link_index > 0:
            self.current_link_index -= 1

    def show_previous_resource(self):
        if self.current_resource > 0:
            self.current_resource -= 1
            self.display_resource()
        else:
            pass
        self.copy_link_btn.setText('Click to copy link')

    def reset(self):
        ''' Reset the widget'''
        self.current_resource = 0
        self.copy_link_btn.setText('Click to copy link')
        self.display_resource()

    def show_back(self):
        ''' Show the back button'''
        self.reset()
        widget.setCurrentIndex(0)

    def show_main_menu(self):
        ''' Show the main menu'''
        self.reset()
        widget.setCurrentIndex(2)


class HomeApp(QDialog):
    '''Main Menu App'''
    def __init__(self):
        ''' Initialize the menu'''
        super(HomeApp, self).__init__()
        # pass super class LoginApp to parent class
        loadUi(r"static\home.ui", self)
        self.b9.clicked.connect(self.menu)
        self.b5_2.clicked.connect(self.show_back)
        self.b5.clicked.connect(self.show_personality)

    def show_personality(self):
        ''' Show the personality'''
        personalityform.current_question = 0
        widget.setCurrentIndex(5)

    def show_back(self):
        ''' Show the back button'''
        widget.setCurrentIndex(0)

    def menu(self):
        ''' Menu function'''
        widget.setCurrentIndex(2)


class GuestApp(QDialog):
    '''Guest User Interface'''
    def __init__(self):
        '''Initialize the widget'''
        super(GuestApp, self).__init__()
        # pass super class GuestApp to parent class
        loadUi(r"static\guest.ui", self)
        self.stress_btn.clicked.connect(self.show_stress)
        self.quotes_btn.clicked.connect(self.show_quotes)
        self.signupmore_btn.clicked.connect(self.show_sign_up)

    def show_quotes(self):
        ''' Show  the quotes'''
        widget.setCurrentIndex(9)

    def show_sign_up(self):
        ''' Show the sign up'''
        widget.setCurrentIndex(1)

    def show_stress(self):
        ''' Show the stress'''
        widget.setCurrentIndex(8)


class Verify:
    ''' Verifies that the user has authorized to perform a given action'''
    def __init__(self, password):
        ''' Initialize the verification'''
        self.password = password

    def compare(self, other_password):
        ''' Compare the password'''
        return self.password == other_password

    def show_quotes_app(self):
        ''' Show quotes'''
        self.quotes_app = QuotesApp()
        self.quotes_app.exec_()


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
# Connects both login and register widgets together
loginform = LoginApp()
registrationform = RegApp()
main_menu = MainMenuapp()
guestform = GuestApp()
homeform = HomeApp()
personalityform = PersonalityApp()
quotes = QuotesApp()
exercises = UserExercisesApp()
guest_exercises = GuestExerciseApp()
guest_quotes = GuestQuotesApp()
music = UserMusicApp()
resources = ResourcesApp()

widget.addWidget(loginform)  # 0
widget.addWidget(registrationform)  # 1
widget.addWidget(main_menu)   # 2
widget.addWidget(guestform)  # 3
widget.addWidget(homeform)  # 4
widget.addWidget(personalityform)  # 5
widget.addWidget(quotes)  # 6
widget.addWidget(exercises)  # 7
widget.addWidget(guest_exercises)   # 8
widget.addWidget(guest_quotes)  # 9
widget.addWidget(music)  # 10
widget.addWidget(resources)  # 11
widget.setWindowTitle("Soft Health v1.0")
widget.setWindowIcon(QIcon('static\images\icon.png'))

widget.setCurrentIndex(0)
widget.setFixedWidth(1024)
widget.setFixedHeight(768)

widget.show()
sys.exit(app.exec_())
