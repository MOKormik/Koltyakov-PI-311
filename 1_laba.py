# -*- coding: utf-8 -*-
"""1 laba.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R523x8m2E5xL8coI_z9eoKz5CgD3rrRD
"""

print ("Hello world")

a = 5
b = 2
c = a + b
print (c)

side = 7.5 # сторона
base = 7.5 # основание

height = (side**2 - (base/2)**2)**0.5

area = (base * height) / 2

print(f"Площадь равнобедренного треугольника со сторонами {side} см и основанием {base} см равна {area} кв. см")

a = 5
b = 3
c = 2

x = (a**2 + b**2 - c**3) / 2

print(f"Сумма X для a={a}, b={b} и c={c} равна {x}")

a = 5

b = input("Введите значение b: ")

print(f"Вы ввели значение b: {b}")

try:
    b = float(b)
    product = a * b
    print(f"Произведение {a} и {b} равно {product}")
except ValueError:
    print("Ошибка: Введите корректное численное значение для b.")

a = input("Введите значение a: ")

b = input("Введите значение b: ")

try:
    a = float(a)
    b = float(b)

    result = (a + b) ** 2

    print(f"Сумма {a} и {b}, возведенная в квадрат, равна {result}")
except ValueError:
    print("Ошибка: Введите корректные численные значения для a и b.")

a = 15
b = 10

c = float(input("Введите значение c: "))

try:
    result = (a + b) / c

    print(f"Сумма {a} и {b}, деленная на {c}, равна {result}")
except ValueError:
    print("Ошибка: Введите корректное численное значение для c.")
except ZeroDivisionError:
    print("Ошибка: Значение c не должно быть равно нулю.")

a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

square_of_sum = (a + b) ** 2

print(f"Формула квадрата суммы ({a} + {b})^2 = {square_of_sum}")

a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2

    area = (s * (s - a) * (s - b) * (s - c))**0.5 #формула герона

    perimeter = a + b + c

    print(f"Площадь неравнобедренного треугольника: {area}")
    print(f"Периметр неравнобедренного треугольника: {perimeter}")
else:
    print("Такой треугольник не существует с заданными сторонами.")

a = float(input("Введите значение a: "))

b = float(input("Введите значение b: "))

result = ((a**3 + 14) / 5) * b

print(f"Результат выражения ((a^3 + 14) / 5) * b при a={a} и b={b} равен {result}")

number = float(input("Введите число: "))
n = float(input("Введите делитель n: "))

result = int((number**2) / n)

print(f"Квадрат числа {number} деленный на {n} без остатка равен {result}")

fraction1 = float(input("Введите первое дробное число: "))
fraction2 = float(input("Введите второе дробное число: "))

division_result = int(fraction1 / fraction2)

print(f"Результат деления {fraction1} на {fraction2} без остатка: {division_result}")

natural1 = int(input("Введите первое натуральное число: "))
natural2 = int(input("Введите второе натуральное число: "))

multiplication_result = natural1 * natural2

print(f"Результат умножения {natural1} и {natural2}: {multiplication_result}")
remainder_result = natural1 % natural2

print(f"Остаток от деления {natural1} на {natural2}: {remainder_result}")

n = int(input("Введите количество число: "))

days = n // (24 * 3600)  # 1 день = 24 часа * 3600 секунд
n %= 24 * 3600
hours = n // 3600  # 1 час = 3600 секунд
n %= 3600
minutes = n // 60  # 1 минута = 60 секунд
seconds = n % 60

print(f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд")