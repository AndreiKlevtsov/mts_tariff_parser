import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

import logging

logger = logging.getLogger(__name__)


def get_source_code():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--disable-gpu')
    url = "https://moskva.mts.ru/personal/mobilnaya-svyaz/tarifi/vse-tarifi/mobile-tv-inet"
    driver = webdriver.Remote('http://selenium:4444/wd/hub',
                              options=options)
    driver.get(url)
    time.sleep(1)
    while True:
        try:
            driver.execute_script("scroll(0, 400)")
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "tariffs-more-btn"))).click()
            time.sleep(2)
            tarifff_cards = driver.find_elements(
                By.TAG_NAME,
                "mts-tariff-card"
            )
            break
        except TimeoutException as e:
            print(e)
    return tarifff_cards


def get_value_if_exists(tariff, class_name):
    try:
        return tariff.find_element(
            By.CLASS_NAME,
            class_name
        ).text
    except NoSuchElementException:
        return None


def tariff_parser(tariff_cards):
    tarifs = []
    for tariff in tariff_cards:
        res = {}
        res['badge_text'] = get_value_if_exists(
            tariff,
            'badge-text'
        )
        res['name'] = tariff.find_element(
            By.CLASS_NAME,
            'card-title'
        ).text
        res['description'] = get_value_if_exists(
            tariff,
            'card-description'
        )
        res['features'] = tariff.find_element(
            By.CLASS_NAME,
            'card-features'
        ).text
        res['benefits'] = get_value_if_exists(
            tariff,
            'card-benefits__margin'
        )
        res['main_price'] = tariff.find_element(
            By.CLASS_NAME,
            'price-main'
        ).text
        res['sale_price'] = get_value_if_exists(
            tariff,
            'price-sale'
        )
        res['price_annotation'] = get_value_if_exists(
            tariff,
            'price-annotation'
        )
        tarifs.append(res)

    return tarifs
