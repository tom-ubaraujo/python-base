#!/usr/bin/env python

"""Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente...

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Tom Araújo"
__license__ = "Unlicense"


import os

current_language = os.getenv("LANG", "pt_BR")[:5]

msg = {
    "pt_BR" : "Ola Mundo!",
    "it_IT" : "Ciao, Mondo!",
    "es_SP" : "Hola, Mundo!",
    "fr_FR" : "Bonjour Monde!",
    "en_US" : "Hello, World!",
}

print(msg[current_language])
