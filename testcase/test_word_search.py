import sys
sys.path.append("..")
import pytest
import allure
from base.browser import Browser
from po.googletranspage import TranHomePage
from po.googleimagepage import ImageHomePage
from po.googlevideopage import VideoHomePage
from po.enlargepage import EnlargeHomePage

@allure.feature("单词学习")
class TestWordLearn:
    @classmethod
    def setup_class(cls):
        browse = Browser(cls)
        cls.driver = browse.get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    wordlist = ['climate', 'complete', 'fairly', 'giant', 'heavy', 'hunter', 'in reality', 'museum', 'physical',
     'relative', 'appearance', 'dig up', 'estimate', 'examine', 'extend', 'length', 'mystery',
     'opinion', 'seek', 'terrible', 'although', 'appropriate', 'collect', 'magical', 'memorize', 'primarily',
     'publish', 'reflect', 'scary', 'text', 'accidental', 'affect', 'deep',
     'determined', 'hide', 'immediate', 'recognize','shock', 'sudden', 'youth', 'illegal', 'law',
     'locate', 'preserve', 'valuable', 'rare', 'weigh', 'treasure', 'collector', 'in demand destroy',
     'middle', 'race', 'equipment', 'limit', 'majority', 'height', 'employed', 'capable', 'occupation',
     'accomplish', 'construction', 'network', 'currency', 'protect', 'expose', 'technique', 'reveal', 'apply',
     'vivid', 'timeless', 'confirm', 'ordinary', 'according to','involve', 'task', 'role', 'block', 'compete',
     'proud', 'average', 'freedom', 'equality', 'divide', 'income', 'steal', 'purchase', 'bury', 'factor', 'disease',
     'pretend', 'sail', 'shoot', 'avoid', 'terrorize', 'transfer', 'fearless', 'target', 'fail', 'respect', 'approach',
     'bright', 'shine', 'response', 'effort', 'flight', 'headed', 'crash', 'investigate', 'disappearance']

    wordlist1 = ['climate', 'complete', 'fairly', 'giant', 'heavy', 'hunter', 'in reality', 'museum', 'physical',
     'relative', 'appearance', 'dig up', 'estimate', 'examine', 'extend', 'length', 'mystery',
     'opinion', 'seek', 'terrible', 'although', 'appropriate', 'collect', 'magical', 'memorize', 'primarily',
     'publish', 'reflect', 'scary', 'text', 'accidental', 'affect', 'deep',
     'determined', 'hide', 'immediate', 'recognize']

    wordlist2 = ['shock', 'sudden', 'youth', 'illegal', 'law',
     'locate', 'preserve', 'valuable', 'rare', 'weigh', 'treasure', 'collector', 'in demand destroy',
     'middle', 'race', 'equipment', 'limit', 'majority', 'height', 'employed', 'capable', 'occupation',
     'accomplish', 'construction', 'network', 'currency', 'protect', 'expose', 'technique', 'reveal', 'apply',
     'vivid', 'timeless', 'confirm', 'ordinary', 'according to']

    wordlist3 = ['involve', 'task', 'role', 'block', 'compete',
     'proud', 'average', 'freedom', 'equality', 'divide', 'income', 'steal', 'purchase', 'bury', 'factor', 'disease',
     'pretend', 'sail', 'shoot', 'avoid', 'terrorize', 'transfer', 'fearless', 'target', 'fail', 'respect', 'approach',
     'bright', 'shine', 'response', 'effort', 'flight', 'headed', 'crash', 'investigate', 'disappearance']

    wordlist4 = ['fairly', 'in reality', 'physical', 'relative', 'extend', 'although', 'memorize', 'primarily',
                 'determined', 'immediate', 'locate', 'in demand', 'technique', 'purchase', 'terrorize', 'disappearance']

    @allure.story("搜索单词解释并发音,放大拼写,查找单词图片,查找单词视频")
    @pytest.mark.parametrize("search_char", wordlist4)
    def test_words_search(self, search_char):
        READ = 3
        LOOK = 1
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
        #同义词
        syn_word = googletranspage.get_syn_word()
        googletranspage.read_syn_word(syn_word)
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