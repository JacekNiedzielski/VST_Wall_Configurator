import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import sqlite3
import style
from PIL import Image


con=sqlite3.connect("products.db")
cur=con.cursor()

defaultImg = "store.png"

confirmation = ""


class SellProducts(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Product")
        self.setWindowIcon(QIcon("icons/ico.ico"))
        self.setGeometry(450,150,350,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()


    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ################ Top layout's widgets ##############################
        self.sellProductImg =QLabel()
        self.img=QPixmap('icons/shop.png')
        self.sellProductImg.setPixmap(self.img)
        self.sellProductImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Sell Products")
        self.titleText.setAlignment(Qt.AlignCenter)
        ################ Bottom layout's widgets ##############################
        self.productCombo = QComboBox()
        self.productCombo.currentIndexChanged.connect(self.changeComboValue)
        self.memberCombo = QComboBox()
        self.quantityCombo = QComboBox()
        self.submitBtn = QPushButton("Submit")
        self.submitBtn.clicked.connect(self.sellProduct)

        query1=("SELECT * FROM products WHERE product_availability=?")
        products=cur.execute(query1, ("Available", )).fetchall()
        query2=("SELECT member_id, member_name FROM members")
        members=cur.execute(query2).fetchall()
        quantity=products[0][4]

        for product in products:
            self.productCombo.addItem(product[1], product[0])


        for member in members:
            self.memberCombo.addItem(member[1], member[0])

        for i in range(1, quantity+1):
            self.quantityCombo.addItem(str(i))



    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout=QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.sellProductTopFrame())
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.sellProductBottomFrame())
        ############### Add widgets ###################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.sellProductImg)
        self.topFrame.setLayout(self.topLayout)

        self.bottomLayout.addRow(QLabel("Product: "), self.productCombo)
        self.bottomLayout.addRow(QLabel("Member: "), self.memberCombo)
        self.bottomLayout.addRow(QLabel("Quantity: "), self.quantityCombo)
        self.bottomLayout.addRow(QLabel(""), self.submitBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)

        self.setLayout(self.mainLayout)

    def changeComboValue(self):
        self.quantityCombo.clear()
        product_id = self.productCombo.currentData()
        query = ("SELECT product_qouta FROM products WHERE product_id = ?")
        qouta = cur.execute(query, (product_id,)).fetchone()

        for i in range(1, qouta[0]+1):
            self.quantityCombo.addItem(str(i))

    def sellProduct(self):
        global productName, productId, memberName, memberId, quantity
        productName=self.productCombo.currentText()
        productId=self.productCombo.currentData()
        memberName=self.memberCombo.currentText()
        memberId=self.memberCombo.currentData()
        quantity=int(self.quantityCombo.currentText())

        self.confirm = ConfirmWindow()
        self.close()


class ConfirmWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sell Product")
        self.setWindowIcon(QIcon("icons/icon.ico"))
        self.setGeometry(450,150,350,600)
        self.setFixedSize(self.size())
        self.UI()
        self.show()


    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        ################ widgets for the top layout ###############
        self.addSellProductImg = QLabel()
        self.img = QPixmap('icons/shop.png')
        self.addSellProductImg.setPixmap(self.img)
        self.addSellProductImg.setAlignment(Qt.AlignCenter)
        self.titleText = QLabel("Sell Product")
        self.titleText.setAlignment(Qt.AlignCenter)
        ################ widgets for the bottom layout
        global productName, productId, memberName, memberId, quantity
        priceQuery = "SELECT product_price FROM products WHERE product_id=?"
        price=cur.execute(priceQuery, (productId, )).fetchone()
        self.amount = quantity*price[0] #because the price is an one element tuple
        self.productName = QLabel()
        self.productName.setText(productName)
        self.memberName = QLabel()
        self.memberName.setText(memberName)
        self.amountLabel = QLabel()
        self.amountLabel.setText(str(price[0])+" x "+str(quantity)+" = "+str(self.amount))
        self.confirmBtn = QPushButton("Confirm")
        self.confirmBtn.clicked.connect(self.funcConfirm)




    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.topFrame.setStyleSheet(style.confirmProductTopFrame())
        self.bottomFrame = QFrame()
        self.bottomFrame.setStyleSheet(style.confirmProductBottomFrame())
        ################### add widgets ################
        self.topLayout.addWidget(self.titleText)
        self.topLayout.addWidget(self.addSellProductImg)
        self.topFrame.setLayout(self.topLayout)
        self.bottomFrame.setLayout(self.bottomLayout)

        self.bottomLayout.addRow(QLabel("Product: "), self.productName)
        self.bottomLayout.addRow(QLabel("Member: "), self.memberName)
        self.bottomLayout.addRow(QLabel("Label: "), self.amountLabel)
        self.bottomLayout.addRow(QLabel(""), self.confirmBtn)

        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)


    def funcConfirm(self):
        global productName, productId, memberName, memberId, quantity, confirmation
        try:
            sellQuery = ("INSERT INTO 'sellings' (selling_product_id, selling_member_id, selling_quantity, selling_amount) VALUES (?,?,?,?)")
            cur.execute(sellQuery, (productId, memberId, quantity, self.amount))
            qoutaQuery="SELECT product_qouta FROM products WHERE product_id=?"
            self.qouta=cur.execute(qoutaQuery, (productId,)).fetchone()
            con.commit()
            
            
            if (quantity == self.qouta[0]):
                updateQoutaQuery = ("UPDATE products set product_qouta=?, product_availability=? WHERE product_id=?")
                cur.execute(updateQoutaQuery, (0, "Not available", productId))
                con.commit()

            else:
                newQouta=(self.qouta[0] - quantity)
                updateQoutaQuery = "UPDATE products set product_qouta=? WHERE product_id=?"
                cur.execute(updateQoutaQuery, (newQouta, productId))
                con.commit()


            QMessageBox.information(self, "Info", "Success")

            confirmation = "Yes"
            return confirmation

        except:
            QMessageBox.information(self, "Info", "Sth went wrong..please try again later")










