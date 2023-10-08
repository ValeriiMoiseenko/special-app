# TODO здесь писать код

container_count = int(input('Количество контейнеров: '))
containers = []
count = 1
container_last = 99999

while count <= container_count:
    container = int(input('Введите вес контейнера: '))
    if container > 200:
        print('Вес контейнера не должен превышать 200кг')
    else:
        if container > container_last:
            print('Этот контейнер должен весить меньше прошлого. Попробуйте другой')
            continue
        else:
            containers.append(container)
            count += 1
    container_last = container

new_container = int(input('\nВведите вес нового контейнера: '))

i_container = 0
for elem in containers:
    if new_container > elem:
        break
    i_container += 1

print(f'\nНомер, который получит новый контейнер: {i_container + 1}')
