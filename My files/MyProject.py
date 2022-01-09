import re
from termcolor import colored
handle = open(r"C:\Users\User\Desktop\Текст.txt", "r")
textfile = handle.read().strip()
opt = re.sub(r'[^\w\s]', '', textfile) #убираем все знаки припинания
text = opt.lower().split() #устанавливаем нижний регистр букв
d = {}
for i in text:
    if len(i) > 2:
        d[i] = int(text.count(i)) #если в слове больше чем 2 буквы, создаем словарь и считаем кол-во повторений слова
for j in sorted(d.items(), key=lambda para: (-para[1], para[0])):
    print(*j) #выводим в порядке убывания количества повторений, затем по алфавиту
while True:
    word = input()
    if word == '':
        break
    else:
        for w in range(len(text)):
            if text[w] == word:
                text[w] = colored(text[w], 'red', attrs=[])
        text = str(text)
        print(text)
