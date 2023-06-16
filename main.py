print("Введите фразу: ", end="")
phrase = input()
phrase = phrase.split()
def count_letter(word):
    count = 0
    letters = "'аиеёоуыэюяАИЕЁОУЫЭЮЯ'"
    for letter in word:
        if letter in letters:
            count += 1
    return count
def check_rhythm(phrase):
    list = [count_letter(word) for word in phrase]
    return list

if (len(set(check_rhythm(phrase)))==1):
    print('Парам пам-пам')
else:
    print('Пам парам')