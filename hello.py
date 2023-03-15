#!/usr/bin/env python

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Tom Araújo"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Ola Mundo!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
elif current_language == "en_US":
    msg = "Hello, World!"

print(msg)
