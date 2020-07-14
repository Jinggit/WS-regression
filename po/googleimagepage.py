import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from allure_commons.types import AttachmentType
from PIL import Image

class ImageHomePage(BasePage):
    search_box_loc = (By.NAME, "q")
    search_button_loc = (By.XPATH, "//*[@aria-label='Google Search']")
    result_image = (By.ID, "islmp")

    @allure.step('打开google图片查询页面')
    def open_homepage(self):
        self.driver.get('https://www.google.ca/imghp?hl=en&tab=wi&ogbl')

    @allure.step('输入内容进行搜索')
    def search(self, search_char, period):
        search_box = self.find_element(*self.search_box_loc)
        search_box.send_keys(search_char)
        search_button = self.find_element(*self.search_button_loc)
        search_button.click()
        time.sleep(period)
        image = self.find_element(*self.result_image).screenshot_as_png
        allure.attach(image, name="单词 %s 截图" % search_char, attachment_type=AttachmentType.PNG)