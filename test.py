from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        self.setWindowTitle('Sample')
        self.setGeometry(200, 200, 200, 200)

    def initUI(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("helloMsg")
        self.label1.move(100, 35)
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click")
        self.b1.clicked.connect(self.button_clicked1)
        self.b1.move(400, 35)
        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("Trigger")
        self.b2.clicked.connect(self.show_popup)

    def button_clicked1(self):
        self.label1.setText('Button clicked')
        self.update()

    def update(self):
        self.label1.adjustSize()

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Alert')
        msg.setText('This is the alert')
        msg.setIcon(QMessageBox.Question)

        msg.exec_()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
