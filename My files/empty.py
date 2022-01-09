d = {}
while True:
    a = list(input().split(', '))
    if a[0] == 'конец':
        break
    else:
        key, value = a[0], a[-1]
        d[key] = d.get(key, [])
        d[key].append(int(value))
# for i in d.items():
#     d[i[0]] = sum(i[1]) / len(i[1])
# for i in sorted(d.items(), key = lambda para: (-para[1], para[0])):
#     print(i[0], i[1])
print(d)