import sys
sys.path.append("..")
import pytest
import allure
from base.browser import Browser
from po.googletranspage import TranHomePage
from po.googleimagepage import ImageHomePage
from po.googlevideopage import VideoHomePage
from po.enlargepage import EnlargeHomePage
from data.words import *


@allure.feature("单词学习")
class TestWordLearn:
    @classmethod
    def setup_class(cls):
        browse = Browser(cls)
        cls.driver = browse.get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.story("搜索单词解释并发音,放大拼写,翻译,例句,查找单词图片,查找单词视频")
    @pytest.mark.parametrize("search_char, meaning, example", wordlist_RE2_Unit7)
    def test_words_search(self, search_char, meaning, example):
        READ = 3
        LOOK = 3
        WATCH = 20

        #放大拼写
        enlargepage = EnlargeHomePage(self.driver)
        enlargepage.open_homepage()
        enlargepage.search(search_char, LOOK)
        #搜索单词解释并发音
        googletranspage = TranHomePage(self.driver)
        googletranspage.open_homepage()
        googletranspage.search(search_char, READ)
        googletranspage.listen()
        googletranspage.listen_tran(1)
        #翻译
        googletranspage.search(meaning, READ)
        googletranspage.listen(period=READ)
        #例句
        # googletranspage.search(example, READ)
        # googletranspage.listen(period=READ)
        #同义词
        #syn_word = googletranspage.get_syn_word()
        #googletranspage.read_syn_word(syn_word)
        #放大拼写
        # enlargepage = EnlargeHomePage(self.driver)
        # enlargepage.open_homepage()
        # enlargepage.search(search_char, LOOK)
        #查找单词图片
        googleimagepage = ImageHomePage(self.driver)
        googleimagepage.open_homepage()
        googleimagepage.search(search_char, LOOK)
        googleimagepage.clickfirstimage(READ)
        #搜索结果截图
        googleimagepage.screenshot(search_char)
        #查找单词视频
        # googlevideopage = VideoHomePage(self.driver)
        # googlevideopage.open_homepage()
        # googlevideopage.search(search_char, LOOK)
        # googlevideopage.play(WATCH)


if __name__ == '__main__':
    pytest.main()