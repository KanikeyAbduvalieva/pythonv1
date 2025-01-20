# 1 task 
#list1 = [1, 3, 7, 8, 2, 9]
list1 = [1, 3, 7, 5, 3, 9]

for i in list1:
    if i%2==0:
        print(i)
        break
else:
    print('Четных чисел нет')

# 2 task 
list2 = [1, -3, -7, 8, 2, 9, 13, 15, -50]
count = 0

while count < len(list2):
    if list2[count]<0:
        count += 1
        continue
    print(list2[count])
    count += 1

# 3 task 
string = 'pythonv1'
counter = 0
numbers = '0123456789'

while counter < len(string):
    if string[counter] in numbers:
        print(f'Цифра найдена: {string[counter]}')
        break
    counter += 1
else:
    print('Цифр в строке нет')

# 4 task 
list3 = [1, 3, 6, -7, 8, 2, 9, 13, 15, 50, 10]
#list4 = [1,2,3,4,5,6,7,8,9,10]
for j in list:
    if j % 3 == 0 and j % 5 == 0:
        print(j)
        break
else:
    print("Число, которое делится на 3 и 5, отсутствует.")

# 5 task 
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_even_numbers = 0

for i in list5:
    if i%2!=0:
        continue
    else:
        sum_of_even_numbers += i
print(f"Сумма четных чисел списка: {sum_of_even_numbers}")