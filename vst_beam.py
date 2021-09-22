import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import sqlite3



class AddBeam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beam Definition")
        self.setWindowIcon(QIcon("icons/ico.ico"))
        self.setGeometry(450,150,500,550)
        self.setFixedSize(self.size())
        self.setStyleSheet("background-color:white")
        self.UI()
        self.show()


    def UI(self):
        pass



