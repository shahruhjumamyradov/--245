string = "Это строка со многими точками. Удалим точки."
count = string.count('.')
string = string.replace('.', '')
print(f"Удалено {count} точек. Новая строка: {string}")
