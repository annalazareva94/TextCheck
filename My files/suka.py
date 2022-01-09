classes = {}
for i in range(1, 12):
    classes[i] = classes.get(i, [])
while True:
    a = list(input().split('\t'))
    if a[0] == '':
        break
    else:
        key, value = int(a[0]), a[-1]
        classes[key].append(int(value))
print(classes)
for i in classes.items():
    if len(i[1]) == 0:
        print(i[0],'-')
    else:
        # v = sum(i[1]) / len(i[1])
        # v.tofix
        print(i[0], sum(i[1]) / len(i[1]))
