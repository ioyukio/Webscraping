from bs4 import BeautifulSoup
import requests
import re

url = "https://www.pracuj.pl/praca/it%20-%20programowanie%20-%20analiza;kw"
result = requests.get(url)
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="listing_snf5u2y listing_pk4iags size-body listing_t1rst47b")

if page_text:
    text = str(page_text)
    pattern = r'<span data-test="top-pagination-max-page-number">(\d+)</span>'
    matches = re.findall(pattern, text)

    number = matches[0] if matches else "Nie znaleziono pasującego numeru."
    print("Liczba stron:", number)
else:
    print("Nie znaleziono elementu o klasie 'listing_snf5u2y listing_pk4iags size-body listing_t1rst47b'.")

soup = BeautifulSoup(page, 'html.parser')
stanowiska = soup.find_all('a', class_='listing_o1dyw02w listing_n194fgoq')
tryb_pracy = soup.find_all('li', class_='listing_isg28kc')
miasta = soup.find_all('h5', class_='listing_rdl5oe8')

table = []
for i in range(len(stanowiska)):
    row = {
        "Stanowisko": stanowiska[i].text.strip(),
        "Tryb pracy": tryb_pracy[i].text.strip(),
        "Miasto": miasta[i].text.strip(),
        "Link": stanowiska[i]['href']
    }
    table.append(row)

# Wyświetlanie tabeli
print("{:<30} {:<20} {:<20} {}".format("Stanowisko", "Tryb pracy", "Miasto", "Link"))
for row in table:
    print("{:<30} {:<20} {:<20} {}".format(row["Stanowisko"], row["Tryb pracy"], row["Miasto"], row["Link"]))