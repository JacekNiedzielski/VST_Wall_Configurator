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
        self.setStyleSheet("background-color:white")
        self.UI()
        self.show()


    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        self.confirmReinforcementBtn = QPushButton("Confirm")
        self.confirmReinforcementBtn.clicked.connect(self.make_widgets)
        self.confirmDiametersBtn = QPushButton("Confirm Diameters")
        self.confirmDiametersBtn.clicked.connect(self.calculate_longitudinal_rebars)
        self.Cross_Section_IMG = QLabel()
        beam_image = QPixmap("img/img3.jpg")
        beam_image = beam_image.scaledToWidth(256)
        beam_image = beam_image.scaledToHeight(256)
        self.Cross_Section_IMG.setPixmap(beam_image)
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
        self.topRightLayout.addRow("Please choose the number of top reinforcement rebars: ", self.top_reinf_number)
        self.topRightLayout.addRow("Stirrups: ", self.stirrups)
        self.topRightLayout.addRow("Please choose the number of bottom reinforcement rebars: ", self.bottom_reinf_number)
        self.topRightLayout.addRow("Confirm", self.confirmReinforcementBtn)
        self.topRightLayout.addRow("Confirm Rebars", self.confirmDiametersBtn)
        self.topRightLayout.setAlignment(Qt.AlignCenter)

        try:
            self.topveryRightLayout.addLayout(self.topRebars)
            self.topveryRightLayout.addLayout(self.bottomRebars)
            self.topveryRightLayout.setAlignment(Qt.AlignCenter)
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


            self.list_of_top_widgets = list()
            self.list_of_bottom_widgets = list()
            number_of_top_widgets = int(self.top_reinf_number.currentText())
            number_of_bottom_widgets = int(self.bottom_reinf_number.currentText())


            for number in range(number_of_top_widgets):
                self.widget = QLineEdit(self)
                self.widget.setFixedSize(20, 20)
                self.list_of_top_widgets.append(self.widget)

            for number in range(number_of_bottom_widgets):
                self.widget = QLineEdit(self)
                self.widget.setFixedSize(20, 20)
                self.list_of_bottom_widgets.append(self.widget)

            for widget in self.list_of_top_widgets:
                self.topRebars.addWidget(widget)


            for widget in self.list_of_bottom_widgets:
                self.bottomRebars.addWidget(widget)


            j = 1
            while j > 0:
                self.topRebars.addWidget(QLabel("Please enter diameters in mm"))
                self.bottomRebars.addWidget(QLabel("Please enter diameters in mm"))
                j = j - 1
                self.topRebars.setAlignment(Qt.AlignCenter)
                self.bottomRebars.setAlignment(Qt.AlignCenter)



            self.topveryRightLayout.addLayout(self.topRebars)
            self.topveryRightLayout.addLayout(self.bottomRebars)
            self.topveryRightLayout.setAlignment(Qt.AlignTop)
            self.topMainLayout.addLayout(self.topLeftLayout)
            self.topMainLayout.addLayout(self.topRightLayout)
            self.topMainLayout.addLayout(self.topveryRightLayout)
            self.topMainLayout.setAlignment(Qt.AlignTop)



        except:
            self.topRebars = QHBoxLayout()
            self.bottomRebars = QHBoxLayout()

            self.list_of_top_widgets = list()
            self.list_of_bottom_widgets = list()
            number_of_top_widgets = int(self.top_reinf_number.currentText())
            number_of_bottom_widgets = int(self.bottom_reinf_number.currentText())

            for number in range(number_of_top_widgets):
                self.widget = QLineEdit(self)
                self.widget.setFixedSize(25, 25)
                self.list_of_top_widgets.append(self.widget)

            for number in range(number_of_bottom_widgets):
                self.widget = QLineEdit(self)
                self.widget.setFixedSize(25, 25)
                self.list_of_bottom_widgets.append(self.widget)

            for widget in self.list_of_top_widgets:
                self.topRebars.addWidget(widget)


            for widget in self.list_of_bottom_widgets:
                self.bottomRebars.addWidget(widget)


            j = 1
            while j > 0:
                self.topRebars.addWidget(QLabel("Please enter diameters in mm"))
                self.bottomRebars.addWidget(QLabel("Please enter diameters in mm"))
                j = j - 1
                self.topRebars.setAlignment(Qt.AlignCenter)
                self.bottomRebars.setAlignment(Qt.AlignCenter)

            self.topveryRightLayout.addLayout(self.topRebars)
            self.topveryRightLayout.addLayout(self.bottomRebars)
            self.topveryRightLayout.setAlignment(Qt.AlignTop)
            self.topMainLayout.addLayout(self.topLeftLayout)
            self.topMainLayout.addLayout(self.topRightLayout)
            self.topMainLayout.addLayout(self.topveryRightLayout)
            self.topMainLayout.setAlignment(Qt.AlignTop)

        return(self.list_of_top_widgets, self.list_of_bottom_widgets)



    def calculate_longitudinal_rebars(self):
        topRebars = self.list_of_top_widgets
        bottomRebars = self.list_of_bottom_widgets


        for rebar in topRebars:
            print("diameters of top rebars")
            print(rebar.text())



        for rebar in bottomRebars:
            print("diameters of bottom rebars")
            print(rebar.text())

















