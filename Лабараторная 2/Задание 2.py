n = int(input("сколько минут прошло с начала дня ?:"))
x = n//60
if x > 23 :
        n = x % 24
z = x % 60
if 4 < x < 20:
        w = "Часов"
else:
        w="Часа"
print("Прошло",x,w,z,"Минут")
