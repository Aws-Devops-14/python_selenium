from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class TransferPage(BasePage):

    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT = (By.ID, "amount")
    TRANSFER_BTN = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_TEXT = (By.XPATH, "//h1[contains(text(),'Transfer Complete')]")

    def transfer_funds(self, amount):
        self.click(self.TRANSFER_LINK)
        self.send_keys(self.AMOUNT, amount)
        self.click(self.TRANSFER_BTN)
        return self.get_text(self.SUCCESS_TEXT)
