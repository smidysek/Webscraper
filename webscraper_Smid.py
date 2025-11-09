"""
Autor: Tomáš Šmíd
Předmět: Webscraping
Popis:
  Tento program stáhne veřejnou webovou stránku s výskytem jména
  'Tomáš Šmíd' z Wikipedie a vypíše vybrané informace z HTML
  pomocí knihovny BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup

# URL stránky s výskytem jména
URL = "https://cs.wikipedia.org/wiki/Tom%C3%A1%C5%A1_%C5%A0m%C3%ADd"

# 1️⃣ Stažení obsahu stránky – přidáme hlavičky pro přístup (jinak Wikipedia může vrátit 403)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)

if response.status_code != 200:
    print(f"❌ Chyba při načítání stránky: {response.status_code}")
    exit()

# 2️⃣ Parsování HTML pomocí BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3️⃣ Ukázka – vypíšeme několik odkazů (<a> tagy)
print("🔗 Odkazy na stránce:")
links = soup.find_all("a", href=True)
for link in links[:10]:  # vypíšeme jen prvních 10
    print(f" - {link.get_text(strip=True)}: {link['href']}")

# 4️⃣ Najdeme nadřazený tag, který obsahuje jméno (např. <p> nebo <div>)
search_name = "Tomáš Šmíd"
tag_with_name = soup.find(string=lambda text: text and search_name in text)

if tag_with_name:
    parent_tag = tag_with_name.find_parent()
    print("\n📍 Tag, který obsahuje jméno:")
    print(f"Typ tagu: <{parent_tag.name}>")
    print("Text z tohoto tagu:\n")
    print(parent_tag.get_text(strip=True))
else:
    print("\n⚠️ Jméno nebylo na stránce nalezeno.")
