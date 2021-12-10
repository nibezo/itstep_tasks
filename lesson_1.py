"""
C помощью команды print() построчно выведите на
консоль вот такое изображение ракеты:
"""
print('  ___\n .    .\n:______:\n|      |\n|      |\n|      |\n|      |')

"""
Задание 2:

Напишите программу, в которой пользователь отдельно
вводит свое имя, возраст и номер телефона, а после ввода
данных они выводятся на экран.
"""

name = input("Enter name: ")
age = int(input("Enter age: "))
phone_number = int(input("Enter phone number: "))

print(f"Your name: {name}, your age: {age}, your phone number: {phone_number}")
