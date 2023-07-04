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
cmds = ['read', 'write']
path = os.curdir
filepath = os.path.join(path, "notes.txt")

if not arguments:
    print(f"Invalid usage. Must specify subcommand {cmds}")
    sys.exit(1)
    
if arguments[0].lower() not in cmds:
    print(f"Invalid command {argument[0]}")

if arguments[0].lower() == "write":
    title = input("Title: ").strip()
    tag = input("Tag: ").strip()
    text = input("Text: ").strip()

    with open("notes.txt", "a") as file_:
       file_.write(f"{title};{tag};{text}\n")
       
elif arguments[0].lower() == "read":
    for linha in open("notes.txt", "r"):
        title, tag, text = linha.split(';')
        if arguments[1].lower() == tag.lower():
            print(f"Title: {title}; Tag: {tag}; Text: {text}")
