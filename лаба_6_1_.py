#Багринцев Даниил Михайлович
#2 вариант
number = int(input("Введите количество элементов "))
stuff = []
minimal = None
for i in range(number):
    k = int(input(f"Введите {i+1} значение "))
    stuff.append(k)
    if minimal is None or k < minimal:
        minimal = k
print(minimal)
