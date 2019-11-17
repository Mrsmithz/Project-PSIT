import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
import random
import sqlite3

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
        self.plot()
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.plot)
        timer.start(1000)



    def plot(self):
        labels = []
        value = []
        data = self.cur.execute("select * from items")
        for i in data:
            labels.append(i[0])
            value.append(i[1])
        ax = self.figure.add_subplot(111)
        ax.cla()
        ax.pie(value, labels=labels, autopct="%1.1f%%", shadow=True)
        self.draw()
