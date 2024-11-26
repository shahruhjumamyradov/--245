def g2(x, y):
    return x**2+y**2  # вычисляем только квадрат гипотенузы [1](https://www.CyberForum.ru/python-tasks/thread2975771.html)

a1, b1 = map(float, input("Катеты первого треугольника a1, b1 = ").split())
a2, b2 = map(float, input("Катеты второго треугольника a2, b2 = ").split())
c1 = g2(a1, b1)
c2 = g2(a2, b2)
if c1 == c2:
    print("Гипотенузы равны")
else:
    print("Гипотенуза первого треугольника больше" if c1>c2 else "Гипотенуза второго треугольника больше")
