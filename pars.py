from bs4 import BeautifulSoup
import requests
import lxml
import json

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0'
}


all_words = {}
#36623

count = 0
for i in range(27000, 36624):
    url = f'https://slovarozhegova.ru/word.php?wordid={i}'

    req = requests.get(url, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    letter = soup.find(class_='main_border').find_all('p')[5]

    all_words[i] = letter.text

    count += 1
    print(count)

with open("all_words_four.json", "w", encoding="utf-8") as file:
     json.dump(all_words, file, indent=4, ensure_ascii=False)

print('end.')




