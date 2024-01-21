from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from template.Calendario import Ui_Calendario

class Data(QDialog):
    def __init__(self,diaFormat,*args,**argvs):
        super(Data, self).__init__(*args,**argvs)
        self.Cal = Ui_Calendario()
        self.Cal.setupUi(self)
        self.setWindowTitle("Mk.Cosmeticos")
        appIcon = QIcon(u"/imagens/Fundo.png")
        self.setWindowIcon(appIcon)
        
        self.Cal.Calendario.selectionChanged.connect(self.Funcao)
        
    def Funcao(self):
        
        self.dia = str(self.Cal.Calendario.selectedDate())
        self.diaFormat = self.dia[21:33]
        self.Cal.data.setText(self.diaFormat)
        #self.ui.L_Data.setText(self.Cal.data)
        return self.diaFormat
        
    