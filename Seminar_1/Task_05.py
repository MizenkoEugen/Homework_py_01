# Напишите программу, которая принимает на вход координаты двух точек и находит 
# расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x = x1 - x2
y = y1 - y2
lenght = (x**2 + y**2)**(0.5)
print(round(lenght,10))