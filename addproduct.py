import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import *
import sqlite3
import vst_beam, style
from sellings import ConfirmWindow

import inspect
from PyQt5.QtCore import QCoreApplication

from PIL import Image

con=sqlite3.connect("products.db")
cur=con.cursor()
defaultImg = "store.png"



class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
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
        ################### Widgets top layout ################
        self.list_of_buttons = []
        #Walls
        self.vstWallBtn = QPushButton("VST Wall")
        self.vstWallBtn.setStyleSheet(style.productsButtons())
        self.vstWallBtnImage = QLabel()
        self.vstWallBtnImage.setPixmap(QPixmap("icons/Wall_AddProduct_icon.jpg"))
        self.list_of_buttons.append(self.vstWallBtn)
        #Slabs
        self.vstSlabBtn = QPushButton("VST Slab")
        self.vstSlabBtn.setStyleSheet(style.productsButtons())
        self.vstSlabBtnImage = QLabel()
        self.vstSlabBtnImage.setPixmap(QPixmap("icons/Slab_AddProduct_icon.jpg"))
        self.list_of_buttons.append(self.vstSlabBtn)
        #Stairs
        self.vstStairsBtn = QPushButton("VST Stairs")
        self.vstStairsBtn.setStyleSheet(style.productsButtons())
        self.vstStairsBtnImage = QLabel()
        self.vstStairsBtnImage.setPixmap(QPixmap("icons/Stairs_AddProduct_icon.jpg"))
        self.list_of_buttons.append(self.vstStairsBtn)
        #Columns
        self.vstColumnBtn = QPushButton("VST Column")
        self.vstColumnBtn.setStyleSheet(style.productsButtons())
        self.vstColumnBtnImage = QLabel()
        self.vstColumnBtnImage.setPixmap(QPixmap("icons/Column_AddProduct_icon.png"))
        self.list_of_buttons.append(self.vstColumnBtn)
        #Beams
        self.vstBeamBtn = QPushButton("VST Beam")
        self.vstBeamBtn.setStyleSheet(style.productsButtons())
        self.vstBeamBtnImage = QLabel()
        self.vstBeamBtnImage.setPixmap(QPixmap("icons/Beam_AddProduct_icon.png"))
        self.list_of_buttons.append(self.vstBeamBtn)
        self.vstBeamBtn.clicked.connect(self.funcAddBeam)

        #Ducts
        self.vstAirLightDuctBtn = QPushButton("VST Air/Light Duct")
        self.vstAirLightDuctBtn.setStyleSheet(style.productsButtons())
        self.vstAirLightDuctBtnImage = QLabel()
        self.vstAirLightDuctBtnImage.setPixmap(QPixmap("icons/Beam_AddProduct_icon.jpg"))
        self.list_of_buttons.append(self.vstAirLightDuctBtn)
        #Roof dormers
        self.vstRoofDormerBtn = QPushButton("VST Roof Dormer")
        self.vstRoofDormerBtn.setStyleSheet(style.productsButtons())
        self.vstRoofDormerBtnImage = QLabel()
        self.vstRoofDormerBtnImage.setPixmap(QPixmap("icons/Beam_AddProduct_icon.jpg"))
        self.list_of_buttons.append(self.vstRoofDormerBtn)
        #Foundations
        self.vstFoundationBtn = QPushButton("VST Foundation")
        self.vstFoundationBtn.setStyleSheet(style.productsButtons())
        self.vstFoundationBtnImage = QLabel()
        self.vstFoundationBtnImage.setPixmap(QPixmap("icons/Beam_AddProduct_icon.jpg"))
        self.list_of_buttons.append(self.vstFoundationBtn)





    def layouts(self):
        #Layouts and Frames
        self.mainLayout = QVBoxLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()
        self.wallLayout = QVBoxLayout()
        self.slabLayout = QVBoxLayout()
        self.stairsLayout = QVBoxLayout()
        self.columnLayout = QVBoxLayout()
        self.beamLayout = QVBoxLayout()
        self.ductLayout = QVBoxLayout()
        self.roofdormerLayout = QVBoxLayout()
        self.foundationLayout = QVBoxLayout()

        #Dependencies
        self.wallLayout.addWidget(self.vstWallBtnImage)
        self.wallLayout.addWidget(self.vstWallBtn)
        self.slabLayout.addWidget(self.vstSlabBtnImage)
        self.slabLayout.addWidget(self.vstSlabBtn)
        self.stairsLayout.addWidget(self.vstStairsBtnImage)
        self.stairsLayout.addWidget(self.vstStairsBtn)
        self.columnLayout.addWidget(self.vstColumnBtnImage)
        self.columnLayout.addWidget(self.vstColumnBtn)
        self.beamLayout.addWidget(self.vstBeamBtnImage)
        self.beamLayout.addWidget(self.vstBeamBtn)
        self.ductLayout.addWidget(self.vstAirLightDuctBtnImage)
        self.ductLayout.addWidget(self.vstAirLightDuctBtn)
        self.roofdormerLayout.addWidget(self.vstRoofDormerBtnImage)
        self.roofdormerLayout.addWidget(self.vstRoofDormerBtn)
        self.foundationLayout.addWidget(self.vstFoundationBtnImage)
        self.foundationLayout.addWidget(self.vstFoundationBtn)



        self.topLayout.addLayout(self.wallLayout)
        self.topLayout.addLayout(self.slabLayout)
        self.topLayout.addLayout(self.stairsLayout)
        self.topLayout.addLayout(self.columnLayout)

        self.bottomLayout.addLayout(self.beamLayout)
        self.bottomLayout.addLayout(self.ductLayout)
        self.bottomLayout.addLayout(self.roofdormerLayout)
        self.bottomLayout.addLayout(self.foundationLayout)

        self.topFrame.setLayout(self.topLayout)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)


    def funcAddBeam(self):
        self.newBeam = vst_beam.AddBeam()
        self.close()




        """
        self.img = QPixmap("icons/addproduct.png")
        self.addProductImg.setPixmap(self.img)
        self.titleText = QLabel("Add Product")
        ################## Widgets of bottom layout ##########
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter name of product")
        self.manufacturerEntry = QLineEdit()
        self.manufacturerEntry.setPlaceholderText("Enter name of manufacturer")
        self.priceEntry = QLineEdit()
        self.priceEntry.setPlaceholderText("Enter price of product")
        self.qoutaEntry = QLineEdit()
        self.qoutaEntry.setPlaceholderText("Enter qouta of product")
        self.uploadBtn = QPushButton("Upload")
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.addProduct)
        """




