# task 1
lst = ['list', 5, True, [1, 3, False, 'list2'], None]
print(lst[0], lst[-1], lst[3][2])

# task 2
lst2 = ['l', 1, 'll', 11, 'python']
lst2.append('lesson')
lst2.append('me')
lst2.pop(1)
lst2.remove('l')
print(lst2)

# task 3
lst3 = ['python','яблоко', 'груша', 'python', 'яблоко', 'банан', 'яблоко', 'python']
print(lst3.count('python'))
lst4 = [1, 2, 0, 11, 10, 330, 0, 0, 7, 0]
print(lst4.count(0))

# task 4
lst5 = ['a', 'b', 'c', 1, 2, 3, 'b']
print(lst5.index('b'))
print(lst5.index('b', 2, 7))

# task Вложенные списки
nested_list = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(nested_list[2][0])
print(nested_list[0][-1])