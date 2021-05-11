from xml.dom.minidom import Element
from xml.etree import ElementTree

import pytest
import requests
import requests_mock

from homework10.course import (
    GET_CURRENCY_URL,
    Currency,
    IncorrectNameError,
    extract_currency,
    get_currency_block,
    reformat_coma_to_dot,
)

MOCK_RESPONSE = """
<ValCurs Date="21.04.2021" name="Foreign Currency Market">
    <Valute ID="R01235">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>Доллар США</Name>
        <Value>76,0155</Value>
    </Valute>
</ValCurs>
"""


def get_text(mock_response=MOCK_RESPONSE) -> str:
    adapter = requests_mock.Adapter()
    adapter.register_uri("GET", GET_CURRENCY_URL, text=mock_response)
    session = requests.Session()

    return session.get(GET_CURRENCY_URL).text


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


def test_get_course():
    assert isinstance(get_course(), float)


def test_get_course_incorrect_name_error():
    with pytest.raises(IncorrectNameError):
        get_course("foo")


def test_get_course_value_error():
    def parse_xml() -> Element:
        text: str = get_text("")
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

    with pytest.raises(ValueError):
        get_course("foo")


@pytest.mark.parametrize(["input_string", "expected_result"], [("", ""), (",", "."), ("2", "2"), ("2,375", "2.375")])
def test_reformat_coma_to_dot(input_string: str, expected_result: str):
    string = ","
    assert reformat_coma_to_dot(string) == "."
