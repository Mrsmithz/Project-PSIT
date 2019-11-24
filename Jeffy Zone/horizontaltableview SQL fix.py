# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\FAITH\Desktop\Prototype1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QListWidget, QListWidgetItem, QLabel, QApplication, QDialog
import pickle
import sqlite3
import sys
from plotcanvas import MyDynamicMplCanvas
from PyQt5.QtWidgets import QMenu


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 800)

        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.clearbtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearbtn.clicked.connect(self.clear)
        self.clearbtn.setGeometry(QtCore.QRect(250, 620, 111, 51))
        self.clearbtn.setObjectName("clearbtn")

        self.submitbtn = QtWidgets.QPushButton(self.centralwidget)

        self.submitbtn.clicked.connect(self.submit)
        self.submitbtn.setGeometry(QtCore.QRect(10, 620, 111, 51))
        self.submitbtn.setObjectName("submitbtn")

        self.updatebtn = QtWidgets.QPushButton(self.centralwidget)
        self.updatebtn.clicked.connect(self.delete)
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
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        header = self.tableView.horizontalHeader()
        header.setDefaultSectionSize(190)
        self.tableView.doubleClicked.connect(self.savefromtable)
        self.tableView.cellPressed.connect(self.savefromtable)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 1001, 211))
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


        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")

        self.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuasd = QtWidgets.QMenu(self.menuBar)
        self.menuasd.setObjectName("menuasd")

        self.setMenuBar(self.menuBar)
        self.actionExport = QtWidgets.QAction(self)
        self.actionExport.setObjectName("actionExport")
        self.actionImport = QtWidgets.QAction(self)
        self.actionImport.setObjectName("actionImport")

        self.menuasd.addSeparator()
        self.menuasd.addAction(self.actionExport)
        self.menuasd.addAction(self.actionImport)
        self.menuBar.addAction(self.menuasd.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.plotpie = QtWidgets.QWidget(self.centralwidget)
        self.plotpie.setGeometry(QtCore.QRect(400, 270, 611, 471))
        self.testui = QtWidgets.QVBoxLayout(self.plotpie)
        self.pie = MyDynamicMplCanvas(self.plotpie)
        self.testui.addWidget(self.pie)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PSIT ON FIRE!!"))
        self.submitbtn.setText(_translate("MainWindow", "Submit"))
        self.updatebtn.setText(_translate("MainWindow", "Delete"))
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
    def submit(self, *args):
        if not self.name_input.toPlainText():
            return
        name = self.name_input.toPlainText()
        try:
            price = float(self.price_input.toPlainText())
        except:
            self.priceerror()
            return
        try:
            quantity = int(self.quantity_input.toPlainText())
        except:
            self.quantityerror()
            return
        try:
            monthly = float(self.month_input.toPlainText())
        except:
            self.monthlyerror()
            return
        date = self.dateEdit.date().toPyDate()
        notes = self.notes_input.toPlainText()
        self.cur.execute("insert into items values (?, ?, ?, ?, ?, ?)", (name, price, quantity, date, monthly, notes))
        self.conn.commit()
        list1 = self.cur.execute("select * from items")
        #list1 = self.cur.fetchall()
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
        list1 = self.cur.execute("select * from items")
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
    def savefromtable(self):
        row = self.tableView.rowCount()
        col = self.tableView.columnCount()
        header2 = ["price", "quantity", "movedindate", "monthlyrate", "notes"]
        list_name = self.cur.execute("select name from items order by rowid")
        list_name = self.cur.fetchall()
        for rows in range(row):
            for cols in range(col):
                item = self.tableView.item(rows, cols)
                name = list_name[rows]
                self.cur.execute('UPDATE items SET '+header2[cols]+' = ? WHERE name = ?', (item.text(), name[0]))
        self.conn.commit()
    def keyPressEvent(self, e):
        pass
    def delete(self):
        row = self.tableView.currentRow()
        self.tableView.removeRow(row)
    def priceerror(self):
        QMessageBox.about(self, "Input Error", "Please enter numbers in the Price box.")
    def quantityerror(self):
        QMessageBox.about(self, "Input Error", "Please enter numbers in the Quantity box.")
    def monthlyerror(self):
        QMessageBox.about(self, "Input Error", "Please enter numbers in the Monthly box.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #self = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    ui.update()
    sys.exit(app.exec_())
