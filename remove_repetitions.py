"""
Дан упорядоченный по неубыванию массив целых 32-разрядных чисел.
Требуется удалить из него все повторения.
Желательно получить решение, которое не считывает входной файл целиком в память, т.е.,
использует лишь константный объем памяти в процессе работы.
"""
import sys

n = int(sys.stdin.readline().strip())
vector, prev = [], -1
for i in range(n):
    el = sys.stdin.readline().strip()
    if el != prev:
        vector.append(el)
    prev = el
for elem in vector:
    print(elem)





