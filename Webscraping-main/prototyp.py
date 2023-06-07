from bs4 import BeautifulSoup
import requests
import re
url = "https://www.pracuj.pl/praca/it%20-%20programowanie%20-%20analiza;kw"
result = requests.get(url)
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
#print(doc.prettify())

page_text = doc.find(class_="listing_snf5u2y listing_pk4iags size-body listing_t1rst47b")

#print(page_text)

if page_text:
    text = str(page_text)
    pattern = r'<span data-test="top-pagination-max-page-number">(\d+)</span>'
    matches = re.findall(pattern, text)

    number = matches[0]
    if matches:
        number = matches[0]
        print(number)  # Wyświetli: 16
    else:
        print("Nie znaleziono pasującego numeru.")
else:
    print("Nie znaleziono elementu o klasie 'listing_snf5u2y listing_pk4iags size-body listing_t1rst47b'.")

soup = BeautifulSoup(page, 'html.parser')
stanowiska = soup.find_all('a', class_='listing_o1dyw02w listing_n194fgoq')

Tryb_pracy = soup.find_all('li', class_='listing_isg28kc')

Miasta= soup.find_all('h5', class_='listing_rdl5oe8')

elements = soup.find_all('a', class_='listing_n194fgoq')

for element in elements:
    link = element['href']
    print(link)

print(link)