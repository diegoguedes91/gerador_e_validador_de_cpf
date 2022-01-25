from random import randint
from valida_cpf import validacpf

def geracpf():
    numero = str(randint(10000000000, 99999999999))

    while validacpf(numero) == False:
        numero = str(randint(10000000000, 99999999999))

    return numero

