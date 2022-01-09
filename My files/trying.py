text = ['это', 'было', 'начало', 'осени','это']
from termcolor import colored
# class color:
#    RED = '\033[91m'

while True:
    word = input()
    if word == '':
        break
    else:
        for w in range(len(text)):
            if text[w] == word:
                text[w] = colored(text[w], 'red', attrs=[])
        print(*text)
