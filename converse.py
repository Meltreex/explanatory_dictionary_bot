import json

with open("All_words.json", "r", encoding="utf-8") as file:
    data = json.load(file)

edit_name = {}

for key, value in data.items():
    try:
        i = value.split()
        if ',' == i[0][-1]: #Проверка на вхождение запятой в слово
            k = i[0]
            k = k.replace(',', '', 1)
            edit_name[k] = value
        else:
            edit_name[i[0]] = value
    except IndexError:
        continue

with open("Edit_all_words.json", "w", encoding="utf-8") as file:
    json.dump(edit_name, file, indent=4, ensure_ascii=False)