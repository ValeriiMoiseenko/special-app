# TODO здесь писать код

number = int(input('Введите число: '))
list_numbers = []

for num in range(1, number + 1):
    if num % 2 != 0:
       list_numbers.append(num)

print(f'Список из нечётных чисел от одного до {number}: {list_numbers}')