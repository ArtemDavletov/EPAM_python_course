import asyncio
import json
import time
from typing import AsyncIterator, List

import aiohttp as aiohttp
import requests
from aiohttp import ClientSession
from bs4 import BeautifulSoup

from homework10.course import get_course

BUSINESS_INSIDER_URL = "https://markets.businessinsider.com/"
S_AND_P_500_URL: str = BUSINESS_INSIDER_URL + "index/components/s&p_500"
ACTUAL_USD_COURSE: float = get_course()


def get_price_in_rubles(price: float):
    return int(price * ACTUAL_USD_COURSE * 100) / 100


class Company:
    code: str
    name: str
    price: float
    pe: float
    growth: float
    potential_profit: float

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
    async def from_html_tr_block(html_tr_block) -> "Company":
        tds_list = html_tr_block.find_all("td")
        try:
            code, pe, potential_profit = await parse_company_page(tds_list[0].a.attrs["href"])

            return Company(
                code=code,
                name=tds_list[0].a.contents[0],
                price=get_price_in_rubles(float(tds_list[1].contents[0].strip().replace(",", ""))),
                pe=pe,
                growth=float(tds_list[-2].find_all("span")[-1].contents[0].strip("%")),
                potential_profit=potential_profit,
            )
        except TypeError as typeError:
            raise ValueError(f"Hypertext markup was changed, check {S_AND_P_500_URL}") from typeError


def get_n_sandp_page(n: int):
    return S_AND_P_500_URL + f"?p={n}"


async def get_pages_gen() -> AsyncIterator:
    for i in range(1, 11):
        yield get_n_sandp_page(i)


def request_to_page(page: str) -> str:
    return requests.get(page).text


async def fetch(client: ClientSession, page: str):
    async with client.get(page, verify_ssl=False) as resp:
        return await resp.text()


def get_all_stocks_from_page(soup):
    return soup.find("table", {"class": "table table-small"}).find_all("tr")


# <span data-v-0ae43770="">, MMM</span>
# soup.find("table",{"class":"table table-small"}).find_all("tr")[1].find_all("td")


async def parse_company_page(href):
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, BUSINESS_INSIDER_URL + href)
    soup = BeautifulSoup(html, "html.parser")

    code = soup.find("span", {"class": "price-section__category"}).span.contents[0].strip(", ")
    pe = soup.find("div", {"class": "snapshot__data-item"}).contents[0].strip().replace(",", "")

    low_cost = (
        soup.find("div", {"class": "snapshot__data-item snapshot__data-item--small"})
        .contents[0]
        .strip()
        .replace(",", "")
    )
    high_cost = (
        soup.find("div", {"class": "snapshot__data-item snapshot__data-item--small snapshot__data-item--right"})
        .contents[0]
        .strip()
        .replace(",", "")
    )
    potential_profit = round(float(high_cost) - float(low_cost), 2)

    return code, float(pe), potential_profit


async def sandp_parser():
    companies: List[Company] = []

    async for page in get_pages_gen():
        async with aiohttp.ClientSession() as client:
            html = await fetch(client, page)
        soup = BeautifulSoup(html, "html.parser")

        stocks_per_page = get_all_stocks_from_page(soup)

        for i in stocks_per_page[1:]:
            company = await Company.from_html_tr_block(i)
            companies.append(company)
    return companies


async def solution():
    companies = await sandp_parser()

    with open("data/task1.json", "w") as file:
        json.dump(list(sorted(map(lambda x: x.to_dict(), companies), key=lambda x: x["price"]))[-10:], file)

    with open("data/task2.json", "w") as file:
        json.dump(list(sorted(map(lambda x: x.to_dict(), companies), key=lambda x: x["P/E"]))[:10], file)

    with open("data/task3.json", "w") as file:
        json.dump(list(sorted(map(lambda x: x.to_dict(), companies), key=lambda x: x["growth"]))[-10:], file)

    with open("data/task4.json", "w") as file:
        json.dump(list(sorted(map(lambda x: x.to_dict(), companies), key=lambda x: x["potential profit"]))[-10:], file)


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(solution())
    print(time.time() - start_time)
