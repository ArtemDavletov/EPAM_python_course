from enum import Enum
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

import requests

GET_CURRENCY_URL = "http://www.cbr.ru/scripts/XML_daily.asp"

# I also can write "http://www.cbr.ru/scripts/XML_daily.asp?VAL_NM_RQ=R01235",
# but it isn't supported, although it is supported for currency dynamic


__all__ = ("get_course",)


class Currency(Enum):
    USD = "R01235"


class IncorrectNameError(ValueError):
    ...


def reformat_coma_to_dot(text: str) -> str:
    return text.replace(",", ".")


def get_text() -> str:
    return requests.get(GET_CURRENCY_URL).text


def get_currency_block(root: Element, currency: str) -> Element:
    try:
        return list(filter(lambda x: x.attrib["ID"] == currency, root))[0]
    except KeyError as keyError:
        raise ValueError("API was changed, check http://www.cbr.ru/development/sxml/") from keyError
    except IndexError as indexError:
        raise IncorrectNameError("Incorrect currency name") from indexError


def extract_currency(currency_block: Element) -> float:
    for sub_block in currency_block:
        if sub_block.tag == "Value":
            return float(reformat_coma_to_dot(sub_block.text))
    raise ValueError("API was changed, check http://www.cbr.ru/development/sxml/")


def parse_xml() -> Element:
    text: str = get_text()
    root: Element = ElementTree.fromstring(text)
    return root


def get_course(currency: str = Currency.USD.value) -> float:
    """
    :param currency: currency ID, by default ID for USD,
    ID's are available to see here: http://www.cbr.ru/scripts/XML_val.asp
    :return: price against the ruble
    """
    root = parse_xml()

    currency_block = get_currency_block(root, currency=currency)
    currency = extract_currency(currency_block)

    return currency
