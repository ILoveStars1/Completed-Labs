#Багринцев Даниил Михайлович
print("\n1. Вывод чисел от A до B включительно:")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
print("Результат:")
for i in range(A, B + 1):
    print(i, end=" ")
print()

print("\n2. Вывод чисел в порядке возрастания или убывания:")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
print("Результат:")
if A < B:
    for i in range(A, B + 1):
        print(i, end=" ")
else:
    for i in range(A, B - 1, -1):
        print(i, end=" ")
print()

print("\n3. Нечетные числа от A до B в порядке убывания (A > B):")
A = int(input("Введите A: "))
B = int(input("Введите B: "))
print("Результат:")
for i in range(A, B - 1, -1):
    if i % 2 != 0:
        print(i, end=" ")
print()

print("\n4. Сумма N чисел:")
n = int(input("Введите количество чисел N: "))
total = 0
print(f"Введите {n} чисел:")
for _ in range(n):
    total += int(input())
print(f"Сумма: {total}")

print("\n5. Сумма кубов чисел от 1 до n:")
n = int(input("Введите n: "))
total = 0
for i in range(1, n + 1):
    total += i ** 3
print(f"Сумма кубов: {total}")

print("\n6. Факториал числа n:")
n = int(input("Введите n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

print("\n7. Сумма факториалов от 1! до n!:")
n = int(input("Введите n: "))
total = 0
current_factorial = 1
for i in range(1, n + 1):
    current_factorial *= i
    total += current_factorial
print(f"Сумма факториалов: {total}")

print("\n8. Лесенка из n ступенек:")
n = int(input("Введите n (≤9): "))
print("Лесенка:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

print("\n9. Сумма N чисел Фибоначчи:")
n = int(input("Введите N: "))
if n == 0:
    result = 0
elif n == 1:
    result = 1
else:
    a, b = 0, 1
    result = 1
    for _ in range(2, n):
        a, b = b, a + b
        result += b
print(f"Сумма {n} чисел Фибоначчи: {result}")

print("\n10. Сумма N чисел Фибоначчи начиная с K-го номера:")
N = int(input("Введите N: "))
K = int(input("Введите K: "))

if K == 1:
    a, b = 0, 1
elif K == 2:
    a, b = 1, 1
else:
    a, b = 1, 1
    for _ in range(3, K + 1):
        a, b = b, a + b

if N == 1:
    total = a
elif N == 2:
    total = a + b
else:
    total = a + b
    for _ in range(2, N):
        a, b = b, a + b
        total += b

print(f"Сумма {N} чисел Фибоначчи начиная с {K}-го: {total}")

