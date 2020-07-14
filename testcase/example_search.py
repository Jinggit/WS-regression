import sys
sys.path.append("..")
import pytest
import allure
from base.browser import Browser
from po.homepage import HomePage



@allure.feature("百度搜索")
class TestBaiduSearch:
    @classmethod
    def setup_class(cls):
        browse = Browser(cls)
        cls.driver = browse.get_driver()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.story("测试百度搜索，验证标题是否正确")
    @pytest.mark.parametrize("search_char, verify_char", [('龙珠', '龙珠_百度搜索'), ('火影忍者', '火影忍者_百度搜索')])
    def test_search(self, search_char, verify_char):
        baidu_homepage = HomePage(self.driver)
        baidu_homepage.open_homepage()
        baidu_homepage.search(search_char)
        baidu_homepage.verify(verify_char)


if __name__ == '__main__':
    pytest.main()