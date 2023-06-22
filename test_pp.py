from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_pp:
    driver=webdriver.Chrome()
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")

    def test_drag_and_drop(self):
        option_A=self.driver.find_element(By.ID,"column-a")
        option_b=self.driver.find_element(By.ID,"column-b")
        action= ActionChains(self.driver)
        action.drag_and_drop(option_A, option_b)
        action.drag_and_drop(option_b,option_A)


