import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.URL_ENDPOINT = "accounts/login/"

        self.LOGIN_FORM_LOCATOR = ("css selector", "#login_form")
        self.REGISTER_FORM_LOCATOR = ("css selector", "#register_form")

    @allure.step("Assert Login page url")
    def should_be_login_url(self):
        assert self.BROWSER.current_url.endswith(self.URL_ENDPOINT), (
            f'Page url should end with "{self.URL_ENDPOINT}", '
            f'but actual url is "{self.BROWSER.current_url}"'
        )

    @allure.step("Assert page contains login form")
    def should_be_login_form(self):
        assert self.is_element_present(
            *self.LOGIN_FORM_LOCATOR
        ), "Login form is missing"

    @allure.step("Assert page contains register form")
    def should_be_register_form(self):
        assert self.is_element_present(
            *self.REGISTER_FORM_LOCATOR
        ), "Register form is missing"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
