from logging import getLogger

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from dump.utilities.baseclass import BaseClass


class Test_001:
    driver=webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")


    def test_radio(self):
        self.driver.find_element(By.CSS_SELECTOR,".radioButton")
        radiobuttons=self.driver.find_elements(By.XPATH,"//input[@type='radio']")
        for i in radiobuttons:
            if i.get_attribute("value")=="radio3":
                i.click()


    def test_autosugestion(self):
        self.driver.find_element(By.XPATH,"//input[@placeholder='Type to Select Countries']").send_keys("Ind")
        countrys=self.driver.find_elements(By.XPATH,"//div[@class='ui-menu-item-wrapper']")
        for country in countrys:
            if country.get_attribute("value")=="INDIA":
                country.click()
            country.is_selected()
    def test_select_dropdown(self):

        radio = Select(self.driver.find_element(By.ID, "dropdown-class-example"))
        radio.select_by_value("option2")

    def test_checkbox(self):
        checkbox=self.driver.find_elements(By.XPATH,"//input[@type='checkbox']")
        for check in checkbox:
            if check.get_attribute("value")=="option3":
                check.click()


    def test_switch_window(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID,"openwindow").click()
        windowsOpened = self.driver.window_handles
        self.driver.switch_to.window(windowsOpened[0])
        self.driver.current_url
        self.driver.switch_to.default_content()

    def test_switch_tab(self):
        self.driver.find_element(By.ID,"opentab").click()
        frame=self.driver.window_handles
        self.driver.switch_to.window(frame[0])
    def test_alret_pop(self):

        self.driver.find_element(By.NAME,"enter-name").send_keys("sasi")
        self.driver.find_element(By.ID,"alertbtn").click()
        alert=self.driver.switch_to.alert
        alert_text=alert.text
        assert "sasi" in alert_text
        alert.accept()
        self.driver.find_element(By.ID,"confirmbtn").click()
        alert.dismiss()
    def test_moucee_action(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.ID, "mousehover")).perform()
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, "Reload")).click().perform()



    def test_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element(By.ID,"courses-iframe"))
        element=self.driver.find_element(By.LINK_TEXT,"Practice").text
        assert "Practice"==element
        print(element)

    def test_sliders(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.get_screenshot_as_file("start.png")
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        self.driver.get_screenshot_as_file("end.png")












