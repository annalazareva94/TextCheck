import os
path = 'C:\\Users\\User\\Desktop\\Диск\\Документы\\Рассказы'
print(os.listdir(path))
def fi (path, level=1):
    print('level =', level, 'content', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path+'\\'+i):
            print('Спускаемся', path+'\\'+i)
            fi(path+'\\'+i, level+1)
            print('Возвращаемся в', path)
fi(path)
