#!/usr/bin/env python

"""Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

     1 x 1 = 1
     1 x 2 = 2
     1 x 3 = 3
...
##################
---Tabuada do 2---

     2 x 1 = 2
     2 x 2 = 4
     2 x 3 = 6
...
##################
"""

__version__ = "0.1.10"
__author__ = "Tom"

numeros = list(range(1, 11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}") + "\n")
    for n2 in numeros:
        print("{:^18}".format(f"{n1} X {n2} = {n1 * n2}"))
    print('\n' + "#" * 18 + '\n')
