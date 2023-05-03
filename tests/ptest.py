# 'import sys
# import os
# src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
# sys.path.append(src_path)
# import pytest
# from PyQt5.QtWidgets import QPushButton
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication
# from src.personality import Ui_PersonalityTest
# from src.personality_quiz import *

# @pytest.fixture
# def app():

#     app = QApplication(sys.argv)
#     ui = QtWidgets.QWidget()
#     form = Ui_PersonalityTest()
#     form.setupUi(ui)
#     ui.show()
#     yield form
#     app.quit()

#     # # initialize Qt application
#     # app = QApplication([])

#     # # create instance of PersonalityApp
#     # dialog = PersonalityApp()

#     # # add QtBot for widget interaction
#     # qtbot.addWidget(dialog)

#     # # return dialog
#     # yield dialog

#     # # cleanup
#     # #dialog.close()
#     # app.quit()


# class TestPersonality:
#     @pytest.fixture
#     def ui_elements(self, app):
#         next_btn = app.next_btn
#         back_btn = app.back_btn
#         Question_No = app.Question_No
#         Question_area = app.Question_area
#         radioButton1 = app.radioButton1
#         radioButton2 = app.radioButton2
#         return next_btn, back_btn, Question_No, Question_area, radioButton1, radioButton2
    

#     def test_display_question(self, app, ui_elements):
#         next_btn, back_btn, Question_No, Question_area, radioButton1, radioButton2 = ui_elements
#         self.questions = [
#             {
#                 'question': 'You feel more energetic when:',
#                 'options': ['Socializing with others', 'Spending time alone'],
#                 'traits': ['E', 'I']
#             },
#             {
#                 'question': 'You focus more on:',
#                 'options': ['Facts and details', 'Big picture and possibilities'],
#                 'traits': ['S', 'N']
#             },
#             {
#                 'question': 'You usually make decisions based on:',
#                 'options': ['Logical analysis', 'Personal values and emotions'],
#                 'traits': ['T', 'F']
#             },
#             {
#                 'question': 'You prefer:',
#                 'options': ['A structured and organized lifestyle', 'A spontaneous and flexible lifestyle'],
#                 'traits': ['J', 'P']
#             }
#         ]

#         self.current_question_index = 0

#         self.next_btn.clicked.connect(self.show_next_question)
#         self.back_btn.clicked.connect(self.show_previous_question)

#         self.show_question(0)

#     def show_question(self, index):
#         question_data = self.questions[index]
#         self.Question_No.setText(f"Question {index + 1}")
#         self.Question_area.setText(question_data['question'])
#         self.radioButton1.setText(question_data['options'][0])
#         self.radioButton2.setText(question_data['options'][1])

#         # Set the radio button states based on user selection (if any)
#         if question_data['traits'][0] in questions:
#             self.radioButton1.setChecked(True)
#         elif question_data['traits'][1] in questions:
#             self.radioButton2.setChecked(True)
#         else:
#             self.radioButton1.setChecked(False)
#             self.radioButton2.setChecked(False)
#         self.next_btn.clicked.connect(self.show_next_question)

#     def show_next_question(self):
#         if self.current_question_index < len(self.questions) - 1:
#             self.current_question_index += 1
#             self.show_question(self.current_question_index)

#     def show_previous_question(self):
#         if self.current_question_index > 0:
#             self.current_question_index -= 1
#             self.show_question(self.current_question_index)

#         # test that the display_question function displays the correct question
#         app.current_question = 0
#         self.show_question()
#         # app.display_question()
#         assert app.Question_No.text() == 'Question 1'
#         assert app.Question_area.text() == 'This is question 1'
#         assert app.radioButton1.text() == 'Option 1'
#         assert app.radioButton2.text() == 'Option 2'

#     def test_next_question(self, app):
#         # test that the next_question function advances to the next question
#         app.current_question = 0
#         app.show_next_question()
#         app.radioButton1.setChecked(True)
#         app.show_next_question()
#         assert app.current_question == 1
#         assert len(app.selected_answers) == 1

#     def test_previous_question(self, app):
#         # test that the previous_question function goes back to the previous question
#         app.current_question = 1
#         app.show_previous_question()
#         app.show_previous_question()
#         assert app.current_question == 0


#     def test_show_result(self, app):
#         # test that the show_result function displays the correct result
#         app.current_question = 4
#         app.show_question(0)
#         app.radioButton1.setChecked(True)
#         app.next_question()
#         app.radioButton1.setChecked(True)
#         app.next_question()
#         app.radioButton2.setChecked(True)
#         app.next_question()
#         app.radioButton2.setChecked(True)
#         app.next_question()
#         app.radioButton1.setChecked(True)
#         app.show_result()
#         assert app.result == 'EINSJ'
#         assert 'Personality Result' in [msg.windowTitle() for msg in app.topLevelWidgets()]
#         assert 'Recommendation for you:' in [msg.text() for msg in app.topLevelWidgets()]'