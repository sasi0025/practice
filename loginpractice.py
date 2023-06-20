import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
class Test_practice:
    driver = webdriver.Chrome()
    def test_register_user(self):
        self.driver.get("https://automationexercise.com/")
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"(//div//li)[4]").click()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Name']").send_keys("sasi")
        self.driver.find_element(By.XPATH,"(//input[@placeholder='Email Address'])[2]").send_keys("sasij77@gmail.com")
        self.driver.find_element(By.XPATH,"(//button[@type='submit'])[2]").click()
        self.driver.find_element(By.XPATH,"//input[@id='id_gender1']").click()
        self.driver.find_element(By.ID,"password").send_keys("sasi12345")
        days=Select(self.driver.find_element(By.ID,"days"))
        days.select_by_value("25")
        months=Select(self.driver.find_element(By.ID,"months"))
        months.select_by_value("3")
        year=Select(self.driver.find_element(By.ID,"years"))
        year.select_by_value("2000")
        self.driver.execute_script("window.scrollTo(0,200)")
        self.driver.find_element(By.ID,"newsletter").click()
        self.driver.find_element(By.XPATH,"//input[@id='optin']").click()
        self.driver.find_element(By.ID,"first_name").send_keys("sasi")
        self.driver.find_element(By.ID,"last_name").send_keys("j")
        self.driver.find_element(By.ID,"company").send_keys("sasi_techi")
        self.driver.find_element(By.ID,"address1").send_keys("smoor building")
        self.driver.find_element(By.ID, "address2").send_keys("jayanagar, bangloore")
        country=Select(self.driver.find_element(By.XPATH,"//select[@id='country']"))
        country.select_by_value("India")
        self.driver.find_element(By.ID,"state").send_keys("karanataka")
        self.driver.find_element(By.ID,"city").send_keys("bangloore")
        self.driver.find_element(By.ID,"zipcode").send_keys("560001")
        self.driver.find_element(By.ID,"mobile_number").send_keys("8990903234")
        self.driver.execute_script("window.scrollTo(0,1200)")
        self.driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Delete Account']").click()
















