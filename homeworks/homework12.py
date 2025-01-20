# task 1
student = {
    'name': 'Аружан',
    'age': 20,
    'groupe': 'IS-23'
}
student2 = {
    'groupe': 'CS-25'
}
student.update(student2)
student['hobby'] = 'чтение'
print(student['name'])
print(student)

# task 2
grades = {'math': 90, 'history': 85, 'english': 88}
grades2 = {'physics': 92}
print(grades.get('math')) 
print(grades.get('science', 'Не найдено')) 
history = grades.pop('history') 
print(history)
last_item = grades.popitem()
print(last_item)
grades.update(grades2)

# task 3
keys = ['name', 'age', 'city']
keys2= dict.fromkeys(keys, 'unknown')
keys2.update({'name': 'Али', 'age': 25, 'city': 'Алматы'})
print(keys2)

# task 4
names = ['Али', 'Айдана', 'Ермек']
names2 = {name: len(name) for name in names}
names3= dict.fromkeys(names, 'unknown')
print(names2)
print(names3)
names3.update({'Али': 'student'})
print(names3)

# task 5
user_info = {
'name': 'Диана',
'age': 22,
'city': 'Алматы',
'profession': 'дизайнер'
}

for key in user_info.keys(): 
    print(key) 

for value in user_info.values(): 
    print(value) 

for item in user_info.items(): 
    print(item) 

# task 6
'''2го задания нет...'''
products = {'apple': 50, 'banana': 30, 'cherry': 60}
for product in products:
    products[product] = int(products[product] * 1.1)
print("+10%:", products)

products['orange'] = 40

print('+ orange', products)

print("Продукты с ценой выше 50:")
for product, price in products.items():
    if price > 50:
        print(product, price)