import json

main_dct = {}

with open("all_words_four.json", "r", encoding="utf-8") as file:
    data4 = json.load(file)

with open("all_words_three.json", "r", encoding="utf-8") as file:
    data3 = json.load(file)

with open("all_words_two.json", "r", encoding="utf-8") as file:
    data2 = json.load(file)

with open("all_words_one.json", "r", encoding="utf-8") as file:
    data1 = json.load(file)

main_dct.update(data1)
main_dct.update(data2)
main_dct.update(data3)
main_dct.update(data4)


with open('All_words.json', 'w', encoding='utf-8') as file:
    json.dump(main_dct, file, indent=4, ensure_ascii=False)
