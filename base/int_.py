num = 10
print(type(num)) #int

num2 = 0.5
print(type(num2)) #float
print(int(num2)) #0

print(0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1+0.1) #0.9999999999999999, а не 1.0

#decimal - е вещественное число, ятоюф работать с Decimal его нужно импортировать

from decimal import Decimal
n = '0.1'
print(Decimal(n))




# round - кругление числа
print(round(5.6)) # округление в большую сторону
print(round(5.5)) # 6
print(round(5.4)) # 5
print(round(5.499)) # 5

