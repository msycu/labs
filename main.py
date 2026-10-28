from random import randint
print("Введите нужный вам вариант: ")
print("1. Готовая матрица в программе")
print("2. Задаете размеры матрицы и значения")
print("3.Задаете размеры матрицы, значения random\n",)
while True:
    choice = int(input())
    if 1 <= choice <= 3:
        break
    print("Введите корректное число!!!")
matriz = list()
def matriza(c):
    if c == 1:
        matrix = [[3, 4 ,-1 ,10 ,44],[1, 5 , -4 , -10, 5], [20 , -9, 3, 1, 0],[-40, 12 , 4 , 5, 2]]
        return matrix
    if c == 2:
        m = int(input("Введите количество столбцов: "))
        n = int(input("Введите количество строк: "))
        mat = [[0]*m for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                mat[i][j] = int(input(f"Введите [{i}] [{j}] элемент матрицы"))
        return mat
    if c == 3:
        m = int(input("Введите количество столбцов: "))
        n = int(input("Введите количество строк: "))
        mat = [[0]*m for i in range(n)]
        for i in range(0,n):
            for j in range(0,m):
                mat[i][j] = randint(-10,10)
        return mat

bloks = []
matriz = matriza(choice)
print(matriz)

for i in range(0, len(matriz[0])):
    h = []
    vrem =[]
    m = len(matriz)
    n = len(matriz[0])
    k=0
    for row in matriz:
        h.append(row[i])
    for x in h:
        if x < len(matriz):
            vrem.append(x)
    bloks.append(vrem)
maxi = 0
pov = []
for row in bloks:
    if len(row) >= maxi:
        maxi = len(row)
for row in bloks:
    if maxi == len(row):
        pov.append(row)
print(maxi,pov)








