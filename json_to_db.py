import json

from Base import Database

db = Database('explanatory')

with open('Edit_all_words_2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

count = 0

for key, value in data.items():
    db.add(key, value)
    count += 1
    print(count)
