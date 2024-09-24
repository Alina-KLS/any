from math import sqrt, cos, radians
a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
x = int(input("Введите величину угла в градусах: "))
x1 = radians(x)

c = sqrt(a**2+b**2-2*a*b*cos(x1))

if a+b>c and a+c>b and b+c>a and 0<=x<=360:
    print("Третья сторона: ", c)
else:
    print("Такого треугольника не существует.")
