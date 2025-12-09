import re

def verificar_cpf(cpf):
    # Expressão regular para verificar o formato do CPF
    padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
    # Verifica se o CPF corresponde ao padrão
    return re.match(padrao, cpf) is not None

# Cpf de teste para a verificação da questão 1. inserir cpf para teste:
cpf = "123.456.789-09"

if verificar_cpf(cpf):
    print("Formato de CPF válido")
else:
    print("Formato de CPF inválido")