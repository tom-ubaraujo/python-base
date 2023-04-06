#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.0"

# Dados
salas = {
    "Sala1" : {"Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"},
    "Sala2" : {"Joao", "Antonio", "Carlos", "Maria", "Isolda"},
}

atividades = {
    "Inglês" : {"Erik", "Maia", "Joana", "Carlos", "Antonio"}, 
    "Música" : {"Erik", "Carlos", "Maria"}, 
    "Dança" : {"Gustavo", "Sofia", "Joana", "Antonio"},
}

# Listar alunos em cada atividade por sala

for atividade in atividades:

    print(f"Alunos da atividade {atividade}")
    print("-" * 40)

    atividade_sala1 = atividades[atividade] & salas["Sala1"]
    atividade_sala2 = atividades[atividade] & salas["Sala2"]

    print("Sala1: ", atividade_sala1)
    print("Sala2: ", atividade_sala2)
    
    print()
    print("#" * 40 + "\n")
