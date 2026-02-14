from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import string


class RegisterPage(BasePage):

    REGISTER_LINK = (By.LINK_TEXT, "Register")
    FIRST_NAME = (By.ID, "customer.firstName")
    LAST_NAME = (By.ID, "customer.lastName")
    ADDRESS = (By.ID, "customer.address.street")
    CITY = (By.ID, "customer.address.city")
    STATE = (By.ID, "customer.address.state")
    ZIP = (By.ID, "customer.address.zipCode")
    PHONE = (By.ID, "customer.phoneNumber")
    SSN = (By.ID, "customer.ssn")
    USERNAME = (By.ID, "customer.username")
    PASSWORD = (By.ID, "customer.password")
    CONFIRM_PASSWORD = (By.ID, "repeatedPassword")
    REGISTER_BTN = (By.XPATH, "//input[@value='Register']")

    def generate_username(self):
        return "user_" + ''.join(random.choices(string.ascii_lowercase, k=5))

    # 🔥 THIS METHOD WAS MISSING
    def register(self):
        self.click(self.REGISTER_LINK)

        username = self.generate_username()
        password = "Test@123"

        self.send_keys(self.FIRST_NAME, "Usha")
        self.send_keys(self.LAST_NAME, "Rani")
        self.send_keys(self.ADDRESS, "Hyderabad")
        self.send_keys(self.CITY, "Hyderabad")
        self.send_keys(self.STATE, "TS")
        self.send_keys(self.ZIP, "500001")
        self.send_keys(self.PHONE, "9999999999")
        self.send_keys(self.SSN, "123456")
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.send_keys(self.CONFIRM_PASSWORD, password)

        self.click(self.REGISTER_BTN)

        return username, password
