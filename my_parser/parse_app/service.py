import requests
from bs4 import BeautifulSoup
from .models import News, Tag


def fetch(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        raise e


def parser(html, site_tag):
    final_data = []
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_="news-list__group")("div", class_='news-list__item')
    for el in data[:10]:
        url = f'https://market.yandex.ru{el.find("a").get("href")}'
        title = el.find("a").text
        description = el.find('div', class_='news-list__item-description').find('p').text
        public_date = el.find('time').get('datetime')
        human_public_date = el.find('time').text
        tag = site_tag
        item = {
            'url': url,
            'title': title,
            'text': description,
            'public_date': public_date,
            'human_public_date': human_public_date,
            'tag': tag
        }
        final_data.append(item)
    return final_data


def add_to_db(last_news):
    data = News.objects.all()
    urls = [news.url for news in data]
    for item in last_news:
        if item['url'] not in urls:
            news = News.objects.create(title=item['title'], url=item['url'], public_date=item['public_date'])
            news.tag.set(Tag.objects.filter(title=item['tag']))


def yandex_parse():
    yandex_url = 'https://market.yandex.ru/partners/news'
    site_tag = 'Яндекс'
    html = fetch(yandex_url)
    last_news = parser(html, site_tag)
    add_to_db(last_news)
    return last_news
