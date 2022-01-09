# handle = open(r"C:\Users\User\Desktop\dataset_3380_5.txt", "r")
# a = handle.read().lower().strip()
d = {}
# math = []
# phiz = []
# rus = []
while True:
    a = list(input().split('\t'))
    if a[0] == '':
        break
    else:
        key, value = int(a[0]), a[-1]
        d[key] = d.get(key, value)
print(d)
