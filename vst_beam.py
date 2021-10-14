import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import math
from PIL import Image
import sqlite3
import beam_insertion_intoDataBase


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
        global defaultImage
        defaultImage = QPixmap("img/img1.jpg")
        self.spacingWidget = QLabel("  ")
        self.confirmReinforcementBtn = QPushButton("Confirm number of rebars")
        self.confirmReinforcementBtn.clicked.connect(self.make_widgets)
        self.confirmDiametersBtn = QPushButton("Confirm diameters")
        self.confirmDiametersBtn.clicked.connect(self.calculate_longitudinal_rebars_area)
        self.choosePositionsTopBtn = QPushButton("Choose coordinates of top rebars")
        self.choosePositionsTopBtn.clicked.connect(self.define_top_rebars_positions)
        self.choosePositionsBottomBtn = QPushButton("Choose coordinates of bottom rebars")
        self.choosePositionsBottomBtn.clicked.connect(self.define_bottom_rebars_positions)
        self.Cross_Section_IMG = QLabel()
        beam_image = defaultImage
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

        self.saveBtn = QPushButton("Save into Database and Show Info")
        self.saveBtn.clicked.connect(self.save_and_getInfo)


    def layouts(self):
        self.mainLayout = QVBoxLayout()

        self.bottomMainLayout = QHBoxLayout()
        self.topMainLayout = QHBoxLayout()

        self.bottomMainLayout.addWidget(self.saveBtn)

        self.topLeftLayout = QVBoxLayout()
        self.topLeftLayout.addWidget(self.Cross_Section_IMG)
        self.topLeftLayout.setAlignment(Qt.AlignCenter)
        self.topRightLayout = QGridLayout()
        self.topveryRightLayout = QVBoxLayout()

        top_reinf_number_Label = QLabel(self.tr("&Choose the number of top reinforcement rebars"))
        top_reinf_number_Label.setBuddy(self.top_reinf_number)

        bottom_number_Label = QLabel(self.tr("&Choose the number of bottom reinforcement rebars"))
        bottom_number_Label.setBuddy(self.bottom_reinf_number)

        confirm_Reinforcement_Label = QLabel(self.tr("&Confirm the number of rebars"))
        confirm_Reinforcement_Label.setBuddy(self.confirmReinforcementBtn)

        confirm_Diameter_Label = QLabel(self.tr("&Confirm chosen diameters"))
        confirm_Diameter_Label.setBuddy(self.confirmDiametersBtn)

        self.choose_PositionsTop_Label  = QLabel(self.tr(" "))
        self.choose_PositionsTop_Label.setBuddy(self.choosePositionsTopBtn)

        self.choose_PositionsBottom_Label = QLabel(self.tr(" "))
        self.choose_PositionsBottom_Label.setBuddy(self.choosePositionsBottomBtn)

        self.topRightLayout.addWidget(top_reinf_number_Label, 0,0)
        self.topRightLayout.addWidget(self.top_reinf_number, 0,1)
        self.topRightLayout.addWidget(bottom_number_Label, 1, 0)
        self.topRightLayout.addWidget(self.bottom_reinf_number, 1, 1)
        self.topRightLayout.addWidget(self.confirmReinforcementBtn, 2, 0)
        self.topRightLayout.addWidget(self.confirmDiametersBtn, 2, 1)
        self.topRightLayout.addWidget(self.choose_PositionsTop_Label, 4, 0)
        self.topRightLayout.addWidget(self.choosePositionsTopBtn,4,1)
        self.topRightLayout.addWidget(self.spacingWidget, 5,0)
        self.topRightLayout.addWidget(self.spacingWidget, 5,1)
        self.topRightLayout.addWidget(self.spacingWidget, 5,2)
        self.topRightLayout.addWidget(self.choose_PositionsBottom_Label, 6, 0)
        self.topRightLayout.addWidget(self.choosePositionsBottomBtn,6,1)

        try:
            self.topRightLayout.addLayout(self.topRebars, 0, 2)
            self.topRightLayout.addLayout(self.bottomRebars, 1, 2)

        except:
            pass


        self.topMainLayout.addLayout(self.topLeftLayout)
        self.topMainLayout.addLayout(self.topRightLayout)
        self.topMainLayout.addLayout(self.topveryRightLayout)
        self.topMainLayout.setAlignment(Qt.AlignTop)

        self.mainLayout.addLayout(self.topMainLayout)
        self.mainLayout.addLayout(self.bottomMainLayout)


        self.setLayout(self.mainLayout)


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

            self.topRightLayout.addLayout(self.topRebars, 0, 2)
            self.topRightLayout.addLayout(self.bottomRebars, 1, 2)


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

            self.topRightLayout.addLayout(self.topRebars, 0, 2)
            self.topRightLayout.addLayout(self.bottomRebars, 1, 2)

        return(self.list_of_top_widgets, self.list_of_bottom_widgets)



    def calculate_longitudinal_rebars_area(self):

        try:
            self.top_reinforcements = []
            self.bottom_reinforcements = []

            for index, rebar in enumerate(self.list_of_top_widgets):
                self.top_reinforcements.append(int(rebar.text()))
            self.topReinforcementAreas = [((x / 1000) ** 2 / 4) * math.pi for x in self.top_reinforcements]
            print(self.topReinforcementAreas)
            self.top_reinforcements.clear()


            for index, rebar in enumerate(self.list_of_bottom_widgets):
                self.bottom_reinforcements.append(int(rebar.text()))
            self.bottomReinforcementAreas = [((x / 1000) ** 2 / 4) * math.pi for x in self.bottom_reinforcements]
            print(self.bottomReinforcementAreas)
            self.bottom_reinforcements.clear()

        except:
            QMessageBox.information(self, "Info", "Entries cannot be empty")

    def define_top_rebars_positions(self):
        beam_image = QPixmap("img/Coordinates_Top.jpg")
        beam_image = beam_image.scaledToWidth(256)
        beam_image = beam_image.scaledToHeight(256)
        self.Cross_Section_IMG.setPixmap(beam_image)

        self.choose_PositionsTop_Label = QLabel(self.tr("""&Choose positions of rebars
staring from the very 
top left and ending with
the very bottom right"""))
        self.choose_PositionsTop_Label.setBuddy(self.choosePositionsTopBtn)
        self.topRightLayout.addWidget(self.choose_PositionsTop_Label, 4, 0)


        try:
            for i in reversed(range(self.rebars_top_Layout.count())):
                self.rebars_top_Layout.itemAt(i).widget().setParent(None)

            self.rebars_top_Layout = QGridLayout()



            for i, rebar in enumerate(self.list_of_top_widgets):
                self.rebars_top_Layout.addWidget(QLabel("X Position"), i, 0)
                self.rebars_top_Layout.addWidget(QLineEdit(), i, 1)
                self.rebars_top_Layout.addWidget(QLabel("Y Position"), i, 2)
                self.rebars_top_Layout.addWidget(QLineEdit(), i, 3)
                self.topRightLayout.addLayout(self.rebars_top_Layout, 4+i,2)

            self.topMainLayout.setAlignment(Qt.AlignTop)


        except:
            self.rebars_top_Layout = QGridLayout()

            for i, rebar in enumerate(self.list_of_top_widgets):
                self.rebars_top_Layout.addWidget(QLabel("X Position"), i, 0)
                self.rebars_top_Layout.addWidget(QLineEdit(), i, 1)
                self.rebars_top_Layout.addWidget(QLabel("Y Position"), i, 2)
                self.rebars_top_Layout.addWidget(QLineEdit(), i, 3)
                self.topRightLayout.addLayout(self.rebars_top_Layout, 4+i, 2)

            self.topMainLayout.setAlignment(Qt.AlignTop)


    def define_bottom_rebars_positions(self):

        beam_image = QPixmap("img/Coordinates_Bottom.jpg")
        beam_image = beam_image.scaledToWidth(256)
        beam_image = beam_image.scaledToHeight(256)
        self.Cross_Section_IMG.setPixmap(beam_image)

        self.choose_PositionsBottom_Label = QLabel(self.tr("""&Choose positions of rebars
staring from the very 
bottom right and ending with
the very top left"""))
        self.choose_PositionsBottom_Label.setBuddy(self.choosePositionsTopBtn)
        self.topRightLayout.addWidget(self.choose_PositionsBottom_Label, 6, 0)

        try:
            for i in reversed(range(self.rebars_bottom_Layout.count())):
                self.rebars_bottom_Layout.itemAt(i).widget().setParent(None)

            self.rebars_bottom_Layout = QGridLayout()


            for i, rebar in enumerate(self.list_of_bottom_widgets):
                self.rebars_bottom_Layout.addWidget(QLabel("X Position"), i, 0)
                self.rebars_bottom_Layout.addWidget(QLineEdit(), i, 1)
                self.rebars_bottom_Layout.addWidget(QLabel("Y Position"), i, 2)
                self.rebars_bottom_Layout.addWidget(QLineEdit(), i, 3)
                self.topRightLayout.addLayout(self.rebars_bottom_Layout, 6+i,2)

            self.topMainLayout.setAlignment(Qt.AlignTop)

        except:
            self.rebars_bottom_Layout = QGridLayout()

            for i, rebar in enumerate(self.list_of_bottom_widgets):
                self.rebars_bottom_Layout.addWidget(QLabel("X Position"), i, 0)
                self.rebars_bottom_Layout.addWidget(QLineEdit(), i, 1)
                self.rebars_bottom_Layout.addWidget(QLabel("Y Position"), i, 2)
                self.rebars_bottom_Layout.addWidget(QLineEdit(), i, 3)
                self.topRightLayout.addLayout(self.rebars_bottom_Layout, 6+i, 2)

            self.topMainLayout.setAlignment(Qt.AlignTop)

    def save_and_getInfo(self):
        self.longitudinal_rebars = dict()
        background_img = QPixmap("img/img1.jpg")
        background_img = background_img.scaledToWidth(256)
        background_img = background_img.scaledToHeight(256)
        self.Cross_Section_IMG.setPixmap(background_img)
        ################ TOP #########################
        i = 0
        counter = 0
        while i <= self.rebars_top_Layout.count()-3:
            self.longitudinal_rebars["top"+"_"+str(counter+1)+"_"+"rebar"] = (self.rebars_top_Layout.itemAt(i+1).widget().text(),
                                                                            self.rebars_top_Layout.itemAt(i+3).widget().text(),
                                                                            self.topRebars.itemAt(counter).widget().text())
            i += 4
            counter += 1
        ################ BOTTOM #########################
        i = 0
        counter = 0
        while i <= self.rebars_bottom_Layout.count()-3:
            self.longitudinal_rebars["bottom"+"_"+str(counter+1)+"_"+"rebar"] = (self.rebars_bottom_Layout.itemAt(i+1).widget().text(),
                                                                               self.rebars_bottom_Layout.itemAt(i+3).widget().text(),
                                                                               self.bottomRebars.itemAt(counter).widget().text())
            i += 4
            counter += 1


        for rebar in self.longitudinal_rebars:

            img = Image.open("img/Rebars_Icons/rebar_"+self.longitudinal_rebars[rebar][2]+".png")
            print("2")
            background_img.paste(img, box = (int(self.longitudinal_rebars[rebar][0]), int(self.longitudinal_rebars[rebar][1])))

        background_img.save("img/img4.jpg")
        background_img = QPixmap("img/img4.jpg")
        background_img = background_img.scaledToWidth(256)
        background_img = background_img.scaledToHeight(256)
        self.Cross_Section_IMG.setPixmap(background_img)



        print(self.longitudinal_rebars)


        #self.beamEntry = beam_insertion_intoDataBase.Insertion()
        #self.close()













