#dictionary - изменяемый иттерируемый не индексируемы упорядоченный тип данных. для хранения данных в парах

dict1 = {"a":1, "b":2, "c":3}
# создайте новый словарь, поменяв ключи со значениями
#dict2 = {1:"a", 2:"b", 3:"c"}
dict2 = {}

for key in dict1:
    dict2[dict1[key]] = key

print(dict2)

dict2 = dict()

for key, values in dict1.items():
    dict2[values] = key

print(dict2)
