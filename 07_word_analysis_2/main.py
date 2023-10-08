# TODO здесь писать код

print('Новое изменение!')

word = list(input('Введите слово: '))
#list_word = list(word)
count = -1
palindrome = True

for sym in word:
    if sym != word[count]:
        palindrome = False
    count -= 1

if palindrome == True:
    print('Слово является палиндромом')
else:
    print('Слово НЕ является палиндромом')