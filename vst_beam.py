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
        self.widgets()
        self.layouts()


    def widgets(self):
        self.confirmReinforcementBtn = QPushButton("Confirm")
        self.confirmReinforcementBtn.clicked.connect(self.make_widgets)
        self.Cross_Section_IMG = QLabel()
        self.Cross_Section_IMG.setPixmap(QPixmap("icons/icon.ico"))
        self.top_reinf_number = QComboBox(self)
        for number in range(2,11,1):
            self.top_reinf_number.addItem(str(number))

        self.stirrups = QLineEdit()
        self.stirrups.setPlaceholderText("Please specify the stirrups")
        self.bottom_reinf_number = QComboBox(self)
        for number in range(2,11,1):
            self.bottom_reinf_number.addItem(str(number))



    def layouts(self):
        self.topMainLayout = QHBoxLayout()
        self.topLeftLayout = QVBoxLayout()


        self.topRightLayout = QFormLayout()
        self.topveryRightLayout = QVBoxLayout()


        self.topLeftLayout.addWidget(self.Cross_Section_IMG)
        self.topLeftLayout.setAlignment(Qt.AlignCenter)
        self.topRightLayout.addRow("Number of top reinforcement rebars: ", self.top_reinf_number)
        self.topRightLayout.addRow("Stirrups: ", self.stirrups)
        self.topRightLayout.addRow("Number of bottom reinforcement rebars: ", self.bottom_reinf_number)
        self.topRightLayout.addRow("Confirm", self.confirmReinforcementBtn)
        self.topRightLayout.setAlignment(Qt.AlignCenter)


        try:
            self.topveryRightLayout.addLayout(self.topRebars)
            self.topveryRightLayout.addLayout(self.bottomRebars)

        except:
            pass

        self.topMainLayout.addLayout(self.topLeftLayout)
        self.topMainLayout.addLayout(self.topRightLayout)
        self.topMainLayout.addLayout(self.topveryRightLayout)
        self.topMainLayout.setAlignment(Qt.AlignTop)



        self.setLayout(self.topMainLayout)


    def make_widgets(self):

        try:
            for i in reversed(range(self.topRebars.count())):
                self.topRebars.itemAt(i).widget().setParent(None)

            for i in reversed(range(self.bottomRebars.count())):
                self.bottomRebars.itemAt(i).widget().setParent(None)

            self.topRebars = QHBoxLayout()
            self.bottomRebars = QHBoxLayout()


            list_of_top_widgets = list()
            list_of_bottom_widgets = list()
            number_of_top_widgets = int(self.top_reinf_number.currentText())
            number_of_bottom_widgets = int(self.bottom_reinf_number.currentText())


            for number in range(number_of_top_widgets):
                print(number_of_top_widgets)
                self.widget = QLineEdit()
                self.widget.setFixedSize(20, 20)
                self.widget.setPlaceholderText("Enter diameter")
                list_of_top_widgets.append(self.widget)

            for number in range(number_of_bottom_widgets):
                print(number_of_bottom_widgets)
                self.widget = QLineEdit()
                self.widget.setFixedSize(20, 20)
                self.widget.setPlaceholderText("Enter diameter")
                list_of_bottom_widgets.append(self.widget)


            for widget in list_of_top_widgets:
                self.topRebars.addWidget(widget)


            for widget in list_of_bottom_widgets:
                self.bottomRebars.addWidget(widget)

            self.topveryRightLayout.addLayout(self.topRebars)
            self.topveryRightLayout.addLayout(self.bottomRebars)
            list_of_top_widgets.clear()
            list_of_bottom_widgets.clear()



        except:
            self.topRebars = QHBoxLayout()
            self.bottomRebars = QHBoxLayout()

            list_of_top_widgets = list()
            list_of_bottom_widgets = list()
            number_of_top_widgets = int(self.top_reinf_number.currentText())
            number_of_bottom_widgets = int(self.bottom_reinf_number.currentText())

            for number in range(number_of_top_widgets):
                print(number_of_top_widgets)
                self.widget = QLineEdit()
                self.widget.setFixedSize(20, 20)
                self.widget.setPlaceholderText("Enter diameter")
                list_of_top_widgets.append(self.widget)

            for number in range(number_of_bottom_widgets):
                print(number_of_bottom_widgets)
                self.widget = QLineEdit()
                self.widget.setFixedSize(20,20)
                self.widget.setPlaceholderText("Enter diameter")
                list_of_bottom_widgets.append(self.widget)

            for widget in list_of_top_widgets:
                self.topRebars.addWidget(widget)


            for widget in list_of_bottom_widgets:
                self.bottomRebars.addWidget(widget)


            self.topveryRightLayout.addLayout(self.topRebars)
            self.topveryRightLayout.addLayout(self.bottomRebars)
            list_of_top_widgets.clear()
            list_of_bottom_widgets.clear()





