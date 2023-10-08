# TODO здесь писать код

print('Изменение в осноной ветке!')

word = list(input('Введите слово: '))
#list_word = list(word)
count = -1
palindrome = True

for sym in word:
    if sym != word[count]:
        palindrome = False
    count -= 1

if palindrome == True:
    print('Это слово является палиндромом')
else:
    print('Это слово НЕ является палиндромом')