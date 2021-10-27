import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import math
from PIL import Image, ImageDraw
import sqlite3


class Insertion(QWidget):
    def __init__(self, length, width, height, concrete, reinforcement, longitudinal_rebars,
                 ro_concrete=2400, ro_reinforcement=7850, ro_CBPB=1350, board_thickness = 24):
        """
        General attributes to be used within the window:
        """
        self.length = length / 1000                         #becuase we want it in m
        self.width = width / 1000                           #becuase we want it in m
        self.height = height / 1000                         #becuase we want it in m
        self.concrete = concrete
        self.reinforcement = reinforcement
        self.longitudinal_rebars = longitudinal_rebars
        self.board_thickness = board_thickness / 1000       #becuase we want it in m
        self.width_concrete = self.width - 2 * self.board_thickness
        self.height_concrete = self.height - self.board_thickness
        self.ro_concrete = ro_concrete #kg/m3
        self.ro_reinforcement = ro_reinforcement #kg/m3
        self.ro_CBPB = ro_CBPB #kg/m3
        self.mass_Concrete = self.width_concrete*self.height_concrete*self.length*self.ro_concrete
        self.mass_CBPB = (self.height * self.board_thickness * 2 + (self.width -
                         2 * self.board_thickness) * self.board_thickness) * self.length * self.ro_CBPB


        self.mass_reinforcement = 0


        super().__init__()
        self.setWindowTitle("Beam Entry")
        self.setWindowIcon(QIcon("icons/ico.ico"))
        self.setGeometry(450,150,500,550)
        self.setStyleSheet("background-color:white")
        self.UI()
        self.show()


    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        self.beam_length_Label = QLabel("Length of the beam in meters")

        self.CBPB_mass_Label = QLabel("Mass of the cement bonded particle boards makes {} kg".format(self.mass_CBPB))
        self.concrete_mass_Label = QLabel("Concrete's mass makes {} kg".format(self.mass_Concrete))


        for key in self.longitudinal_rebars:
            diameter = int(self.longitudinal_rebars[key][2]) / 1000  #so that we have them in meters
            mass = math.pi * diameter**2/4 * self.length * self.ro_reinforcement
            self.mass_reinforcement += mass
        self.reinforcement_mass_Label = QLabel("Reinforcement mass makes {}".format(self.mass_reinforcement))

        self.im = Image.new('RGBA', (int(self.width*1000), int(self.height*1000)), "white")
        draw = ImageDraw.Draw(self.im)
        print("2")
        draw.line([(0,0), (0, self.height*1000-1), (self.board_thickness*1000, self.height*1000-1), (self.board_thickness*1000,0), (0, 0)], fill="black")
        self.im.save("image.png")

        self.image = QPixmap("image.png")
        self.Cross_Section_IMG = QLabel()
        self.Cross_Section_IMG.setPixmap(self.image)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()

        self.topLeftLayout = QVBoxLayout()
        self.topRightLayout = QVBoxLayout()
        self.bottomLeftLayout = QVBoxLayout()
        self.bottomRightLayout = QVBoxLayout()

        self.topLeftLayout.addWidget(self.CBPB_mass_Label)
        self.topLeftLayout.addWidget(self.concrete_mass_Label)
        self.topLeftLayout.addWidget(self.reinforcement_mass_Label)
        self.topLeftLayout.addWidget(self.Cross_Section_IMG)

        self.topLayout.addLayout(self.topLeftLayout)
        self.mainLayout.addLayout(self.topLayout)

        self.setLayout(self.mainLayout)

