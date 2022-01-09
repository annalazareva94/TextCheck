import json

count = 0
with open ('group_people.json') as file:
    data = json.load(file)
    for i in data:
        id_group = i['id_group']
        if i['people'][0]['gender'] == 'Female':
            gender_f = i['people'][0]['gender']

        for j in gender_f:
            year = i['people'][0]['year']
            if year > 1977:
                count += 1
            print(j, count)