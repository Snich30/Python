import math

def add(x, y):
    '''Сложение'''
    return x + y

def subtract(x, y):
    '''Вычитание'''
    return x - y

def multiply(x, y):
    '''Умножение'''
    return x * y

def divide(x, y):
    '''Деление'''
    try:
        return x / y
    except TypeError:
        return "Ошибка введения"

def power(x, y):
    '''Возведение в степень'''
    try:
        return x ** y
    except TypeError:
        return "Ошибка введения"

def square_root(x):
    '''Квадратный корень'''
    try:
        return math.sqrt(x)
    except TypeError:
        return "Ошибка введения"

def cube_root(x):
    '''Кубический корень'''
    try:
        return x ** (1 / 3)
    except TypeError:
        return "Ошибка введения"

def sine(x):
    '''Синус'''
    try:
        return math.sin(x)
    except TypeError:
       return "Ошибка введения"

def cosine(x):
    '''Косинус'''
    try:
        return math.cos(x)
    except TypeError:
        return "Ошибка введения"

def tangent(x):
    '''Тангенс'''
    try:
        return math.tan(x)
    except TypeError:
        raise ValueError

'''Меню калькулятора'''
print("Выберите операцию.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Квадратный корень")
print("7. Кубический корень")
print("8. Синус")
print("9. Косинус")
print("10. Тангенс")
print('')
choice = input("Введите номер операции (1/2/3/4/5/6/7/8/9/10): ")
print('')
if choice in ('1', '2', '3', '4', '5'):
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "**", num2, "=", power(num1, num2))
elif choice in ('6', '7', '8', '9', '10'):
    num = float(input("Введите число: "))
    if choice == '6':
        print("Квадратный корень из", num, "=", square_root(num))
    elif choice == '7':
        print("Кубический корень из", num, "=", cube_root(num))
    elif choice == '8':
        print("Синус", num, "=", sine(num))
    elif choice == '9':
        print("Косинус", num, "=", cosine(num))
    elif choice == '10':
        print("Тангенс", num, "=", tangent(num))
else:
    print("Неверный ввод")