#yiu need to have PyQt, PyQtWebEngine installed

from importlib import reload
from sys import *
from turtle import color, forward
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navber = QToolBar()
        self.addToolBar(navber)

        backbutton = QAction('BACK', self)
        backbutton.triggered.connect(self.browser.back)
        navber.addAction(backbutton)
        
        forward_button = QAction("Forward", self)
        forward_button.triggered.connect(self.browser.forward)
        navber.addAction(forward_button)

        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(self.browser.reload)
        navber.addAction(reload_button)

applicationX = QApplication(sys.argv)
QApplication.setApplicationName('IDK')
window = MainWindow()
applicationX.exec_()