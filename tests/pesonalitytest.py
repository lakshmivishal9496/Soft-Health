# import sys
# import os
# src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
# sys.path.append(src_path)
# import pytest
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication
# from src.personality import Ui_PersonalityTest



# @pytest.fixture
# def app():
#     app = QApplication(sys.argv)
#     ui = QtWidgets.QWidget()
#     form = Ui_PersonalityTest()
#     form.setupUi(ui)
#     ui.show()
#     yield form
#     app.quit()


# def test_display_question(app):
#     questions = [
#         {
#             'question': 'You feel more energetic when:',
#             'options': ['Socializing with others', 'Spending time alone'],
#             'traits': ['E', 'I']
#         },
#         {
#             'question': 'You focus more on:',
#             'options': ['Facts and details', 'Big picture and possibilities'],
#             'traits': ['S', 'N']
#         },
#         {
#             'question': 'You usually make decisions based on:',
#             'options': ['Logical analysis', 'Personal values and emotions'],
#             'traits': ['T', 'F']
#         },
#         {
#             'question': 'You prefer:',
#             'options': ['A structured and organized lifestyle', 'A spontaneous and flexible lifestyle'],
#             'traits': ['J', 'P']
#         }
#     ]

#     app.show_question(0)
#     assert app.Question_No.text() == 'Question 1'
#     assert app.Question_area.text() == 'You feel more energetic when:'
#     assert app.radioButton1.text() == 'Socializing with others'
#     assert app.radioButton2.text() == 'Spending time alone'


# def test_show_next_question(app):
#     app.show_question(0)
#     app.next_btn.click()
#     assert app.Question_No.text() == 'Question 2'


# def test_show_previous_question(app):
#     app.show_question(1)
#     app.back_btn.click()
#     assert app.Question_No.text() == 'Question 1'


# def test_show_result(app):
#     app.show_question(3)
#     app.radioButton1.setChecked(True)
#     app.next_btn.click()
#     app.radioButton1.setChecked(True)
#     app.next_btn.click()
#     app.radioButton2.setChecked(True)
#     app.next_btn.click()
#     app.radioButton2.setChecked(True)
#     app.next_btn.click()
#     app.radioButton1.setChecked(True)
#     app.show_result()
#     assert app.result == 'EINSJ'
#     assert 'Personality Result' in [msg.windowTitle() for msg in app.topLevelWidgets()]
#     assert 'Recommendation for you:' in [msg.text() for msg in app.topLevelWidgets()]
