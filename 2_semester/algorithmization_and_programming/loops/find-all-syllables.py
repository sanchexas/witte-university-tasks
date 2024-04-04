# Определить количество слогов в слове
word = 'достопримечательность'
syllables = 0
for letter in word:
    if letter in 'аоиыеёэуюя': syllables += 1
print(syllables)