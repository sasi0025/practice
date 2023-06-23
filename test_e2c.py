import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_e2c():

    def __init__(self):
        self.driver = webdriver.Chrome()

    def setup(self):
        self.driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

    def test_search_product(self, email_sender):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
        vegitables = self.driver.find_elements(By.XPATH, "//div[@class='product']")
        for vegi in vegitables:
            veginame = vegi.find_element(By.XPATH, "h4").text
            if veginame == "Cucumber - 1 Kg":
                vegi.find_element(By.XPATH, "//div[@class='product']/div/button").click()

        self.driver.find_element(By.XPATH, "//a[@class='cart-icon']").click()
        self.driver.find_element(By.XPATH, "(//button[@type='button'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoBtn")))
        self.driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
        time.sleep(2)
        promo = self.driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
        assert promo == "Code applied ..!"
        totalamount = float(self.driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
        percentage = str(self.driver.find_element(By.CSS_SELECTOR, ".discountPerc").text)
        dicountamount = float(self.driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
        if totalamount > dicountamount:
            print(f"Discount applied: {percentage}%")
        else:
            print("there is no discount")

        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button)[2]")))
        button.click()
        drop = Select(self.driver.find_element(By.TAG_NAME, "select"))
        drop.select_by_value("India")
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//button").click()
        email_sender.send_email("test_search_product","passed")



    def teardown(self):
        self.driver.close()

