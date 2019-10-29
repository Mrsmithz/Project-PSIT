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
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.clicked.connect(self.clear)
        self.clearbtn.setGeometry(QtCore.QRect(250, 620, 111, 51))
        self.clearbtn.setObjectName("clearbtn")

        self.submitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitbtn.clicked.connect(self.test)
        self.submitbtn.setGeometry(QtCore.QRect(10, 620, 111, 51))
        self.submitbtn.setObjectName("submitbtn")

        self.updatebtn = QtWidgets.QPushButton(self.centralwidget)
        self.updatebtn.clicked.connect(self.update)
        self.updatebtn.setGeometry(QtCore.QRect(130, 620, 111, 51))
        self.updatebtn.setObjectName("updatebtn")

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
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")

        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        #self.tableView.setColumnCount(5)
        #self.tableView.setRowCount(0)
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

        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submitbtn.setText(_translate("MainWindow", "Submit"))
        self.updatebtn.setText(_translate("MainWindow", "Update"))
        self.clearbtn.setText(_translate("MainWindow", "Clear"))
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
        price = float(self.price_input.toPlainText())
        quantity = int(self.quantity_input.toPlainText())
        date = self.dateEdit.date().toPyDate()
        monthly = float(self.month_input.toPlainText())
        notes = self.notes_input.toPlainText()
        self.cur.execute("insert into items values (?, ?, ?, ?, ?, ?)", (name, price, quantity, date, monthly, notes))
        self.conn.commit()
        self.cur.execute("select * from items")
        list1 = self.c.fetchall()
        header = []
        header2 = ["Price", "Quantity", "MovedInDate", "Monthly Rate", "Notes"]
        self.tableView.setColumnCount(5)
        self.tableView.setRowCount(0)
        row = 0
        for items in list1:
            header.append(items[0])
            cols = 0
            self.tableView.insertRow(row)
            for value in items[1:]:
                item = QTableWidgetItem(value)
                self.tableView.setItem(row, cols, item)
                cols += 1
            row += 1
        self.tableView.setHorizontalHeaderLabels(header2)
        self.tableView.setVerticalHeaderLabels(header)
    def update(self, *args):
        self.cur.execute("select * from items")
        list1 = self.cur.fetchall()
        header = []
        header2 = ["Price", "Quantity", "MovedInDate", "Monthly Rate", "Notes"]
        row = 0
        self.tableView.setColumnCount(5)
        self.tableView.setRowCount(0)
        for items in list1:
            header.append(items[0])
            cols = 0
            self.tableView.insertRow(row)
            for value in items[1:]:
                item = QTableWidgetItem(value)
                self.tableView.setItem(row, cols, item)
                cols += 1
            row += 1
        self.tableView.setHorizontalHeaderLabels(header2)
        self.tableView.setVerticalHeaderLabels(header)
    def clear(self, *args):
        self.name_input.clear()
        self.price_input.clear()
        self.quantity_input.clear()
        self.month_input.clear()
        self.notes_input.clear()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
