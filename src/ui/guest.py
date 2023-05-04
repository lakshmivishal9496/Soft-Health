from PyQt5.QtWidgets import QMessageBox, QDialog


class GuestApp(QDialog):
    def guest_login(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Welcome " + 'guest user' + '\n'
                       "Do you want to take personality assessment")
        msgBox.setWindowTitle("Guest User login")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        # show the message box and wait for a button to be clicked
        buttonClicked = msgBox.exec()
        if buttonClicked == QMessageBox.Ok:
            print("OK button clicked")
