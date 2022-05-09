import unittest2
from selenium import webdriver
from test_case.BaseTestCase import BaseTestCase


class SearchTest(BaseTestCase):
    # 测试用例
    def test_01(self):
        self.assertEqual(1, 2)

    def test_02(self):
        self.assertTrue(1)

    # 以后的测试用例就不用写打开浏览器和关闭浏览器,只需要关注业务逻辑即可
    def test_search(self):
        self.driver.get("https://www.atstudy.com/")
        self.driver.find_element_by_xpath('//*[@id="__layout"]/div/div[1]/div/div[1]/div[2]/div[1]/input')\
            .send_keys('自动化测试')
        # 点击搜索按钮
        self.driver.find_element_by_class_name('el-icon-search').click()

