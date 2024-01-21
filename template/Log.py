# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Log.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(445, 271)
        Login.setStyleSheet(u"background-color: rgb(0, 0, 127);")
        self.gridLayout = QGridLayout(Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(Login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setScaledContents(False)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.L_User = QLineEdit(self.frame_2)
        self.L_User.setObjectName(u"L_User")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.L_User.setFont(font1)
        self.L_User.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.L_User.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.L_User)

        self.L_Senha = QLineEdit(self.frame_2)
        self.L_Senha.setObjectName(u"L_Senha")
        self.L_Senha.setFont(font1)
        self.L_Senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.L_Senha.setMaxLength(50)
        self.L_Senha.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.L_Senha)

        self.Lbl_Acesso = QLabel(self.frame_2)
        self.Lbl_Acesso.setObjectName(u"Lbl_Acesso")
        self.Lbl_Acesso.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Lbl_Acesso.sizePolicy().hasHeightForWidth())
        self.Lbl_Acesso.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.Lbl_Acesso)


        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.Btn_Entrar = QPushButton(self.frame_2)
        self.Btn_Entrar.setObjectName(u"Btn_Entrar")
        self.Btn_Entrar.setFont(font1)
        self.Btn_Entrar.setStyleSheet(u"QPushButton{  \n"
"    background-color: rgb(0, 255, 0);\n"
"	border-radius: 8px	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  background-color:rgb(50,50,50);\n"
"  color:rgb(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color:rgb(35,35,35);\n"
"  color:rgb(200,200,200)\n"
"}")

        self.gridLayout_2.addWidget(self.Btn_Entrar, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><img src=\":/image/imagens/cade.png\"/><span style=\" color:#ffffff;\">LOGIN</span></p></body></html>", None))
        self.L_User.setPlaceholderText(QCoreApplication.translate("Login", u"Login", None))
        self.L_Senha.setInputMask("")
        self.L_Senha.setText("")
        self.L_Senha.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.Lbl_Acesso.setText("")
        self.Btn_Entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
    # retranslateUi

