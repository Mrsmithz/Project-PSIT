import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
from newcode import MainWindow
import os
class Login(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(500, 600)
        self.main = QWidget(self)
        self.setWindowTitle("Login")
        font = QFont()
        font.setPointSize(16)

        path = str(os.path.dirname(os.path.abspath(__file__))).replace("\\", "/")
        self.display_img = QWidget(self.main)
        self.display_img.setGeometry(10, 40, 481, 181)
        self.display_img.setStyleSheet(f"background-image: url({path}/img/login.jpg);")

        self.submitbtn = QPushButton(self.main)
        self.submitbtn.setGeometry(140, 390, 231, 51)
        self.submitbtn.setFont(font)
        self.submitbtn.setText("Login")
        self.submitbtn.clicked.connect(self.check)

        self.user_input = QLineEdit(self.main)
        self.user_input.setGeometry(140, 280, 231, 41)
        self.user_input.setFont(font)

        self.pass_input = QLineEdit(self.main)
        self.pass_input.setGeometry(140, 330, 231, 41)
        self.pass_input.setEchoMode(QLineEdit.Password)

        self.user_label = QLabel(self.main)
        self.user_label.setGeometry(20, 280, 111, 31)
        self.user_label.setFont(font)
        self.user_label.setText("Username :")

        self.pass_label = QLabel(self.main)
        self.pass_label.setGeometry(20, 330, 111, 31)
        self.pass_label.setFont(font)
        self.pass_label.setText("Password  :")

        self.setCentralWidget(self.main)

        self.conn = sqlite3.connect('user.db')
        self.cur = self.conn.cursor()
    def check(self):
        user = self.user_input.text()
        pwd = self.pass_input.text()
        self.cur.execute("select password from user where username=(?)", (user, ))
        test = self.cur.fetchall()
        if test:
            if pwd == test[0][0]:
                self.openwindow()
        else:
            msgbox = QMessageBox(self)
            #msgbox.about(self, "Incorrect", "\n\nIncorrect Username or Password\n\n")
            msgbox.setWindowTitle("INCORRECT!!")
            msgbox.setText("\n\nIncorrect Username or Password\n\n")
            msgbox.setIcon(QMessageBox.Critical)
            msgbox.setStandardButtons(QMessageBox.Retry)
            msgbox.exec_()
            return
    def openwindow(self):
        #self.windows = QMainWindow()
        self.another = MainWindow()
        self.another.update()
        login.hide()
        self.another.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())
