vowels = ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'я', 'ю']
word = input("Введите слово на русском :")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(f'Слове {word} {v} букв {k}.')
