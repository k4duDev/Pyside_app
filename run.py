from PySide2.QtWidgets import QApplication,QDialog
from modulos.log import Inicio
import sys,os

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
     window = Inicio()
     window.show()
sys.exit(app.exec_())