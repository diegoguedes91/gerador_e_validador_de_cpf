import sys
from valida_cpf import validacpf
from gera_cpf import geracpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design

class GeraValidaCPF(design.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btngeracpf.clicked.connect(self.gera_cpf)
        self.btnvalidacpf.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelretorno.setText(str(geracpf()))

    def valida_cpf(self):
        cpf = self.inputvalidacpf.text()
        if validacpf(cpf) == True:
            self.labelretorno.setText(str('CPF válido!'))
        else:
            self.labelretorno.setText(str('CPF inválido!'))

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()


