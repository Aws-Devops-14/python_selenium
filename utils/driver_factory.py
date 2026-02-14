from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome", headless=False):

        if browser.lower() == "chrome":
            options = Options()

            if headless:
                options.add_argument("--headless")
                options.add_argument("--disable-gpu")

            options.add_argument("--start-maximized")

            driver = webdriver.Chrome(options=options)
            return driver

        else:
            raise Exception(f"Browser '{browser}' not supported yet")
