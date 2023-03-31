#!/usr/bin/env python

"""Imprime a tabuada do 1 ao 10.
"""

__version__ = "0.1.10"
__author__ = "Tom"

num = list(range(1, 11))

for n1 in num:
    print("{:-^18}".format(f"Tabuada do {n1}") + "\n")
    for n2 in num:
        print("{:^18}".format(f"{n1} X {n2} = {n1 * n2}"))
    print('\n' + "#" * 18 + '\n')
