#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2] 

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9

Os resultados ficam salvos em 'infixcalc.log'

"""

__version__ = "0.1.0"
__author__ = "Ubaraujo"
__license__ = "Unlicensed"


import os
import sys
from datetime import datetime
import logging

log = logging.Logger("hello.py", logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter('%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s')
ch.setFormatter(fmt)
log.addHandler(ch)


arguments = sys.argv[1:]

# Validação
if not arguments:
    op = input("Operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [op, n1, n2]
elif len(arguments) != 3:
    print("Número de argumentos inválidos!")
    print("ex: 'sum 5 5' ")
    sys.exit(1)

op, *nums = arguments
valid_ops = ("sum", "sub", "mul", "div")

if op not in valid_ops:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

valid_nums = []
for num in nums:
    #TODO: Repetição com while + exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valid_nums.append(num)

try:
    n1, n2 = valid_nums
except ValueError as e: 
    print(str(e))
    sys.exit(1)
    
# TODO: Usar dict de funcoes
if op == 'sum':
    result = n1 + n2
elif op == 'sub':
    result = n1 - n2
elif op == 'mul':
    result = n1 * n2
elif op == 'div':
    result = n1 / n2

print(f"O resultado é: {result} ")

path = os.curdir
filepath = os.path.join(path, "infixcalc.log")
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {op}, {n1}, {n2} = {result}\n")
except PermissionError as e:
    log.error("ERROR: %s", str(e))
    sys.exit(1)
    

