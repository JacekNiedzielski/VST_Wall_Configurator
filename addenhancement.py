import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image


con=sqlite3.connect("products.db")
cur=con.cursor()
defaultImg = "store.png"

class AddEnhancement(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product's Enhancement")
        self.setWindowIcon(QIcon("icons/Bautätigkeit_ohneHintergrund.png"))
        self.setGeometry(450,150,350,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()


    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        ################### Widgets top layout ################
        self.addMemberImg=QLabel()
        self.img=QPixmap("icons/addmember.png")
        self.addMemberImg.setPixmap(self.img)
        self.addMemberImg.setAlignment(Qt.AlignCenter)
        self.titleText=QLabel("Add Member")
        self.titleText.setAlignment(Qt.AlignCenter)
        ################# Widgets of bottom layout ############
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter memeber's name")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter memeber's surname")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter memeber's phone")
        self.submitBtn= QPushButton("Submit")
        self.submitBtn.clicked.connect(self.addMember)

    def layouts(self):
        self.mainLayout=QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout=QFormLayout()
        self.topFrame=QFrame()
        self.bottomFrame=QFrame()
        ############### Add widget ##########################
        ############## Widgets of top layout ################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addMemberImg)
        self.topFrame.setLayout(self.topLayout)
        ############## Widgets of bottom layout ################
        self.bottomLayout.addRow(QLabel("Name: "), self.nameEntry)
        self.bottomLayout.addRow(QLabel("Surname: "), self.surnameEntry)
        self.bottomLayout.addRow(QLabel("Phone: "), self.phoneEntry)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)


        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)




    def addMember(self):
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()

        if (name and surname and phone !=""):
            try:
                print(phone)
                print(surname)
                print(name)
                query = "INSERT INTO 'members' (member_name, member_surname, member_phone) VALUES (?,?,?)"
                cur.execute(query, (name, surname, phone))
                con.commit()
                QMessageBox.information(self, "Info", "Member has been added")
                self.nameEntry.setText("")
                self.surnameEntry.setText("")
                self.phoneEntry.setText("")

            except:
                QMessageBox.information(self, "Info", "Member has not been added")


        else:
            QMessageBox.information(self, "Info", "Fields can not be empty!")








