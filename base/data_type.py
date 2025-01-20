'==============Переменные=============='
# Переменная - это ссылка на ячейку памяти, где хранятся какие-то данные для дальнейшего использования этих данных, при помощии обращения к названию переменной

#number1=123
#number2=35
#print(number1 + number2)

'==============Правила наименования переменных=============='
#name = input('Ваше имя и фамилия: ')
#print(name)


                #### Методы строк ####
print('hello'.center(11)) #перемешает слово на середину 11 пробелов
print('hello'.center(11),'*') #тоже самое, но вместо пробелов звездочка ***hello***

print('hello world'.count('l')) #3
print('hello world'.count('ll')) #1

print('hello world'.startswith('he')) #True

print('hello world'.endswith('he')) #False
print('hello world'.endswith('d')) #True

print('hello world'.islower()) #True
print('heLlo world'.islower()) #False
print('Hello world'.isupper()) #False
print('hello world'.isupper()) #False
print('HELLO WORLD'.isupper()) #True

print('hello'.isdigit()) #False
print('hello1432'.isdigit()) #False
print('5895'.isdigit()) #True
print('43.43'.isdigit()) #False)
print('5895   '.isdigit()) #False

print('hello'.isalpha()) #True
print('hello123'.isalpha()) #False
print('867'.isalpha()) #False
print('hello   '.isalpha()) #False
print('hello 123'.isalpha()) #False
print('hello123'.isalpha()) #True
print('hello'.isalpha()) #True
print('11221'.isalpha()) #True

print('hello world'.replace('e', 'i')) #hillo world
print('hello world'.replace('o', 'i')) #helli wirld
print('hello world'.replace('o', 'i', 1)) #helli world

'''.split()
.join()'''


#      ********Индексы********* Срезы **********
# Индексы(Index) - порядковый номер элемента, последовательности. индексация начинается с нуля
'h e l l o   w o r l d'
'0 1 2 3 4 5 6 7 8 9 10'
'. . . . . . . . . -2 -1'
string = 'hello world'
print(string[0])

# срез - подстрока стпрки (часть строки) - str[start:end:step]
print(string[2:5]) # llo
print(string[0:4]) # hell
print(string[4:]) # o world
print(string[4:]) # hello world
print(string[4: :2]) # hlowrd
print(string[::-1]) # dlrow olleh
 