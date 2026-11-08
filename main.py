from random import randint

print("Введите нужный вам вариант: ")
print("1. Готовая матрица в программе")
print("2. Задаете размеры матрицы и значения")
print("3.Задаете размеры матрицы, значения random", )
while True:
    choice = int(input("Ваш выбор: "))
    if 1 <= choice <= 3:
        break
    print("Введите корректное число!!!")


def create_matrix(c):
    if c == 1:
        matrix = [[3, 4, -1, 10, 44], [1, 5, -4, -10, 5], [20, -9, 3, 1, 0], [-40, 12, 4, 5, 2]]
        return matrix
    if c == 2:
        while True:
            m = int(input("Введите количество столбцов: "))
            if m > 0:
                break
            print("Введите корректное число столбцов!!!")
        while True:
            n = int(input("Введите количество строк: "))
            if n > 0:
                break
            print("Введите корректное число строк!!!")
        mat = [[0] * m for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                mat[i - 1][j - 1] = int(input(f"Введите [{i}] [{j}] элемент матрицы: "))
        return mat
    if c == 3:
        while True:
            m = int(input("Введите количество столбцов: "))
            if m > 0:
                break
            print("Введите корректное число столбцов!!!")
        while True:
            n = int(input("Введите количество строк: "))
            if n > 0:
                break
            print("Введите корректное число строк!!!")
        A = int(input("Задайте начало диапазона"))
        while True:
            B = int(input("Задайте конец диапазона: "))
            if A < B:
                break
            print("ОШИБКА конец не может быть меньше начала и не могут быть равными")
        mat = [[0] * m for i in range(n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                mat[i - 1][j - 1] = randint(A, B)
        return mat
    return []


bloks = []
matriz = create_matrix(choice)
for row in matriz:
    print('|', end="")
    for i in range(len(row)):
        print(f"{row[i]:^3} ", end="")
    print('|')
for i in range(0, len(matriz[0])):
    h = []
    vrem = []
    m = len(matriz)
    n = len(matriz[0])
    k = 0
    for row in matriz:
        h.append(row[i])
    for x in h:
        if x < len(matriz):
            vrem.append(x)
    bloks.append(vrem)
maxi = 0
pov = []
num = 1
for row in bloks:
    if len(row) >= maxi:
        maxi = len(row)
print("Номера столбцов:")
for row in bloks:
    if maxi == len(row):
        pov.append(row)
        print("№", num, bloks[num - 1], end=", ")
    num = num + 1
print(f"\nМаксиальноемчисло элементов меньше чем m: {maxi} \nЭлементы Столбцов:{pov}")
