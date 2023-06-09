import sys
import os
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.append(src_path)
import pytest
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from src.personality import Ui_PersonalityTest

questions = [
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
    ]

personality_list = {
    "ISTJ": "Introverted, Sensing, Thinking, Judging",
    "ISFJ": "Introverted, Sensing, Feeling, Judging",
    "INFJ": "Introverted, Intuitive, Feeling, Judging",
    "INTJ": "Introverted, Intuitive, Thinking, Judging",
    "ISTP": "Introverted, Sensing, Thinking, Perceiving",
    "ISFP": "Introverted, Sensing, Feeling, Perceiving",
    "INFP": "Introverted, Intuitive, Feeling, Perceiving",
    "INTP": "Introverted, Intuitive, Thinking, Perceiving",
    "ESTP": "Extroverted, Sensing, Thinking, Perceiving",
    "ESFP": "Extroverted, Sensing, Feeling, Perceiving",
    "ENFP": "Extroverted, Intuitive, Feeling, Perceiving",
    "ENTP": "Extroverted, Intuitive, Thinking, Perceiving",
    "ESTJ": "Extroverted, Sensing, Thinking, Judging",
    "ESFJ": "Extroverted, Sensing, Feeling, Judging",
    "ENFJ": "Extroverted, Intuitive, Feeling, Judging",
    "ENTJ": "Extroverted, Intuitive, Thinking, Judging"
}

personality_recommendation = {
 "ISTJ": "Practice adaptability,\
    embrace change, and explore creative problem-solving. \
    Make time for leisure and social activities\
    to balance work and personal life.\
    (source: Costa Jr, P. T., & McCrae, R. R. (1992).\
    Revised NEO Personality Inventory (NEO-PI-R) and\
    NEO Five-Factor Inventory (NEO-FFI) manual.\
    Psychological Assessment Resources.)",
    
    "ISFJ": "Develop assertiveness, set boundaries, and\
    engage in self-care practices.\
    Explore new experiences and ideas to expand perspectives.\
    (source: Judge, T. A., & Bono, J. E. (2001).\
    Relationship of core self-evaluations traits--self-esteem,\
    generalized self-efficacy, locus of control, and emotional stability\
    --with job satisfaction and job performance: A meta-analysis.\
    Journal of Applied Psychology, 86(1), 80-92.)",
    
    "ISFJ": "Develop assertiveness, set boundaries, and engage \
        in self-care practices. Explore new experiences and ideas \
        to expand perspectives. (source: Judge, T. A., & Bono, J. E. (2001).\
        Relationship of core self-evaluations traits--self-esteem,\
        generalized self-efficacy, locus of control, and emotional\
        stability--with job satisfaction and job performance:\
        A meta-analysis. Journal of Applied Psychology, 86(1), 80-92.)",
    "INFJ": "Prioritize self-care and set boundaries to avoid burnout.\
        Practice open-mindedness and engage in activities that promote\
        self-awareness and self-growth. (source: Ashton, M. C., & Lee, K. (2009).\
        The HEXACO-60: A short measure of the major dimensions of personality.\
        Journal of Personality Assessment, 91(4), 340-345.)",
    "INTJ": "Develop emotional intelligence, practice empathy, and \
        engage in team-building activities to strengthen social connections.\
        Balance intellectual pursuits with physical exercise and relaxation.\
        (source: Goleman, D. (1995). Emotional intelligence. Bantam Books.)",
    "ISTP": "Cultivate long-term goals, practice time management,\
        and develop organizational skills. Engage in social activities\
        and build a support network. (source: Macan, T. H.,\
        Shahani, C., Dipboye, R. L., & Phillips, A. P. (1990).\
        College students' time management: Correlations with \
        academic performance and stress. Journal of Educational \
            Psychology, 82(4), 760-768.)",
    "ISFP": "Develop assertiveness, practice communication skills,\
        and set personal goals. Engage in creative pursuits and\
        explore new experiences.\
        (source: Riggio, R. E., & Reichard, R. J. (2008).\
        The emotional and social intelligences of effective\
        leadership: An emotional and social skill approach.\
        Journal of Managerial Psychology, 23(2), 169-185.)",
    "INFP": "Set realistic goals, develop practical skills, and \
        practice self-compassion. Engage in mindfulness and stress\
        management techniques. (source: Neff, K. D. (2011).\
        Self-compassion, self-esteem, and well-being.\
        Social and Personality Psychology Compass, 5(1), 1-12.)",
    "INTP": "Develop emotional intelligence, practice active listening,\
        and engage in social activities. Balance intellectual\
        interests with physical exercise and self-care.\
        (source: Goleman, D. (1995). Emotional intelligence. Bantam Books.)",
    "ESTP": "Develop long-term goals, practice patience,\
        and engage in mindfulness techniques. Cultivate deeper\
        connections through meaningful conversations.\
        (source: Kabat-Zinn, J. (2003). \
        Mindfulness-based interventions in context:\
        past, present, and future. Clinical Psychology: \
        Science and Practice, 10(2), 144-156.)",
    "ESFP": "Develop time management and organizational skills,\
        and set personal goals. Engage in activities that promote\
        self-reflection and personal growth.\
        (source: Macan, T. H., Shahani,\
            C.,Dipboye, R. L., & Phillips, A. P. (1990).\
        College students' time management: Correlations with\
        academic performance and stress. Journal of Educational Psychology, 82(4), 760-768.)",
    "ENFP": "Practice setting boundaries, develop self-discipline,\
        and work on follow-through. Engage in relaxation techniques\
        and mindfulness to manage stress. \
        (source: Kabat-Zinn, J. (2003).\
        Mindfulness-based interventions in context: past,\
        present, and future.\
        Clinical Psychology: Science and Practice, 10(2), 144-156.)",
    "ENTP": "Develop active listening skills, practice empathy, \
        and cultivate emotional intelligence.\
        Balance exploration of new ideas with self-care\
        and relaxation. (source: Goleman, D. (1995).\
        Emotional intelligence. Bantam Books.)",
    "ESTJ": "Develop flexibility, practice empathy,\
        and engage in open-minded discussions. Balance work\
        and personal life by making time for leisure activities\
        and self-care. (source: Goleman, D. (1995).\
        Emotional intelligence. Bantam Books.)",
    "ESFJ": "Practice self-compassion, develop assertiveness,\
        and set boundaries. Engage in activities that\
        promote self-awareness and personal growth. \
        (source: Neff, K. D. (2011). Self-compassion,\
        self-esteem, and well-being. Social and Personality Psychology\
        Compass, 5(1), 1-12.)",
    "ENFJ": "Prioritize self-care, set personal boundaries,\
        and avoid overcommitting. Engage in stress management\
        techniques and relaxation activities. \
        (source: Kabat-Zinn, J. (2003).\
        Mindfulness-based interventions in \
        context: past, present, and future.\
        Clinical Psychology: Science and Practice, 10(2), 144-156.)",
    "ENTJ": "Develop emotional intelligence, practice active listening,\
        and engage in team-building activities. Balance work and\
        personal life with leisure activities and self-care. \
        (source: Goleman, D. (1995). Emotional intelligence. Bantam Books.)"
}


