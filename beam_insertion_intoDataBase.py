import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import math
from PIL import Image
import sqlite3





class Insertion(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Beam Entry")
        self.setWindowIcon(QIcon("icons/ico.ico"))
        self.setGeometry(450,150,500,550)
        self.setStyleSheet("background-color:white")
        self.UI()
        self.show()


    def UI(self):
        pass