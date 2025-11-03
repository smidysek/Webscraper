# 🕸️ Webscraper – Tomáš Šmíd

## 🎯 Úkol
Cílem bylo vytvořit program, který pomocí **web scrapingu** získá a zpracuje data  
z veřejné webové stránky. Jako cílová stránka byla zvolena  
[Wikipedia – Python (programming language)](https://en.wikipedia.org/wiki/Python_(programming_language)).

---

## 🧩 Popis programu
Program:
1. Načte HTML stránku pomocí knihovny **requests**.
2. Rozparsuje ji pomocí **BeautifulSoup**.
3. Vypíše prvních 10 nalezených odkazů (`<a>` tagů).
4. Vyhledá text obsahující klíčové slovo `"Python"`.
5. Vypíše celý text z HTML tagu, který tento text obsahuje (např. `<p>` nebo `<div>`).

---

## 🧠 Použité technologie
- **Python 3.12+**
- **Knihovny:**
  - `requests` – pro stažení obsahu webu
  - `beautifulsoup4` – pro analýzu HTML

Instalace knihoven:
```bash
pip install requests beautifulsoup4
