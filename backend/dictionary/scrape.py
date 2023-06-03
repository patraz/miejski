
from requests_html import HTMLSession


# fuction that outputs list of dictionaries with word, meanin and example

def scrape_words(times):
    session = HTMLSession()
    scraping_site = 'https://www.miejski.pl/losuj'
    list = []
    for x in range(times):
        r = session.get(scraping_site)
        word = r.html.find('article')[0].find('header')[0].text
        meaning = r.html.find('article')[0].find('p')[0].text
        example = r.html.find('article')[0].find('blockquote')[0].text

        dict = {
            'word': word,
            'meaning' : meaning,
            'example' : example
        }
        list.append(dict)
    return(list)
