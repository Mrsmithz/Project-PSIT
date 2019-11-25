from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
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
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QDateEdit
from PyQt5.QtWidgets import QTableWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QVBoxLayout
from plotcanvas import MyDynamicMplCanvas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(1024, 800)

        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()

        self.main = QWidget(self)

        self.clearbtn = QPushButton(self.main)
        self.clearbtn.setGeometry(250, 620, 111, 51)
        self.clearbtn.setText("Clear")
        self.clearbtn.clicked.connect(self.clear)

        self.submitbtn = QPushButton(self.main)
        self.submitbtn.setGeometry(10, 620, 111, 51)
        self.submitbtn.setText("Submit")
        self.submitbtn.clicked.connect(self.submit)

        self.deletebtn = QPushButton(self.main)
        self.deletebtn.setGeometry(130, 620, 111, 51)
        self.deletebtn.setText("Delete")
        self.deletebtn.clicked.connect(self.delete)

        self.name_input = QTextEdit(self.main)
        self.name_input.setGeometry(90, 230, 291, 41)
        self.name_input.setFontPointSize(14)

        self.price_input = QTextEdit(self.main)
        self.price_input.setGeometry(90, 280, 291, 41)
        self.price_input.setFontPointSize(14)

        self.quantity_input = QTextEdit(self.main)
        self.quantity_input.setGeometry(90, 330, 291, 41)
        self.quantity_input.setFontPointSize(14)

        self.date_input = QDateEdit(self.main)
        self.date_input.setGeometry(120, 380, 91, 21)
        currentdate = QtCore.QDateTime.currentDateTime()
        self.date_input.setDate(currentdate.date())
        self.date_input.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.date_input.setCalendarPopup(True)

        self.rate_input = QTextEdit(self.main)
        self.rate_input.setGeometry(130, 420, 171, 41)
        self.rate_input.setFontPointSize(14)

        self.note_input = QTextEdit(self.main)
        self.note_input.setGeometry(90, 470, 291, 131)
        self.note_input.setFontPointSize(14)

        self.mytable = QTableWidget(self.main)
        self.mytable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        header = self.mytable.horizontalHeader()
        header.setDefaultSectionSize(190)
        self.mytable.setGeometry(10, 10, 1001, 211)
        self.mytable.doubleClicked.connect(self.savefromtable)
        self.mytable.cellPressed.connect(self.savefromtable)

        self.name_label = QLabel(self.main)
        self.name_label.setGeometry(10, 240, 61, 16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_label.setFont(font)
        self.name_label.setText("Name")

        self.price_label = QLabel(self.main)
        self.price_label.setGeometry(10, 290, 51, 16)
        self.price_label.setFont(font)
        self.price_label.setText("Price")

        self.quantity_label = QLabel(self.main)
        self.quantity_label.setGeometry(10, 343, 81, 20)
        self.quantity_label.setFont(font)
        self.quantity_label.setText("Quantity")

        self.date_label = QLabel(self.main)
        self.date_label.setGeometry(10, 380, 101, 21)
        self.date_label.setFont(font)
        self.date_label.setText("Date")

        self.rate_label = QLabel(self.main)
        self.rate_label.setGeometry(10, 430, 111, 21)
        self.rate_label.setFont(font)
        self.rate_label.setText("Rate")

        self.note_label = QLabel(self.main)
        self.note_label.setGeometry(10, 520, 81, 21)
        self.note_label.setFont(font)
        self.note_label.setText("Note")

        self.status_bar = QStatusBar(self)
        self.setStatusBar(self.status_bar)

        self.menu_bar = QMenuBar(self)
        self.menu_bar.setGeometry(0, 0, 1024, 20)
        self.menu_top = QMenu(self.menu_bar)
        self.menu_top.setTitle("Menu")
        self.setMenuBar(self.menu_bar)

        self.menu_top.addSeparator()
        self.export = QAction(self)
        self.export.setText("Export")
        self.menu_top.addAction(self.export)
        self.menu_bar.addAction(self.menu_top.menuAction())

        self.setCentralWidget(self.main)

        self.plotpie = QWidget(self.main)
        self.plotpie.setGeometry(400, 270, 611, 471)
        self.pie_box = QVBoxLayout(self.plotpie)
        self.pie = MyDynamicMplCanvas(self.plotpie)
        self.pie_box.addWidget(self.pie)
    def submit(self, *args):
        """Submit input from input slots when called and update cell in the same time"""
        if not self.name_input.toPlainText():
            return
        name = self.name_input.toPlainText()
        price = float(self.price_input.toPlainText())
        quantity = int(self.quantity_input.toPlainText())
        date = self.date_input.date().toPyDate()
        monthly = float(self.rate_input.toPlainText())
        notes = self.note_input.toPlainText()
        self.cur.execute("insert into items values (?, ?, ?, ?, ?, ?)", (name, price, quantity, date, monthly, notes))
        self.conn.commit()
        list1 = self.cur.execute("select * from items")
        #list1 = self.cur.fetchall()
        header = []
        header2 = ["Price", "Quantity", "MovedInDate", "Monthly Rate", "Notes"]
        self.mytable.setColumnCount(5)
        self.mytable.setRowCount(0)
        row = 0
        for items in list1:
            header.append(items[0])
            cols = 0
            self.mytable.insertRow(row)
            for value in items[1:]:
                item = QTableWidgetItem(value)
                self.mytable.setItem(row, cols, item)
                cols += 1
            row += 1
        self.mytable.setHorizontalHeaderLabels(header2)
        self.mytable.setVerticalHeaderLabels(header)

    def update(self, *args):
        """Update Cell when called"""
        list1 = self.cur.execute("select * from items order by rowid")
        header = []
        header2 = ["Price", "Quantity", "MovedInDate", "Monthly Rate", "Notes"]
        row = 0
        self.mytable.setColumnCount(5)
        self.mytable.setRowCount(0)
        for items in list1:
            header.append(items[0])
            cols = 0
            self.mytable.insertRow(row)
            for value in items[1:]:
                item = QTableWidgetItem(value)
                self.mytable.setItem(row, cols, item)
                cols += 1
            row += 1
        self.mytable.setHorizontalHeaderLabels(header2)
        self.mytable.setVerticalHeaderLabels(header)
        self.headertest = header

    def clear(self, *args):
        """Clear all input slot"""
        self.name_input.clear()
        self.price_input.clear()
        self.quantity_input.clear()
        self.rate_input.clear()
        self.note_input.clear()

    def savefromtable(self):
        """Save input from Cell in MyTable Instantly"""
        row = self.mytable.rowCount()
        col = self.mytable.columnCount()
        header2 = ["price", "quantity", "movedindate", "monthlyrate", "notes"]
        list_name = self.cur.execute("select name from items order by rowid")
        list_name = self.cur.fetchall()
        for rows in range(row):
            for cols in range(col):
                item = self.mytable.item(rows, cols)
                name = list_name[rows]
                self.cur.execute('UPDATE items SET '+header2[cols]+' = ? WHERE name = ?', (item.text(), name[0]))
        self.conn.commit()

    def delete(self, *args):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.update()
    ui.show()
    sys.exit(app.exec_())
