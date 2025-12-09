import re

def encontrar_variaveis(codigo):

    # Expressão regular para capturar nomes de variáveis na atribuição:
    padrao = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*='

    variaveis = re.findall(padrao, codigo)
    return variaveis

# Para você mudar o código para testes:
codigo = "a = 1\nb = 2"

variaveis = encontrar_variaveis(codigo)
print(variaveis)

# Saída esperada: ['a', 'b']