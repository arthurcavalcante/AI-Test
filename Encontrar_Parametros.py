import re

def encontrar_parametros(codigo):
    # Expressão regular para encontrar tudo entre parênteses:
    regex = r'\((.*?)\)'

    parametros = re.findall(regex, codigo)

    return parametros

    # Exemplo de código de função em Python, mude se precisar:

codigo_exemplo = """
def minha_funcao(param1, param2):
    pass

def outra_funcao(a, b, c):
    return a + b + c

def funcao_sem_parametros():
    return None
"""

parametros_encontrados = encontrar_parametros(codigo_exemplo)

# Faz uma print dos parâmetros encontrados na função:
print("Parâmetros encontrados:", parametros_encontrados)