Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from math import tan, pi
import time

def main():
while True:
number = int(input("Введите 1 если это расчет площади правильного многоугольника или 2 для расчета суммы положительных чисел: "))
if (number == 1):
print("Вызывается функция: площадь правильного многоугольник")
regularPolygonAreaCounter()

elif(number == 2):
print("Вызывается функция: cумма первых n положительных чисел")
numberCounter()
elif(number == "выход"):
break
print("Ваше число не подходит по правилам!")
print("Введите 'выход' для выхода из программы")


def regularPolygonAreaCounter():
start_time = time.time()
length = int(input("Длина стороны: "))
count = float(input("Количество сторон: "))
regularPolygonArea = count * (length ** 2) / (4 * tan(pi / count))
print("Длина стороны: {} Количество сторон: {}".format(length, count))
print("Площадь многоугольника: {}".format(regularPolygonArea))
print("Время, затраченное на выполнение функции " "%s seconds" % (time.time() - start_time))

def numberCounter():
start_time = time.time()
number = int(input("Введите число: "))
print("Ответ")
answer = (number * (number + 1)) / 2;
print("Сумма положительных чисел: {}".format(answer))
print("Время, затраченное на выполнение функции " " %s seconds" % (time.time() - start_time))