"""




class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setWindowIcon(QIcon("icons/ico.ico"))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        ################### Widgets top layout ################
        self.addProductImg=QLabel()
        self.img=QPixmap("icons/addproduct.png")
        self.addProductImg.setPixmap(self.img)
        self.titleText=QLabel("Add Product")
        ################## Widgets of bottom layout ##########
        self.nameEntry=QLineEdit()
        self.nameEntry.setPlaceholderText("Enter name of product")
        self.manufacturerEntry = QLineEdit()
        self.manufacturerEntry.setPlaceholderText("Enter name of manufacturer")
        self.priceEntry=QLineEdit()
        self.priceEntry.setPlaceholderText("Enter price of product")
        self.qoutaEntry=QLineEdit()
        self.qoutaEntry.setPlaceholderText("Enter qouta of product")
        self.uploadBtn = QPushButton("Upload")
        self.uploadBtn.clicked.connect(self.uploadImg)
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.addProduct)

    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QHBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.bottomFrame=QFrame()
        ############### Add widget ##########################
        ############## Widgets of top layout ################
        self.topLayout.addWidget(self.addProductImg)
        self.topLayout.addWidget(self.titleText)
        self.topFrame.setLayout(self.topLayout)
        ############## Widgets of form layout ##############
        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("Manufacturer: "), self.manufacturerEntry)
        self.bottomLayout.addRow(QLabel("Price: "), self.priceEntry)
        self.bottomLayout.addRow(QLabel("Qouta: "), self.qoutaEntry)
        self.bottomLayout.addRow(QLabel("Upload: "), self.uploadBtn)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)


    def uploadImg(self):
        global defaultImg
        size=(256,256)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload", "", "Image Files (*.jpg *.png)")
        if ok:
            defaultImg=os.path.basename(self.filename)
            #print(defaultImg)
            #print(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("img/{0}".format(defaultImg))

    def addProduct(self):
        global defaultImg
        name = self.nameEntry.text()
        manufacturer = self.manufacturerEntry.text()
        price = self.priceEntry.text()
        qouta = self.qoutaEntry.text()

        if (name and manufacturer and price and qouta !=""):
            try:
                query = "INSERT INTO 'products' (product_name, product_manufacturer, product_price, product_qouta, product_img) VALUES (?, ?, ?, ?, ?)"
                cur.execute(query, (name, manufacturer, price, qouta, defaultImg))
                con.commit()
                QMessageBox.information(self, "Info", "Product has been added")


            except:
                QMessageBox.information(self, "Info", "Product has not been added")

        else:
            QMessageBox.information(self, "Info", "Fileds cannot be empty")


"""
