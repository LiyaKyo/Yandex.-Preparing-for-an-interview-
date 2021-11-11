"""
Требуется найти в бинарном векторе самую длинную
последовательность единиц и вывести её длину.
# Желательно получить решение, работающее за линейное время и
при этом проходящее по входному массиву только один раз.
"""

n = int(input())
vector = [int(input()) for _ in range(n)]
vector_gen = (el for el in vector)
one_count, max_one = 0, 0
for el in vector_gen:
    if el == 1:
        one_count += 1
    else:
        one_count = 0
    if max_one < one_count:
        max_one = one_count


print(max_one)
