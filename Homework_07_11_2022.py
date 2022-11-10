# Функция: "А" Принимает в себя 2 числа, и выводит большее.
def greater_number(a, b):
    if a > b:
        print(a)
        return

    if b > a:
        print(b)
        return


greater_number(10, 20)


# Функция: "B" Принимает в себя 3 числа, и выводит меньшее.
def less_number(a, b, c):
    if a < b and a < c:
        print(a)
        return

    if b < a and b < c:
        print(b)
        return 

    if c < a and c < b:
        print(c)
        return 


less_number(50, 40, 30)


# Функция: "С" Принимает значение, и выводит его модуль.
def modul_chisla(a):
    if a <= 0:
        a = -1
        print(a)
        return
    if a > 0:
        print(a)
        return


modul_chisla(-1.2)


# Функция: "D" Принимает 2 значения, и выводит их сумму.
def add(a, b):
    results = (a + b)
    print(results)
    return


add(20, 20)


# Функция: "E" Принимает значение, и определяет негативное число, позитивное или НОЛЬ.
def positiv_or_negativ(a):
    if a > 0:
        print("Это число Позитивное")
        return
    if a < 0:
        print("Это число Негативное")
        return

    if a == 0:
        print("Это Ноль")
        return


positiv_or_negativ(10)
