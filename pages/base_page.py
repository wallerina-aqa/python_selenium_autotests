import allure
from selenium.common import NoSuchElementException

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.BROWSER = browser
        self.BASE_URL = "https://selenium1py.pythonanywhere.com/"
        self.WAIT = WebDriverWait(self.BROWSER, timeout=5)
        self.EC = ec

        self.LOGIN_LINK_LOCATOR = ("css selector", "#login_link")

    def open(self, url):
        self.BROWSER.get(url)

    def find_element(self, how, what):
        return self.BROWSER.find_element(how, what)

    @property
    def login_link(self):
        return self.find_element(*self.LOGIN_LINK_LOCATOR)

    def is_element_present(self, how, what):
        try:
            self.WAIT.until(self.EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    @allure.step("Assert page contains link to Login page")
    def should_be_login_link(self):
        assert self.is_element_present(
            *self.LOGIN_LINK_LOCATOR
        ), "Login link is not displayed, but should be"

    @allure.step("Assert page contains link to Login page")
    def should_be_login_link(self):
        assert (
            self.login_link.is_displayed()
        ), "Login link is not displayed, but should be"
        assert self.login_link.is_enabled(), "Login link is not enabled, but should be"

    @allure.step("Click login link")
    def click_login_link(self):
        self.login_link.click()
