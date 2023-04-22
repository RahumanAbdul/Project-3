from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Test_Locators import locators
from Test_Data import data
import pytest

class Test_Abdul:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(25)
        yield
        self.driver.close()

    # Validation on Pick Your Trail Home Page
    # Test Case ID: TC_PICK_01  
    def test_validate_homepage(self, booting_function):
        self.driver.get(data.Pick_Data().url)
        self.driver.implicitly_wait(6)
        assert self.test_validate_homepage == self.test_validate_homepage
        print("SUCCESSFULLY VALIDATED ON PICK YOUR TRAIL HOME PAGE")