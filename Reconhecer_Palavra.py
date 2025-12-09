import re

def reconhecer_palavra_e(letra):
    # Expressão regular para palavras terminadas em "E":
    regex_2 = r"\b\w*e\b"

    if re.findall(regex_2, letra, re.IGNORECASE):
        return True
    else:
        return False

# Teste de letras terminadas em "E" da questão 2. inserir letra para teste:
letra = "XXXXXX"

if reconhecer_palavra_e(letra):
    print("Palavra terminada em E!")
else:
    print("Palavra não terminada em E!")