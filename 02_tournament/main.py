# TODO здесь писать код

print('Проверяем новую ветку')

list_names = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_list_names = []

for elem in range(len(list_names)):
    if elem % 2 == 0:
        new_list_names.append(list_names[elem])

print(f'Первый день: {new_list_names}')