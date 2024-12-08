import array

import numpy

logic = True
for foo in range(1, len(array)):
    for bar in range(foo):
        if array[foo][bar] != array[bar][foo]:
            print("Не симетрична")
            logic = False
            break
if not logic:
    pass
else:
    print("Всё же симметрична")
