'''
Напишите программу, которая принимает на вход вещественное число
и показывает сумму его цифр
Пример:
6782 -> 23
0,56 -> 11
'''

print("Введите число:")
num = input()

sum = 0
for n in num:
    if (n.isdigit()):
        sum += int(n)

print(sum)