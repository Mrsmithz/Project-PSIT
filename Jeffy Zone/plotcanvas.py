import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
import random
import sqlite3
import time

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        fig.set_facecolor('lightgrey')
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

class MyDynamicMplCanvas(Canvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()
        self.plot_by_price()
        #timer = QtCore.QTimer(self)
        #timer.timeout.connect(self.liveplot)
        #timer.start(1000)
        self.liveplot()
    def plot_by_price(self):
        labels = []
        value = []
        data = self.cur.execute("select * from items")
        for i in data:
            labels.append(i[0])
            value.append(i[1])
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.pie(value, labels=labels, autopct="%1.1f%%", shadow=True)
        ax.set_title("Pie Chart By Price")
        self.draw()

    def plot_by_quantity(self):
        labels = []
        value = []
        data = self.cur.execute("select * from items")
        for i in data:
            labels.append(i[0])
            value.append(i[2])
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.pie(value, labels=labels, autopct="%1.1f%%", shadow=True)
        ax.set_title("Pie Chart By Quantity")
        self.draw()

    def plot_by_rate(self):
        labels = []
        value = []
        data = self.cur.execute("select * from items")
        for i in data:
            labels.append(i[0])
            value.append(i[4])
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.pie(value, labels=labels, autopct="%1.1f%%", shadow=True)
        ax.set_title("Pie Chart By Rate")
        self.draw()

    def liveplot(self):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.plot_by_price)
        timer.timeout.connect(self.liveplot2)
        timer.setSingleShot(True)
        timer.start(1000)
    def liveplot2(self):
        timer2 = QtCore.QTimer(self)
        timer2.timeout.connect(self.plot_by_quantity)
        timer2.timeout.connect(self.liveplot3)
        timer2.setSingleShot(True)
        timer2.start(1000)
    def liveplot3(self):
        timer3 = QtCore.QTimer(self)
        timer3.timeout.connect(self.plot_by_rate)
        timer3.timeout.connect(self.liveplot)
        timer3.setSingleShot(True)
        timer3.start(1000)
