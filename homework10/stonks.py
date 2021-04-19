from collections import Iterator
from typing import List

import requests
from bs4 import BeautifulSoup

from homework10.course import get_course

S_AND_P_500_URL: str = "https://markets.businessinsider.com/index/components/s&p_500"
ACTUAL_USD_COURSE: float = get_course()


# Have to modify from requests to aiohttp!!!!!


def get_price_in_rubles(price: float):
    return int(price * ACTUAL_USD_COURSE * 100) / 100


class Company:
    code: str
    name: str
    price: float
    pe: str
    growth: str
    potential_profit: str

    def __init__(self, code, name, price, pe, growth, potential_profit):
        self.code = code
        self.name = name
        self.price = price
        self.pe = pe
        self.growth = growth
        self.potential_profit = potential_profit

    def __str__(self):
        return str(self.to_dict())

    def __repr__(self):
        return str(self.to_dict())

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "price": self.price,
            "P/E": self.pe,
            "growth": self.growth,
            "potential profit": self.potential_profit,
        }

    @staticmethod
    def from_html_tr_block(html_tr_block) -> "Company":
        tds_list = html_tr_block.find_all("td")
        try:
            return Company(
                code="???",
                name=tds_list[0].find("a").contens,
                price=get_price_in_rubles(float(tds_list[1].contents[0].strip().replace(",", ""))),
                pe="???",
                growth="???",
                potential_profit="???",
            )
        except TypeError as typeError:
            raise ValueError(f"Hypertext markup was changed, check {S_AND_P_500_URL}") from typeError


def get_n_sandp_page(n: int):
    return S_AND_P_500_URL + f"?p={n}"


def get_pages_gen() -> Iterator:
    yield from (get_n_sandp_page(i) for i in range(1, 11))


def request_to_page(page: str) -> str:
    return requests.get(page).text


def get_all_stocks_from_page(soup):
    return soup.find("table", {"class": "table table-small"}).find_all("tr")


# soup.find("table",{"class":"table table-small"}).find_all("tr")[1].find_all("td")


def bs_parser():
    companies: List[Company] = []

    for page in get_pages_gen():
        html = request_to_page(page)
        soup = BeautifulSoup(html, "html.parser")

        stocks_per_page = get_all_stocks_from_page(soup)
        companies += list(map(Company.from_html_tr_block, stocks_per_page[1:]))
    return companies


companies = bs_parser()
print(companies, len(companies))
