from PyQt6 import QtWidgets, QtCore
from qt_material import apply_stylesheet
from PyQt6.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import numpy as np
import serial
import pandas as pd

from ui2 import Ui_MainWindow

serialPort = "/dev/ttyUSB0"
baudRate = 9600
ser = serial.Serial(serialPort, baudRate, timeout=1)
ser.readline()


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.init_plot()

    def init_connection(self):
        ser.write(b"b")

    def display_page1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def display_page2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def initUI(self):
        self.graphWidget = pg.PlotWidget()
        #self.setCentralWidget(self.graphWidget)
        self.ui.verticalLayout_band.addWidget(self.graphWidget)
        self.ui.pushButton_quit.clicked.connect(QApplication.instance().quit)
        self.ui.pushButton_begin.clicked.connect(self.init_connection)
        self.ui.pushButton_clear.clicked.connect(self.clear_data)
        self.ui.pushButton_main.clicked.connect(self.display_page1)
        self.ui.pushButton_about.clicked.connect(self.display_page2)
        self.ui.pushButton_save.clicked.connect(self.save_date)

        self.x = list()  # 100 time points
        self.y = list()  # 100 data points

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('virtual oscilloscope')
        self.show()

    def get_data(self):
        T = ser.readline()
        flag = ser.readline()
        V = ser.readline()

        T = str(T, 'utf-8')
        flag = str(flag, 'utf-8')
        V = str(V, 'utf-8')

        T = float(T)
        T = int(T)
        flag = flag[:-1]
        flag =flag[:-1]
        flag = int(flag)
        V = float(V)
        #V = int(V)

        if flag == 1:
            V = V * (-1)

        self.x.append(T)
        self.y.append(V)

    def init_plot(self):

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        self.graphWidget.showGrid(x=True, y=True)

        self.graphWidget.setTitle("virtual oscilloscope", color="b", size="30pt")

        styles = {'color':'r', 'font-size':'20px'}
        self.graphWidget.setLabel('left', 'Voltage (V)', **styles)
        self.graphWidget.setLabel('bottom', 'Times', **styles)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(0)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.get_data()
        self.data_line.setData(self.x, self.y)  # Update the data.

    def clear_data(self):
        self.x = list()
        self.y = list()

    def save_date(self):
        dict = {'times': self.x, 'voltage': self.y}

        df = pd.DataFrame(dict)

        df.to_csv('Voltage_Data.csv')



def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    apply_stylesheet(app, theme='light_lightgreen.xml')
    w.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
