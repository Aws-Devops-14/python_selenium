from behave import *
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.open_account_page import OpenAccountPage
from pages.transfer_page import TransferPage
from pages.account_page import AccountsPage
from selenium.webdriver.common.by import By
import random
import string

def generate_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=5))

@given("user launches the application")
def step_launch(context):
    context.driver.get("https://parabank.parasoft.com/parabank/index.htm")

@when("user registers a new account")
def step_register(context):
    register_page = RegisterPage(context.driver)

    username, password = register_page.register()

    context.username = username
    context.password = password

    # logout after registration
    context.driver.find_element(By.LINK_TEXT, "Log Out").click()


@when("user logs in")
def step_login(context):
    LoginPage(context.driver).login(context.username, context.password)

@when("user opens a new account")
def step_open_account(context):
    context.account_number = OpenAccountPage(context.driver).open_account()

@when("user transfers funds")
def step_transfer(context):
    TransferPage(context.driver).transfer_funds("100")

@then("transaction should be successful")
def step_verify(context):
    result = AccountsPage(context.driver).verify_transaction(context.account_number)
    assert result

@then("user logs out")
def step_logout(context):
    LoginPage(context.driver).logout()
