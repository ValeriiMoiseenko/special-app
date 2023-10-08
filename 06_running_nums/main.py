# TODO здесь писать код

list_start = [1, 4, -3, 0, 10]
list_shift = []

shift = int(input('Сдвиг: '))
print(f'Изначальный список: {list_start}')

for elem in range(-shift, 0):
    list_shift.append(list_start[elem])

for num in list_start:
    if num in list_shift:
        continue
    else:
        list_shift.append(num)

print(f'Сдвинутый список: {list_shift}')