@pytest.fixture
def personality_ui():
    app = QApplication(sys.argv)
    ui = QtWidgets.QWidget()
    form = Ui_PersonalityTest()
    form.setupUi(ui)
    ui.show()
    yield form
    app.quit()

class TestPersonalityUI:
    def test_logoutButton(self, personality_ui):
        assert personality_ui.logout.text() == "Logout"
        QTest.mouseClick(personality_ui.logout, Qt.LeftButton)

    def test_nextButton(self, personality_ui):
        assert personality_ui.next_btn.text() == "Next"
        QTest.mouseClick(personality_ui.next_btn, Qt.LeftButton)

    def test_backButton(self, personality_ui):
        assert personality_ui.back_btn.text() == "Back"
        QTest.mouseClick(personality_ui.back_btn, Qt.LeftButton)

    def test_mainButton(self, personality_ui):
        assert personality_ui.main_btn.text() == "Main Menu"
        QTest.mouseClick(personality_ui.main_btn, Qt.LeftButton)

    def test_questionNo(self, personality_ui):
        assert personality_ui.Question_No.text() == "Question 1"
        QTest.mouseClick(personality_ui.Question_No, Qt.LeftButton)

    def test_questionArea(self, personality_ui):
        assert personality_ui.Question_area.text() == "You feel more energetic when:"
        QTest.mouseClick(personality_ui.Question_area, Qt.LeftButton)
        
    def test_radioButtons(self, personality_ui):
        assert personality_ui.radioButton1.text() == "Socializing with others"
        assert personality_ui.radioButton2.text() == "Spending time alone"
        QTest.mouseClick(personality_ui.radioButton1, Qt.LeftButton)
        QTest.mouseClick(personality_ui.radioButton2, Qt.LeftButton)

    def test_display_question(self, personality_ui):
        for i, question in enumerate(questions):
            personality_ui.Question_No.setText(f'Question {i+1}')
            personality_ui.Question_area.setText(question['question'])
            assert personality_ui.Question_No.text() == f"Question {i+1}"
            assert personality_ui.Question_area.text() == question['question']