#  Curso de Python 3 do Básico ao Avançado 
#### Desafio: Criar um gerador e validador de CPF

O programa é capaz de criar um CPF válido ou validar uma entrada de CPF pelo usuário. 

#### Para criar o layout do programa foi utilizado o Qt Designer

![imagem do Qt Designer](https://github.com/diegoguedes91/gerador_e_validador_de_cpf/blob/main/imagens/designer.png)

Após salvar o arquivo deve converter o arquivo gerado em .ui para .py. </br>
No linux utilizei o comando _pyuic5 design.ui -o design.py_ no terminal. </br>
É feito esta conversão de arquivos pois necessita importar a classe _Ui_MainWindow_ gerado pelo Qt Designer.


O modulo _valida_cpf_ é responsável por validar se o CPF é valido ou não, para saber as regras nas quais um CPF é considerado válido acesse o repositório [diegoguedes91
/
curso_python_validador_de_CPF](https://github.com/diegoguedes91/curso_python_validador_de_CPF)

* Link do repositório: [https://github.com/diegoguedes91/curso_python_validador_de_CPF](https://github.com/diegoguedes91/curso_python_validador_de_CPF)

```python
import re


def validacpf(cpf):
    cpf = str(cpf)

    cpf = re.sub(r'[^0-9]', '', cpf)

    if not len(cpf) == 11:
        return False

    if cpf == cpf[::-1]:
        return False

    soma = 0
    cpf_temp = ''
    for i, v in enumerate(range(10, 1, -1)):
        mult = v * int(cpf[i])
        soma = soma + mult
        cpf_temp += cpf[i]

    digito = 11 - (soma % 11)

    if digito > 9:
        digito = 0

    cpf_temp = cpf_temp + str(digito)

    soma = 0
    cpf_valido = ''
    for i, v in enumerate(range(11, 1, -1)):
        mult = v * int(cpf_temp[i])
        soma = soma + mult
        cpf_valido += cpf_temp[i]

    validade_digito = 11 - (soma % 11)
    if validade_digito > 9:
        validade_digito = 0

    cpf_valido = cpf_valido + str(validade_digito)

    if cpf == cpf_valido:
        return True
    else:
        return False
```

Para gerar um CPF foi criado o modulo _gera_cpf_ no qual gera 11 digitos aleatorios e valida os numeros no modulo _validacpf_, o _geracpf_ só retorna com a informação se o numero estiver válido, caso contrario é gerado novamente um novo grupo de digitos. 

```python
from random import randint
from valida_cpf import validacpf

def geracpf():
    numero = str(randint(10000000000, 99999999999))

    while validacpf(numero) == False:
        numero = str(randint(10000000000, 99999999999))

    return numero
```

Por fim temos o modulo _app_ que tem a classe _GeraValidaCPF_ responsável por gerar as informações e executar o programa:

```python
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
```

Na classe _GeraValidaCPF_ temos as funções: 

1. gera_cpf 

Ao clicar no botão *Gerar* é inserido na label o valor gerado pela função _geracpf_ do modulo _gera_cpf_.

```python
  def gera_cpf(self):
        self.labelretorno.setText(str(geracpf()))
 ```
 
![imagem do gerador de CPF](https://github.com/diegoguedes91/gerador_e_validador_de_cpf/blob/main/imagens/geracpf.png)

2. valida_cpf

Ao inserir um CPF e clicar no botão *Validar* é chamado a função _validacpf_ do modulo _valida_cpf_.


```python
def valida_cpf(self):
        cpf = self.inputvalidacpf.text()
        if validacpf(cpf) == True:
            self.labelretorno.setText(str('CPF válido!'))
        else:
            self.labelretorno.setText(str('CPF inválido!'))
```

Se a função retornar _False_ quer dizer que o CPF é inválido. 

![imagem do CPF inválido](https://github.com/diegoguedes91/gerador_e_validador_de_cpf/blob/main/imagens/cpf_invalido.png)

Se a função retornar _True_ quer dizer que o CPF é válido. 

![imagem do CPF válido](https://github.com/diegoguedes91/gerador_e_validador_de_cpf/blob/main/imagens/cpf_valido.png)


### Para executar e abrir a aplicação: 

```python
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_cpf = GeraValidaCPF()
    gera_valida_cpf.show()
    qt.exec_()
 ```

