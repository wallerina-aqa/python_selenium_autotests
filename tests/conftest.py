import pytest
from selenium import webdriver

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage


def pytest_addoption(parser):
    # fmt: off
    parser.addoption("--language", action="store", default="en",
        help="Choose language: ",
        choices=("ar", "ca", "cs", "da", "de", "en", "el",
                 "es", "fi", "fr", "it", "ko", "nl", "pl",
                 "pt", "pt-br", "ro", "ru", "sk", "uk", "zh-hans")

    )
    # fmt: on


@pytest.fixture()
def browser(request):
    print("\nStart browser for test")

    driver_options = webdriver.ChromeOptions()
    user_language = request.config.getoption("--language")
    driver_options.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )

    driver = webdriver.Chrome(options=driver_options)
    yield driver

    print("\nQuit browser")
    driver.quit()


@pytest.fixture()
def main_page(browser):
    return MainPage(browser)


@pytest.fixture()
def login_page(browser):
    return LoginPage(browser)


@pytest.fixture()
def product_page(browser):
    return ProductPage(browser)


@pytest.fixture()
def basket_page(browser):
    return BasketPage(browser)
