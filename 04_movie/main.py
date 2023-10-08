films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

# TODO здесь писать код

films_count = int(input('Сколько фильмов хотите добавить? '))
favourites = []

for _ in range(films_count):
    film_names = input('Введите название фильма: ')
    if film_names in favourites:
        print('Этот фильм уже добавлен в избранное!')
    elif film_names in films:
        favourites.append(film_names)
    else:
        print(f'Ошибка: фильма {film_names} у нас нет :(')

print(f'\nВаш список любимых фильмов: {favourites}')