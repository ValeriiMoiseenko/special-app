# TODO здесь писать код

# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
print(f'Изначальный список: {numbers_list}')

#Выбираем только четные элементы списка
for elem in numbers_list:
    if elem % 2 != 0:
        numbers_list.remove(elem)

print(f'\nСписок из четных чисел: {numbers_list}')

len_list = len(numbers_list)
i_number = 0

#Перезаписываем элементы списка в обратном порядке
for num in range(len_list // 2):
    numbers_list[num], numbers_list[len_list - num - 1] = numbers_list[len_list - num - 1], numbers_list[num]

print(f'Обратный список из четных чисел: {numbers_list}')