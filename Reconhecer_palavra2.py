import re

def reconhecer_palavra_ar(letra_2):
    # Expressão usada para identificar palavras que começam com "AL":
    regex_3 = r"\bal\w*\b"

    if re.findall(regex_3, letra_2, re.IGNORECASE):
        return True
    else:
        return False

# Teste para letras que começam com "AL":
letra_2 = "XXXXXXX"

if reconhecer_palavra_ar(letra_2):
    print("Palavra começou com AL")
else:
    print("Palavra não começou com AL")