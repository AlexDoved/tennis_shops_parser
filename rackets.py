import requests

from bs4 import BeautifulSoup

from informational_messages import print_info_rackets

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/100.0.4896.143 YaBrowser/22.5.0.1792 '
                  'Yowser/2.5 Safari/537.36'
}

names_of_rackets = []
links_to_rackets = []
prices_for_rackets = []


def get_rackets_third_size_racketlon(url: str, brand: str) -> None:
    """Парсер ракеток разных фирм из магазина <Ракетлон>, размер ручки - 3."""
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('a', class_='product-title')
    prices = soup.find_all('span', class_='ty-price-num')[::2]

    for item in items:
        names_of_rackets.append(''.join(item.text.split('Теннисная ракетка ')))
        links_to_rackets.append(item.get('href'))

    for item in prices:
        prices_for_rackets.append(item.text)

    all_info = [names_of_rackets, links_to_rackets, prices_for_rackets]
    elements = list(map(list, zip(*all_info)))

    if not elements:
        raise ValueError(
            f'Ссылка {brand} не корректна, что-то поменялось на сайте!')

    print_info_rackets(brand)

    for name, link, price in elements:
        print('Название ракетки: ', name)
        print('Ссылка: ', link)
        print('Цена: ', price, 'руб.')
        print()
