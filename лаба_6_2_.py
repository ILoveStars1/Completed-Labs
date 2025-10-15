#Багринцев Даниил Михайлович
#2 вариант
number = int(input("Введите количество элементов: "))
stuff = []
positive = []
other = []
for i in range(number):
    num2 = int(input(f"Введите {i+1} число: "))  
    stuff.append(num2)
for k in range(number):
    if stuff[k] > 0:  
        positive.append(stuff[k])
    else:
        other.append(stuff[k])
print("Положительные числа:", positive)
print("Остальные числа:", other)
