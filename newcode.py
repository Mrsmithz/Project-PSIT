# import all funtions that we need!!!
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
from PyQt5.QtCore import QLocale
from plotcanvas import MyDynamicMplCanvas
from plotcanvas import barplot
# make a class!
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1024, 800) # set the size of mainwindow

        self.conn = sqlite3.connect('test.db') # connecting to the database ("test.db")
        self.cur = self.conn.cursor()

        self.main = QWidget(self)
        font = QtGui.QFont()
        font.setPointSize(12) # set the point size

        self.clearbtn = QPushButton(self.main) # set variable clear button
        self.clearbtn.setGeometry(250, 620, 111, 51) # set where the button is
        self.clearbtn.setText("Clear") # set the name of button --> "Clear"
        self.clearbtn.clicked.connect(self.clear) # if the button was clicked, it will connecting to "clear" function

        self.submitbtn = QPushButton(self.main) # set variable --> submit button
        self.submitbtn.setGeometry(10, 620, 111, 51) # set where the button is
        self.submitbtn.setText("Submit") # set the name of the button --> "Submit"
        self.submitbtn.clicked.connect(self.submit) # if the button was clicked, it will connecting to "submit" function

        self.deletebtn = QPushButton(self.main) # set variable --> delete button
        self.deletebtn.setGeometry(130, 620, 111, 51) #set where the button is
        self.deletebtn.setText("Delete") # set the name of the button --> "Delete"
        self.deletebtn.clicked.connect(self.delete) # if the button was clicked, it will connecting to "delete" function

        self.name_input = QLineEdit(self.main) # set variable --> input() of name
        self.name_input.setGeometry(90, 230, 291, 41) # set where the name input is
        self.name_input.setFont(font) # set the size of the letter that you will going to input

        self.price_input = QLineEdit(self.main) # set variable --> input() of price
        self.price_input.setGeometry(90, 280, 291, 41) # set where the  price input is
        self.price_input.setFont(font) # set the size of the letter that you will going to input

        self.quantity_input = QLineEdit(self.main) # set variable --> input() of quantity
        self.quantity_input.setGeometry(90, 330, 291, 41) # set where the quantity input is
        self.quantity_input.setFont(font) # set the size of the letter that you will going to input

        self.date_input = QDateEdit(self.main) # set variable --> input() of date
        self.date_input.setGeometry(120, 380, 91, 21) # set where the date input is
        currentdate = QtCore.QDateTime.currentDateTime()
        self.date_input.setDate(currentdate.date()) # set variable --> input() of date
        self.date_input.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom)) # The local time is in United States
        self.date_input.setCalendarPopup(True) # set the pop-up of the carlender

        self.rate_input = QLineEdit(self.main) # set variable --> input() of rate
        self.rate_input.setGeometry(130, 420, 171, 41) # set where the input() is
        self.rate_input.setFont(font) # set the size of the letter that you will going to input

        self.note_input = QLineEdit(self.main) # set variable --> input() of note
        self.note_input.setGeometry(90, 470, 291, 131) # set where the input() is
        self.note_input.setFont(font) # set the size of the letter that you will going to input

        self.mytable = QTableWidget(self.main) # set the table
        self.mytable.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked) # set edittriggers for mytable
        header = self.mytable.horizontalHeader() # the header is the horizontal header
        header.setDefaultSectionSize(190) # set the size of ???
        self.mytable.setGeometry(10, 10, 1001, 211) # set where the table is?
        self.mytable.doubleClicked.connect(self.savefromtable) # connecting to double-cliked function
        self.mytable.cellPressed.connect(self.savefromtable) # connecting to cell-pressed

        self.name_label = QLabel(self.main) # set the variable --> label of "name"
        self.name_label.setGeometry(10, 240, 61, 16) # set where the "name" label is
        self.name_label.setFont(font) # set a font
        self.name_label.setText("Name") # called this label as "Name"

        self.price_label = QLabel(self.main) # set the variable --> label of "price"
        self.price_label.setGeometry(10, 290, 51, 16) # set where the "price" label is
        self.price_label.setFont(font) # set a font
        self.price_label.setText("Price") # called this label as "Price"

        self.quantity_label = QLabel(self.main) # set the variable --> label of "price"
        self.quantity_label.setGeometry(10, 343, 81, 20)  # set where the "price" label is
        self.quantity_label.setFont(font) # set a font
        self.quantity_label.setText("Quantity") # called this label as "Quantity"

        self.date_label = QLabel(self.main) # set the variable --> label of "price"
        self.date_label.setGeometry(10, 380, 101, 21)  # set where the "price" label is
        self.date_label.setFont(font) # set a font
        self.date_label.setText("Date") # called this label as "Date"

        self.rate_label = QLabel(self.main) # set the variable --> label of "price"
        self.rate_label.setGeometry(10, 430, 111, 21)  # set where the "price" label is
        self.rate_label.setFont(font) # set a font
        self.rate_label.setText("Rate") # called this label as "Rate"

        self.note_label = QLabel(self.main) # set the variable --> label of "price"
        self.note_label.setGeometry(10, 520, 81, 21)  # set where the "price" label is
        self.note_label.setFont(font) # set a font
        self.note_label.setText("Note") # called this label as "Note"

        self.status_bar = QStatusBar(self) # use the status bar that you import from the beginning
        self.setStatusBar(self.status_bar)

        self.menu_bar = QMenuBar(self) # set variables in menu bar
        self.menu_bar.setGeometry(0, 0, 1024, 20) # set where the variable is
        self.menu_top = QMenu(self.menu_bar)
        self.menu_top.setTitle("Export")
        self.setMenuBar(self.menu_bar)

        self.menu_top.addSeparator()

        self.export1 = QAction(self)
        self.export1.setText("1")
        self.export1.triggered.connect(self.plot_price)

        self.export2 = QAction(self)
        self.export2.setText("2")
        self.export2.triggered.connect(self.plot_quantity)

        self.export3 = QAction(self)
        self.export3.setText("3")
        self.export3.triggered.connect(self.plot_rate)

        self.menu_top.addAction(self.export1)
        self.menu_top.addAction(self.export2)
        self.menu_top.addAction(self.export3)
        self.menu_bar.addAction(self.menu_top.menuAction())

        self.setCentralWidget(self.main)

        self.plotpie = QWidget(self.main)
        self.plotpie.setGeometry(400, 220, 611, 471)
        self.pie_box = QVBoxLayout(self.plotpie)
        self.pie = MyDynamicMplCanvas(self.plotpie)
        self.pie_box.addWidget(self.pie)

    def submit(self, *args):
        """Submit input from input slots when called and update cell in the same time"""
        if not self.name_input.text():
            return
        name = self.name_input.text()
        price = float(self.price_input.text())
        quantity = int(self.quantity_input.text())
        date = str(self.date_input.date().toPyDate())
        date = "-".join((date[8:10], date[5:7], date[0:4]))
        monthly = float(self.rate_input.text())
        notes = self.note_input.text()
        self.cur.execute("insert into items values (?, ?, ?, ?, ?, ?)", (name, price, quantity, date, monthly, notes))
        self.conn.commit()
        list1 = self.cur.execute("select * from items")
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
        self.clear()
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
        row = self.mytable.currentRow()
        item = self.mytable.verticalHeaderItem(row).text()
        self.cur.execute('delete from items where name=(?)', (item, ))
        self.conn.commit()
        self.mytable.removeRow(row)

    def plot_price(self):
        pass

    def plot_quantity(self):
        pass

    def plot_rate(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.update()
    ui.show()
    sys.exit(app.exec_())
