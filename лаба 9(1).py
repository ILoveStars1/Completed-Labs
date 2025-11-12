def fac(a, b):
    if a < b:
        return a
    return fac(a - b, b)
a, b = map(int, input("Enter the numbers ").split())
answer = fac(a,b)
print(answer)