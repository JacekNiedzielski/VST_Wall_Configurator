"""
MS SQL Server Configuration!!!
"""
server = '127.0.0.1'
port = '1433'
database = 'VST'
#username = 'username'
#password = 'password'
driver = 'SQL+SERVER'
schema = 'dbo'

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import math
from PIL import Image, ImageDraw
import sqlite3
from sqlalchemy import create_engine
import pyodbc
connection_str = f'mssql+pyodbc://{server}:{port}/{database}?driver={driver}'
engine = create_engine(connection_str)
connection = engine.raw_connection()
cur = connection.cursor()

class Insertion(QWidget):
    def __init__(self, length, width, height, concrete, reinforcement, longitudinal_rebars,
                 ro_concrete=2400, ro_reinforcement=7850, ro_CBPB=1350, board_thickness = 24):
        """
        General attributes to be used within the window:
        """
        self.length = length / 1000                         #because we want it in m
        self.width = width / 1000                           #because we want it in m
        self.height = height / 1000                         #because we want it in m
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
        self.databaseSave()

    def widgets(self):

        #Information for Bill of Quantities
        self.beam_length_Label = QLabel("Length of the beam in meters")
        self.CBPB_mass_Label = QLabel("Mass of the cement bonded particle boards makes {} kg".format(round(self.mass_CBPB, 2)))
        self.concrete_mass_Label = QLabel("Concrete's mass makes {} kg".format(round(self.mass_Concrete, 2)))

        for key in self.longitudinal_rebars:
            diameter = int(self.longitudinal_rebars[key][2]) / 1000  #so that we have them in meters
            mass = math.pi * diameter**2/4 * self.length * self.ro_reinforcement
            self.mass_reinforcement += mass
        self.reinforcement_mass_Label = QLabel("Reinforcement mass makes {} kg".format(round(self.mass_reinforcement, 2)))

        #Image
        scale = 500
        self.im = Image.new('RGBA', (int(self.width*scale+1), int(self.height*scale+1)), "white")
        draw = ImageDraw.Draw(self.im)

        #Drawing the cross section
        draw.rectangle((0, 0, self.board_thickness*scale, self.height*scale),
                       fill="green", outline="black")
        draw.rectangle((self.width*scale-self.board_thickness*scale, 0, self.width*scale, self.height*scale),
                       fill="green", outline="black")
        draw.rectangle((self.board_thickness*scale, 0, self.width*scale-self.board_thickness*scale, self.height*scale),
                       fill="grey", outline="black")
        draw.rectangle((self.board_thickness*scale, self.height*scale-self.board_thickness*scale,
                        self.width*scale-self.board_thickness*scale, self.height*scale), fill="green", outline="black")

        #Drawing reinforcement
        for key in self.longitudinal_rebars:
            initial_distanceX = int(self.longitudinal_rebars[key][0])/1000*scale - (int(self.longitudinal_rebars[key][2])/1000*scale)/2
            initial_distanceY = int(self.longitudinal_rebars[key][1])/1000*scale - (int(self.longitudinal_rebars[key][2])/1000*scale)/2
            draw.ellipse((initial_distanceX,
                          initial_distanceY,
                          initial_distanceX+int(self.longitudinal_rebars[key][2])/1000*scale,
                          initial_distanceY+int(self.longitudinal_rebars[key][2])/1000*scale), fill="red", outline="black")
        self.im.save("image.png")
        self.image = QPixmap("image.png")
        self.Cross_Section_IMG = QLabel()
        self.Cross_Section_IMG.setPixmap(self.image)

        #Bending resistance
        #First step is calculating the resultant lever arm of internal forces. For that manner we need to calculate the
        # y_coordinate of the entire reinforcement.


        self.bottom_reinforcement_total_Area = 0
        self.bottom_reinforcement_static_moment = 0
        self.top_reinforcement_total_Area = 0
        self.top_reinforcement_static_moment = 0


        for rebar in self.longitudinal_rebars:

            if rebar.startswith("bottom"):
                rebar_area = (int(self.longitudinal_rebars[rebar][2])/1000)**2/4*math.pi
                self.bottom_reinforcement_total_Area += rebar_area
                static_moment = rebar_area * int(self.longitudinal_rebars[rebar][1])/1000
                self.bottom_reinforcement_static_moment += static_moment

                self.d_bottom = self.bottom_reinforcement_static_moment / self.bottom_reinforcement_total_Area
                print(self.d_bottom)
                self.x_eff_top = (self.bottom_reinforcement_total_Area * self.reinforcement.yield_strength*10**6 /
                                      self.reinforcement.gamma) / (self.width_concrete * (self.concrete.f_ck*10**6 / self.concrete.gamma))

                self.Mrd_bottom = (self.concrete.f_ck*10**6 / self.concrete.gamma) * self.width_concrete * self.x_eff_top * (
                                        self.d_bottom - 0.5 * self.x_eff_top)/10**3
                print(self.Mrd_bottom)

            if rebar.startswith("top"):
                rebar_area = (int(self.longitudinal_rebars[rebar][2])/1000)**2/4*math.pi
                self.top_reinforcement_total_Area += rebar_area

                static_moment = rebar_area * (self.height_concrete-int(self.longitudinal_rebars[rebar][1]) / 1000)
                self.top_reinforcement_static_moment += static_moment

                self.d_top = self.top_reinforcement_static_moment / self.top_reinforcement_total_Area
                print(self.d_top)
                self.x_eff_bottom = (self.top_reinforcement_total_Area * self.reinforcement.yield_strength * 10 ** 6 /
                                  self.reinforcement.gamma) / (
                                             self.width_concrete * (self.concrete.f_ck * 10 ** 6 / self.concrete.gamma))

                self.Mrd_top = (self.concrete.f_ck * 10 ** 6 / self.concrete.gamma) * self.width_concrete * self.x_eff_bottom * (
                                          self.d_top - 0.5 * self.x_eff_bottom) / 10 ** 3
                print(self.Mrd_top)

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
    


    def databaseSave(self):
        cur.execute('INSERT INTO "VST_Beams" (Height) VALUES (100)')
        connection.commit()
        connection.close()
