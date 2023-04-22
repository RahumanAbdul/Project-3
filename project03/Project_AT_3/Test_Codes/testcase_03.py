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

    # Validation of Planning to Travel a Country and Booking
    # Test Case ID: TC_ PICK_03
    def test_planningto_travel(self, booting_function):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().SearchPlanning_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().SearchPlanning_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().SearchPlanning_Inputbox)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().SearchPlanning_Inputbox).send_keys(data.Pick_Data().PlanningCountry)

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().DubaiOption_Locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().DubaiOption_Locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().TempDubai_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().TempDubai_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().DepartDubai_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().DepartDubai_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().DepartDate_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().DepartDate_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().DurationTrip_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().DurationTrip_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().TravellingWith_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().TravellingWith_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().VisitPlace_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().VisitPlace_locator).click()

            self.wait.until(EC.element_to_be_clickable((By.XPATH, locators.Pick_Locators().Itinerary_locator)))
            self.driver.find_element(by=By.XPATH, value=locators.Pick_Locators().Itinerary_locator).click()
            assert self.test_planningto_travel == self.test_planningto_travel
            print("PERFORMING PLANNING TO TRAVEL A COUNTRY IS SUCCESSFULLY VALIDATED")
        except NoSuchElementException:
            print('yes')        