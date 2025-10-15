def S():
    for i in range(3):
        a, b = map(int, input(f"Введите значения a и b {i+1}-го прямоугольника ").split())
        print(f"Площадь {i+1} прямоугольника равна {a*b}")
S()