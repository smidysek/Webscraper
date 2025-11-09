# 🕸️ Webscraper – Tomáš Šmíd

## 📘 Popis projektu
Tento projekt byl vytvořen jako úkol pro lekci **Webscrapingu v Pythonu**.  
Cílem bylo:
- stáhnout veřejnou webovou stránku, na které se vyskytuje jméno autora,  
- získat a analyzovat její HTML obsah pomocí knihovny **BeautifulSoup**,  
- vypsat vybrané prvky stránky (např. odkazy, nadpisy, odstavce),  
- a najít HTML tag obsahující celé jméno.

Program používá stránku Wikipedie o **Tomáši Šmídovi** – bývalém českém tenistovi.

---

## 🧠 Použité technologie
- **Python 3.11+**
- **requests** – pro stažení webové stránky  
- **BeautifulSoup (bs4)** – pro parsování HTML a extrakci dat

---

## ⚙️ Instalace knihoven
Pokud ještě nemáš potřebné balíčky, nainstaluj je příkazem:

```bash
pip install requests beautifulsoup4
```

## 🚀 Spuštění programu
```bash
python webscraper_Smid.py
```

## 🌍 Cílová stránka

Program zpracovává stránku:
https://cs.wikipedia.org/wiki/Tom%C3%A1%C5%A1_%C5%A0m%C3%ADd

## 🧾 Co skript dělá

Stáhne HTML obsah stránky s přidanými hlavičkami (pro přístup bez chyby 403).

Pomocí BeautifulSoup načte HTML a vyhledá tagy <a> (odkazy).

Vypíše prvních 10 odkazů nalezených na stránce.

Vyhledá nadřazený tag, který obsahuje jméno "Tomáš Šmíd",
a vypíše text z tohoto tagu (např. první odstavec biografie).

## 📊 Ukázkový výstup

🔗 Odkazy na stránce:
 - Wikipedie:Hlavní strana: /wiki/Wikipedie:Hlavn%C3%AD_strana
 - Česká republika: /wiki/%C4%8Cesk%C3%A1_republika
 - 1956: /wiki/1956
 - Brno: /wiki/Brno
 - Tenis: /wiki/Tenis
 - Sportovec: /wiki/Sportovec
 - 1980: /wiki/1980
 - Grand Slam: /wiki/Grand_Slam
 - Davis Cup: /wiki/Davis_Cup
 - Česko: /wiki/%C4%8Cesko

📍 Tag, který obsahuje jméno:
Typ tagu: <p>
Text z tohoto tagu:
Tomáš Šmíd (* 20. května 1956, Brno) je bývalý český profesionální tenista a reprezentant Československa.

