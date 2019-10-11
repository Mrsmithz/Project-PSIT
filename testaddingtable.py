# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\FAITH\Desktop\Prototype1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
import pickle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.submitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitbtn.clicked.connect(self.test)
        self.submitbtn.setGeometry(QtCore.QRect(10, 620, 111, 51))
        self.submitbtn.setObjectName("submitbtn")

        self.name_input = QtWidgets.QTextEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(90, 230, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")

        self.price_input = QtWidgets.QTextEdit(self.centralwidget)
        self.price_input.setGeometry(QtCore.QRect(90, 280, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.price_input.setFont(font)
        self.price_input.setObjectName("price_input")

        self.quantity_input = QtWidgets.QTextEdit(self.centralwidget)
        self.quantity_input.setGeometry(QtCore.QRect(90, 330, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.quantity_input.setFont(font)
        self.quantity_input.setObjectName("textEdit_2")

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(120, 380, 91, 21))
        current = QtCore.QDateTime.currentDateTime()
        self.dateEdit.setDate(current.date())
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit.setObjectName("dateEdit")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setRowCount(5)
        self.tableView.setColumnCount(5)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 671, 211))
        self.tableView.setObjectName("tableView")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 380, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 240, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 343, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 430, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.month_input = QtWidgets.QTextEdit(self.centralwidget)
        self.month_input.setGeometry(QtCore.QRect(130, 420, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.month_input.setFont(font)
        self.month_input.setObjectName("month_input")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 520, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.notes_input = QtWidgets.QTextEdit(self.centralwidget)
        self.notes_input.setGeometry(QtCore.QRect(90, 470, 291, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.notes_input.setFont(font)
        self.notes_input.setObjectName("textEdit_4")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(700, 10, 301, 541))
        self.listView.setObjectName("listView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuasd = QtWidgets.QMenu(self.menuBar)
        self.menuasd.setObjectName("menuasd")

        MainWindow.setMenuBar(self.menuBar)
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")

        self.menuasd.addSeparator()
        self.menuasd.addAction(self.actionExport)
        self.menuasd.addAction(self.actionImport)
        self.menuBar.addAction(self.menuasd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submitbtn.setText(_translate("MainWindow", "Submit"))
        self.label_3.setText(_translate("MainWindow", "MovedInDate : "))
        self.label.setText(_translate("MainWindow", "Name : "))
        self.label_2.setText(_translate("MainWindow", "Price  :"))
        self.label_4.setText(_translate("MainWindow", "Quantity : "))
        self.label_5.setText(_translate("MainWindow", "Monthly Rate  : "))
        self.label_6.setText(_translate("MainWindow", "Notes  : "))
        self.menuasd.setTitle(_translate("MainWindow", "Files"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
    def test(self, *args):
        if not self.name_input.toPlainText():
            return
        name = self.name_input.toPlainText()
        price = self.price_input.toPlainText()
        quantity = self.quantity_input.toPlainText()
        dict1 = {}
        dict1[name] = price, quantity
        with open("dict1.pkl", "ab") as f:
            pickle.dump(dict1, f, pickle.HIGHEST_PROTOCOL)
        with open("dict1.pkl", "rb") as p:
            row = 0
            cols = 0
            while 1:
                try:
                    dict2 = pickle.load(p)
                    print(dict2)
                    for key in dict2.keys():
                        item = QTableWidgetItem(key)
                        self.tableView.setItem(row, cols, item)
                        cols += 1
                except:
                    break
        """header = []
        for n, key in enumerate(sorted(dict2.keys())):
            header.append(key)
            for m, item in enumerate(dict2[key]):
                newitem = QTableWidgetItem(item)
                self.tableView.setItem(m, n, newitem)
        self.tableView.setHorizontalHeaderLabels(header)"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
