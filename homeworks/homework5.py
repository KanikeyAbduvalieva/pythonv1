#task 1
user_coment = input('Оставьте ваше обращение... ')
print(user_coment.center(50))
print(user_coment.count('а'), ' - "a" в вашем комментарие')

#task 2
user_coment2 = input('Текст2... ')
print(user_coment2.startswith('Привет')) 
print(user_coment2.endswith('!')) 

#task 3
user_coment3 = input('Текст3... ')
print(user_coment3.isdigit()) 
print(user_coment3.isalpha()) #True
print(user_coment3.isalnum()) 

#task 4
user_coment4 = input('Текст4... ')
print(user_coment4.replace(' ', '_'))