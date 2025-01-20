# task 1
product_list = input('Введите список продуктов через запятую: ').split(',')
product_list_extra = input('Введите дополнительные товары через пробел: ').split()
product_list.extend(product_list_extra)

print(f'Ваш список: {product_list}')

print('Хотите yдалить последний товар? (да/нет):')
product_list.pop()
print(f'Ваш список: {product_list}')

print('Хотите развернуть список? (да/нет):')
product_list.reverse() 
print(f'Ваш список: {product_list}')

print('Хотите отсортировать список? (да/нет):')
product_list.sort() 
print(f'Ваш список: {product_list}')

print(f'Длинна списка: {len(product_list)}')

print('Желаете очистить список? (да/нет):')
clear_or_not_answer = input('Введите "да", если вы хотите очистить список и "нет", если вы не хотите очищать список ... ')
if clear_or_not_answer == 'да':
    product_list.clear()
    print('Список очищен.')
elif clear_or_not_answer == 'нет':
    print(f'Tекущиe товары {product_list}')
else:
    print('Нужно вводить толь "да" или "нет"')

count = 0
print('Ваши товары по порядку:')
for i in product_list:
    count+=1
    print(f'{count}. {i}') 

product_list[0], product_list[-1] = product_list[-1], product_list[0]
print(f'Меняем местами первый и последний товары. \nОбновлённый список: {product_list}')

print('Список товаров в строку с разделителем ":":')
product_string = ': '.join(product_list)
print(product_string)

# Доп. задание
# Задание 1
counter = 0
user_str = input('Введите строку: ').lower() 
for i in user_str:
    if i in 'аеёиоуыэюя':  
        counter += 1
print(f'{counter} - гласных в строке')

# Задание 2
user_nums = input('Введите числа через пробел: ')  
even_numbers = []
user_list = [int(i) for i in user_nums.split()]  
for i in user_list:
    if i%2==0:
        even_numbers.append(i)  
print(f'Чётные числа: {even_numbers}')

# Задание 3
word = "pomidor"
user_word = input("Введите строку: ").lower()  
result = ''

for i in word:
    if i in user_word:
        result += i 
    else:
        result += "_"  
        
print(f"Вывод: {result}")
