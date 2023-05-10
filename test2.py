import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class JobSearchUI(QMainWindow):
    def __init__(self, job_offers):
        super().__init__()

        self.job_offers = job_offers

        self.setWindowTitle('Przegląd ofert pracy')
        self.setGeometry(200, 200, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setRowCount(len(self.job_offers))
        self.table.setColumnCount(4)
        self.layout.addWidget(self.table)

        self.table.setHorizontalHeaderLabels(['Tytuł', 'Opis', 'Wymagania', 'Lokalizacja'])

        self.fill_table()

    def fill_table(self):
        row = 0
        for offer in self.job_offers:
            title = QTableWidgetItem(offer['title'])
            title.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row, 0, title)

            description = QTableWidgetItem(offer['description'])
            self.table.setItem(row, 1, description)

            requirements = QTableWidgetItem(offer['requirements'])
            self.table.setItem(row, 2, requirements)

            location = QTableWidgetItem(offer['location'])
            self.table.setItem(row, 3, location)

            row += 1

def get_job_offers(url_list):
    job_offers = []

    for url in url_list:
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')
        job_offers_html = soup.find_all('div', {'class': 'offer-details'})

        for offer in job_offers_html:
            title = offer.find('a', {'class': 'offer-title__link'}).text.strip()
            description = offer.find('p', {'class': 'offer-company'}).text.strip()
            requirements = offer.find('ul', {'class': 'offer-requirements'}).text.strip()
            location = offer.find('span', {'class': 'offer-labels__location'}).text.strip()

            job_offer = {'title': title, 'description': description, 'requirements': requirements, 'location': location}
            job_offers.append(job_offer)

    return job_offers

if __name__ == '_main_':
    url_list = ['https://www.pracuj.pl/praca/it%20-%20programowanie%20-%20analiza',
                'https://www.infopraca.pl/praca?kw=szukana%20fraza&kt=18']
    job_offers = get_job_offers(url_list)

    app = QApplication(sys.argv)
    ui = JobSearchUI(job_offers)
    ui.show()
    sys.exit(app.exec_())