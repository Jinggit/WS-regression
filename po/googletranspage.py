import time
from base.base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class TranHomePage(BasePage):
    search_box_loc = (By.ID, "source")
    listen_button_loc = (By.XPATH, "//*[@class='src-tts left-positioned ttsbutton jfk-button-flat source-or-target-footer-button jfk-button']")
    listen_tran_button_loc = (By.XPATH, "//*[@class ='res-tts ttsbutton-res left-positioned ttsbutton jfk-button-flat source-or-target-footer-button jfk-button']")
    syn_word_loc = (By.XPATH, "(//*[@class ='gt-syn-span']/span)[1]")

    @allure.step('打开google翻译页面')
    def open_homepage(self):
        self.driver.get('https://translate.google.ca/#view=home&op=translate&sl=auto&tl=zh-CN')

    @allure.step('输入内容进行搜索')
    def search(self, search_char, period=1):
        search_box = self.find_element(*self.search_box_loc)
        search_box.clear()
        search_box.send_keys(search_char)
        time.sleep(period)


    @allure.step('发音n次')
    def listen(self, count=3):
        listen_button = self.find_element(*self.listen_button_loc)
        for i in range(count):
            listen_button.click()
            time.sleep(3)

    @allure.step('读出中文翻译')
    def listen_tran(self, count=1):
        listen_button = self.find_element(*self.listen_tran_button_loc)
        for i in range(count):
            listen_button.click()
            time.sleep(3)

    @allure.step('得到同义词')
    def get_syn_word(self):
        syn_word = self.find_element(*self.syn_word_loc).text
        return syn_word

    @allure.step('读出同义词')
    def read_syn_word(self, search_char):
        self.search(search_char)
        self.listen()