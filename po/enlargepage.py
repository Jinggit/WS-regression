import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class EnlargeHomePage(BasePage):
    text = (By.XPATH, "//*[@class ='text']")
    search_box_loc = (By.XPATH, "//*[@class='inputbox']")


    @allure.step('打开放大字体页面')
    def open_homepage(self):
        self.driver.get('https://large-type.com/')

    @allure.step('输入内容进行搜索')
    def search(self, search_char, period):
        search_box = self.find_element(*self.search_box_loc)
        search_box.send_keys(search_char)
        time.sleep(period)