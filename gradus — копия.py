import math
def inp_ut(x):
    while True:
        try:
            text = '{} {} {} '.format("Введите значение в Цельсиях",x,'>>>')
            a = float(input(text))
            return a
        except ValueError:
            print("Неверно.Повторите попыптку,введя верные данные")
a = inp_ut('a')
print((5/9*a)+32)


