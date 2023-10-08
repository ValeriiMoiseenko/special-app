# TODO здесь писать код

numbers = [1, 4, -3, 0, 10]
count = 1
print(f'Изначальный список: {numbers}')

while count < len(numbers):
    for elem in range(len(numbers) - count):
        if numbers[elem] > numbers[elem + 1]:
            numbers[elem], numbers[elem + 1] = numbers[elem + 1], numbers[elem]
    count += 1

print(f'Отсортированный список: {numbers}')