# task 1
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

set_a.add(10)
set_b.remove(4)
set_a_pop =set_a.pop()
print(f'{set_a_pop} - "случайно" удаленный элемент')
set_a.update(set_b)
print(set_a.difference(set_b))

# task 2
user_numbers = input('Введите числа через пробел: ')
user_numbers_set = set(user_numbers)
user_numbers = user_numbers_set
print(f'{user_numbers} - уникальные числа')
 
'''Второй вариант:

user_numbers = input('Введите числа через пробел: ')

for char in user_numbers:
    if not (char in '0123456789 '):
        print('Ошибка: вводить нужно только числа!')
        break
else:
    user_numbers_set = set(user_numbers.replace(' ', ''))
    print(f'{user_numbers_set} - уникальные числа')'''

# task 3. extra task
user_input = input('Введите числа через пробел: ')
numbers_t = tuple(user_input.split()) 
unique_numbers = set()
counter = 0

for num in numbers_t:
    if numbers_t.count(num) > 1 and num not in unique_numbers:
        counter += 1
        unique_numbers.add(num)

print(f'Количество повторяющихся элементов: {counter}')

# task 4
tup_num = (3, 6, 3, 7, 9, 3, 10)
index7 = tup_num.index(7)
count3 = tup_num.count(3)
print(f'Индекс числа "7" - {index7} \nЧисло "3" встречается - {count3} раза')

# task 5
tuple_nums = (1, 2, 3, 5, 7)
#tuple_nums[0] = 10
#print(tuple_nums)
'''" 'tuple' object does not support item assigment " - означает что кортежи не поддерживают изменений. Так как tuple - это не изменяемый тип данный, т.е. ее нельзя менять (удалять элементы внутри кортежа, добавлять и т.д.) '''

# While. Number's sum. Extra task
num_sum = 0

while True:
    num = int(input('Введите число: '))
    if num == 0:
        break
    num_sum += num

print(f'{num_sum} - сумма введенных пользователем чисел')

# 'Password' task. Extra task
chance = 3
password = 'python123'

while chance > 0:
    user_pas = input('Введите пароль: ')
    if user_pas == password:
        print('Доступ разрешен.')
        break
    else:
        chance -= 1
        if chance > 0:
            print(f'Неверный пароль. Осталось попыток: {chance}')
        else:
            print('Попытки исчерпаны. Доступ запрещен.')