a = int(input("Введите целое число"))
b = int(input("Введите целое число"))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
