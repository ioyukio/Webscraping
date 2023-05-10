import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_job_offers(url):
    job_offers = []

    response = requests.get(url)
    html = response.content

    soup = BeautifulSoup(html, 'html.parser')
    job_offers_html = soup.find_all('div', {'class': 'single-result'})

    for offer in job_offers_html:
        title = offer.find('a', {'class': 'offer-title__link'}).text.strip()
        description = offer.find('p', {'class': 'offer-company'}).text.strip()
        requirements = offer.find('ul', {'class': 'offer-requirements'}).text.strip()
        location = offer.find('span', {'class': 'offer-labels__location'}).text.strip()

        job_offer = {'title': title, 'description': description, 'requirements': requirements, 'location': location}
        job_offers.append(job_offer)

    return job_offers

url = 'https://www.infopraca.pl/praca?q=programista&lc=&d=20'
job_offers = get_job_offers(url)

df = pd.DataFrame(job_offers, columns=['Tytuł', 'Opis', 'Wymagania', 'Lokalizacja'])
print(df)