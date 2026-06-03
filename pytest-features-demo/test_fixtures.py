# # pytest provides a feature called fixtures which was used to set up the test envoirnments where used to manage the test dependencies effectivelly
# # this feature will allow you to reuse the setup and the teardown code it will make your code more cleaner and more modular
#
# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     yield driver
#
#     driver.quit()
# #
# # def test_youtube_launch(driver):
# #     driver.get("https://www.youtube.com/")
# #
# # def test_amazon_launch(driver):
# #     driver.get("https://www.amazon.com")
#
#
#
# import pytest
#
# @pytest.fixture
# def user_data():
#     return {
#         "email": "hari"
#     }
#
# @pytest.fixture
# def login():
#     return {
#         "email": "hari",
#         "status": "login successfully"
#     }
#
# def test_verify_user_name(user_data):
#     assert user_data["email"] == "hari"
#
# def test_verify_login(login):
#     assert login["email"] == "hari"
#
#
#



# scope -

# 1. Function Scope (Default)
#
# Runs before every test method.
#
# Real-Time Use
# Open browser for each test
# Fresh test execution
# Test isolation
import pytest

@pytest.fixture(scope="function")
def browser():

    print("\nOpening Browser")

    yield

    print("\nClosing Browser")


def test_login(browser):
    print("Login Test")


def test_logout(browser):
    print("Logout Test")

#







# 2. Class Scope
# Browser opens and closes for every test.
# Runs once for an entire class.
#
# Real-Time Use
# Login once
# Execute multiple test cases
# Logout once
import pytest

@pytest.fixture(scope="class")
def login():

    print("\nLogin to Application")

    yield

    print("\nLogout from Application")


@pytest.mark.usefixtures("login")
class TestUserManagement:

    def test_create_user(self):
        print("Create User")

    def test_update_user(self):
        print("Update User")

    def test_delete_user(self):
        print("Delete User")






# 3. Module Scope
#
# Runs once for an entire Python file.
#
# Real-Time Use
# Database Connection
# API Session
# Common Test Data
import pytest

@pytest.fixture(scope="module")
def database():

    print("\nConnecting Database")

    yield

    print("\nClosing Database")


def test_insert_user(database):
    print("Insert User")


def test_update_user(database):
    print("Update User")


def test_delete_user(database):
    print("Delete User")






# 4. Session Scope
#
# Runs once for the entire pytest execution.
#
# Real-Time Use
# Generate JWT Token
# Framework Setup
# Read Config Files
# Start Reporting
import pytest

@pytest.fixture(scope="session")
def auth_token():

    print("\nGenerating Token")

    token = "ABC123"

    yield token

    print("\nDestroying Token")


def test_user(auth_token):
    print(auth_token)


def test_product(auth_token):
    print(auth_token)


def test_order(auth_token):
    print(auth_token)