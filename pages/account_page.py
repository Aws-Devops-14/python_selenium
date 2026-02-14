from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountsPage(BasePage):

    ACCOUNTS_OVERVIEW = (By.LINK_TEXT, "Accounts Overview")
    TRANSACTION_TABLE = (By.ID, "transactionTable")

    def verify_transaction(self, account_number):
        self.click(self.ACCOUNTS_OVERVIEW)
        self.click((By.LINK_TEXT, account_number))
        transaction_text = self.get_text(self.TRANSACTION_TABLE)
        return "Debit" in transaction_text or "Credit" in transaction_text
