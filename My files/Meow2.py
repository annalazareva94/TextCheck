def longest_word_in_file(file_name):
    a = open(file_name, 'r', encoding = 'utf-8')
    for i in a:
        words = i.split()
        for j in words:
            print(j)
longest_word_in_file('Энея.txt')