import time
import random
from base.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
import logging


class VideoHomePage(BasePage):
    search_box_loc = (By.XPATH, "//*[@title='Google Search']")
    search_button_loc = (By.NAME, "btnG")
    first_video_loc = (By.ID, "vidthumb%s" % random.randint(1, 2))
    skip_ad_loc = (By.XPATH, "//*[contains(text(),'Skip Ad')]")

    @allure.step('打开google视频页面')
    def open_homepage(self):
        self.driver.get('https://www.google.com/videohp')

    @allure.step('输入内容进行搜索')
    def search(self, search_char, period):
        search_box = self.find_element(*self.search_box_loc)
        search_box.send_keys('%s definition youtube' % search_char)
        search_box.submit()
        search_button = self.find_element(*self.search_button_loc)
        search_button.click()
        time.sleep(period)

    @allure.step('随机选择播放视频')
    def play(self, period):
        play_button = self.find_element(*self.first_video_loc)
        play_button.click()
        self.skip_ad()
        time.sleep(period)

    def skip_ad(self):
        # 等待n秒如果发现广告可以允许跳过则跳过
        pre_ad_time = 10
        try:
            time.sleep(pre_ad_time)
            self.find_element(*self.skip_ad_loc).click()
        except Exception as e:
            logging.info('没发现跳过广告按钮. %s' % e)