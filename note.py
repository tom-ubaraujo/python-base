#!/usr/bin/env python3

"""Bloco de anotações. Usuário deve informar titulo, tag, texto.
salva em no arquivo notas.txt. Separados por tab(tsv).
Ao executar 'python3 note.py read' exibe todas as notas linha a linha, ou 
filtrando com --tag=geral

Como usar:

$ python3 note.py write
"""
__version__ = "0.1.0"
__author__ = "Tom Araújo"
__license__ = "Unlicensed"

import os
import sys

arguments = sys.argv[1:]

if arguments[0].lower() == "write":
    titulo = input("Título: ")
    tag = input("Tag: ")
    texto = input("Texto: ")

    with open("notas.txt", "w") as arquivo:
        arquivo.write(f"Título: {titulo}\nTag: {tag}\n{texto}\n")
        arquivo.write("--- *** ---\n")

elif arguments[0].lower() == "read":
    for linha in open("notas.txt", "r"):
        print(linha, end="")
