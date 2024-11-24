a = int(input("Введите целое число"))
b = int(input("Введите целое число"))

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)
