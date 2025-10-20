#Багринцев Даниил Михайлович
#Вариант 2
n = int(input("Введите n "))
A=[]
C=[]
D=[]
k = 0
for i in range(n):
    B=[]
    for i in range(n):
        B.append(int(input(f"Введите {k + 1} элемент ")))
        k= k + 1
    A.append(B)

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(n):
    temp = A[i][0]
    A[i][0] = A[i][n-1]
    A[i][n-1] = temp

print("Матрица после обмена первого и последнего столбцов:")
for row in A:
    print(row)