#Багринцев Даниил Михайлович
#Вариант 2
n = int(input("Введите n: "))
A = []
k = 0
for i in range(n):
    B = []
    for j in range(n):
        B.append(int(input(f"Введите {k + 1} элемент ")))
        k = k + 1
    A.append(B)

magic_sum = sum(A[0])
is_magic = True

for i in range(n):
    if sum(A[i]) != magic_sum:
        is_magic = False
        break

if is_magic:
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += A[i][j]
        if col_sum != magic_sum:
            is_magic = False
            break

if is_magic:
    main_diag_sum = 0
    for i in range(n):
        main_diag_sum += A[i][i]
    if main_diag_sum != magic_sum:
        is_magic = False

if is_magic:
    secondary_diag_sum = 0
    for i in range(n):
        secondary_diag_sum += A[i][n - 1 - i]
    if secondary_diag_sum != magic_sum:
        is_magic = False

if is_magic:
    print("Да, это магический квадрат")
else:
    print("Нет, это не магический квадрат")
