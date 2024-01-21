# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Estoque.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import template.icons_rc

class Ui_Estoque(object):
    def setupUi(self, Estoque):
        if not Estoque.objectName():
            Estoque.setObjectName(u"Estoque")
        Estoque.resize(712, 507)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Estoque.sizePolicy().hasHeightForWidth())
        Estoque.setSizePolicy(sizePolicy)
        Estoque.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.gridLayout_3 = QGridLayout(Estoque)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_Voltar = QPushButton(Estoque)
        self.btn_Voltar.setObjectName(u"btn_Voltar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_Voltar.sizePolicy().hasHeightForWidth())
        self.btn_Voltar.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Segoe UI Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Voltar.setFont(font)
        self.btn_Voltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Voltar.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 127);\n"
"   border-radius: 0px\n"
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
        icon = QIcon()
        icon.addFile(u":/image/imagens/voltar1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Voltar.setIcon(icon)
        self.btn_Voltar.setIconSize(QSize(80, 45))

        self.gridLayout_2.addWidget(self.btn_Voltar, 0, 0, 1, 1)

        self.label = QLabel(Estoque)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(30)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.btn_Cad_Produto = QPushButton(Estoque)
        self.btn_Cad_Produto.setObjectName(u"btn_Cad_Produto")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_Cad_Produto.sizePolicy().hasHeightForWidth())
        self.btn_Cad_Produto.setSizePolicy(sizePolicy2)
        self.btn_Cad_Produto.setFont(font)
        self.btn_Cad_Produto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Cad_Produto.setStyleSheet(u"QPushButton{\n"
"   border-radius: 8px\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/image/imagens/Produtos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Cad_Produto.setIcon(icon1)
        self.btn_Cad_Produto.setIconSize(QSize(45, 45))

        self.gridLayout_3.addWidget(self.btn_Cad_Produto, 1, 0, 1, 1)

        self.frame = QFrame(Estoque)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.Tab_Estoque = QTableWidget(self.frame)
        if (self.Tab_Estoque.columnCount() < 5):
            self.Tab_Estoque.setColumnCount(5)
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem.setFont(font3);
        self.Tab_Estoque.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem1.setFont(font4);
        self.Tab_Estoque.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem2.setFont(font3);
        self.Tab_Estoque.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem3.setFont(font3);
        self.Tab_Estoque.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignJustify|Qt.AlignVCenter);
        __qtablewidgetitem4.setFont(font4);
        self.Tab_Estoque.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.Tab_Estoque.setObjectName(u"Tab_Estoque")

        self.gridLayout.addWidget(self.Tab_Estoque, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)


        self.retranslateUi(Estoque)

        QMetaObject.connectSlotsByName(Estoque)
    # setupUi

    def retranslateUi(self, Estoque):
        Estoque.setWindowTitle(QCoreApplication.translate("Estoque", u"Dialog", None))
        self.btn_Voltar.setText("")
        self.label.setText(QCoreApplication.translate("Estoque", u"Controle de Estoque", None))
        self.btn_Cad_Produto.setText(QCoreApplication.translate("Estoque", u"Produtos", None))
        self.label_2.setText(QCoreApplication.translate("Estoque", u"Estoque Dispon\u00edvel", None))
        ___qtablewidgetitem = self.Tab_Estoque.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Estoque", u"Id", None));
        ___qtablewidgetitem1 = self.Tab_Estoque.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Estoque", u"Produtos", None));
        ___qtablewidgetitem2 = self.Tab_Estoque.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Estoque", u"Entrada", None));
        ___qtablewidgetitem3 = self.Tab_Estoque.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Estoque", u"Sa\u00edda", None));
        ___qtablewidgetitem4 = self.Tab_Estoque.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Estoque", u"Estoque", None));
    # retranslateUi
