import sys
from PyQt5.uic  import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget


class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)


app = QApplication(sys.argv)
win = WelcomeScreen()
widget = QStackedWidget()
widget.addWidget(win)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)


widget.show()

try:
    sys.exit(app.exec_())
except Exception:
    print("Error")
