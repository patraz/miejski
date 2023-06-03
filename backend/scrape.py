from datetime import datetime
from requests_html import HTML
# from send_mail import Emailer
from requests_html import HTMLSession


# session = HTMLSession()

# scraping_site = 'https://www.miejski.pl/losuj'


# r = session.get(scraping_site)

# word = r.html.find('article')[0].find('header')[0].text
# meaning = r.html.find('article')[0].find('p')[0].text
# example = r.html.find('article')[0].find('blockquote')[0].text
# print(f"słowo:{word}", f'znaczenie:{meaning}', f'przykład{example}')


def scrape_words(times):
    session = HTMLSession()
    scraping_site = 'https://www.miejski.pl/losuj'

    for x in range(times):
        r = session.get(scraping_site)

        word = r.html.find('article')[0].find('header')[0].text
        meaning = r.html.find('article')[0].find('p')[0].text
        example = r.html.find('article')[0].find('blockquote')[0].text
        print(f"słowo: {word}", f'znaczenie: {meaning}', f'przykład {example}')

scrape_words(4)