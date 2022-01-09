from requests import get
handle = open(r"C:\Users\User\Desktop\dataset_3378_3.txt", "r")
a = handle.read().strip()
text = get(a).text
while a[0:2] != 'We':
    a = 'https://stepic.org/media/attachments/course67/3.6.3/' + text
    text = get(a).text
    print(text)

