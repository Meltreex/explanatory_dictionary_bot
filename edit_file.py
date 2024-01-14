# import json
#
# with open('Edit_all_words.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
#
# for key, value in data.items():
#     t = value
#     t = t.lstrip()
#     t = t.rstrip()
#     t = t.replace('\n', '')
#     t = t.replace('\r', '')
#     data[key] = t
#
# with open('Edit_all_words_2.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)


#Для перевода JSON-файла в py.
# with open('Edit_all_words.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#
# words = []
#
# for key, value in data.items():
#     words.append(key)
#
# with open('list_words.json', 'w', encoding='utf-8') as file:
#     json.dump(words, file, indent=4, ensure_ascii=False)



