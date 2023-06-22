
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from practice.automationexercice.base import Base
from practice.automationexercice.excel_data import TestData


class TestTC(Base):

    @pytest.fixture
    def getdata(self):
        return TestData.getTestData()

    @pytest.mark.parametrize('test_case', TestData.getTestData())
    def test_login(self, getdata, test_case):
        log = self.getLogger()
        self.driver.get("http://qa-giverly-admin.neokredx.com:9080/login")
        username_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Email']")
        password_input = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']")
        login_button = self.driver.find_element(By.XPATH, "//button[@data-testid='button']")
        otp_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        log.info(f"Entering Username: {test_case['username']}")
        username_input.send_keys(test_case['username'])
        log.info(f"Entering password: {test_case['password']}")
        password_input.send_keys(test_case['password'])
        login_button.click()
        otp_input.send_keys(test_case['otp'])
        login_button.click()

        self.driver.quit()

