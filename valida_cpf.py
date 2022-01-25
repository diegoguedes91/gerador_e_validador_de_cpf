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

