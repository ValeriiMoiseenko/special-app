# TODO здесь писать код

card_count = int(input('Количество видеокарт: '))
list_card = []

for _ in range(card_count):
    video_card = int(input(' Видеокарта: '))
    list_card.append(video_card)

print(f'\nСтарый список видеокарт: {list_card}')

max_card = max(list_card)

while max_card in list_card:
    list_card.remove(max_card)

print(f'Новый список видеокарт: {list_card}')
