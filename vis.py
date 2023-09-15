word = input('Введите слово: ')
stars = '*' * len(word)
print(stars)
health = len(word)
while not (word == stars) and (health > 0):
    attempt = input('Введите букву ')
    if attempt in word:
        for i in range(len(word)):
            if word[i] == attempt:
                stars = list(stars)
                stars[i] = attempt
                stars = ''.join(stars)
        print(stars)
    else:
        health -= 1
        print(stars, 'У вас осталось', health, 'жизни')
if word == stars:
    print('Вы победили')
else:
    print('Вы проиграли')






