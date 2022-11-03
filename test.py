from const.CONSTANTS import MAXSTRING

print(len('Университет Иннополис приглашает посетить Дни открытых дверей абитуриентов'))

text = 'За свою карьеру я пропустил более 9000 бросков, проиграл почти 300 игр. 26 раз мне доверяли сделать финальный победный бросок, и я промахивался. Я терпел поражения снова, и снова, и снова. И именно поэтому я добился успеха.'


def format_text(text):
    lines = []
    line = []
    text = text.split()
    for word in text:
        # print([lambda a: len(a) for a in text])
        if len(' '.join(line)) < MAXSTRING:
            line.append(word)
        else:
            incorrect = line.pop()
            lines.append(' '.join(line))
            line = [incorrect, word]
    lines.append(' '.join(line))
    return lines


print(format_text(text))
