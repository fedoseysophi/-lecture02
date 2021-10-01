import math
print("Введите значения длин сторон")
print("a=? ")
a=int(input())
if a<0:
 print("Неверно")
print("b=? ")
b=int(input())
if b<0:
 print("Неверно")
print("γ=? ")
γ=int(input())
if γ<0:
 print("Неверно")
print(math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(γ))))



