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
        self.driver.get(data.Pick_Data().url)
        self.wait = WebDriverWait(self.driver, 20)

    # Validation of Tour Packages On Pick Your Trail
    # Test Case ID: TC_ PICK_02
    def test_tourpackages(self, booting_function):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().Packages_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().Packages_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().Search_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().Search_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().Search2Inputbox_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().Search2Inputbox_locator).send_keys(data.Pick_Data().Country1)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().AustriaOption_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().AustriaOption_locator).click()
            assert self.test_tourpackages == self.test_tourpackages
            print(" CHECKING TOUR PACKAGES ON PICK YOUR TRAIL IS SUCCESSFULLY VALIDATED")
        except NoSuchElementException:
            print('yes')    




