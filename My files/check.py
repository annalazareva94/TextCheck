
def longest_word_in_file(file_name):
    a = open(file_name, 'r')
    lenn = ''
    for i in a:
        words = i.split()
        for j in words:
            j = remove_punctuation(j)
            if len(j) >= len(lenn):
                lenn = j
    return lenn

def remove_punctuation(w):
    from string import punctuation
    for s in punctuation:
        if s in w:
            w = w.replace(s, '')
    return w

print(longest_word_in_file('Энея.txt'))

