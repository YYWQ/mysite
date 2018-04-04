from django.test import LiveServerTestCase
from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements("css selector","tr")
        self.assertIn(row_text,[row.text for row in rows])
        time.sleep(3)
        

    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪斯听说有一个很酷的应用
        #她去看了应用的首页
        
        self.browser.get(self.live_server_url)

        #她注意到网页的标题和头部都包含“TO-DO”这个词
        time.sleep(5)
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        #她在一个文本框中输入了“Buy peacock feathers”(购买孔雀羽毛)
        #伊迪斯的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车键后，被带到了一个新URL
        #待办事件表格中显示了“1：Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        time.sleep(5)
        edith_list_url = self.browser.current_url
        time.sleep(5)
        self.assertRegex(edith_list_url,'/lists/.+')
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        
        #页面中又显示了一个文本框，可以输入其他事项
        #她输入了“Use peacock feathers to make a fly”(使用孔雀羽毛做假蝇)
        #伊迪斯做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #页面再次更新，请单中显示了这两个待办事项
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1:Buy peacock feathers')

        #现在一个叫弗朗西斯的新用户访问了网站
        ##我们使用一个新浏览器会话
        ##确保伊迪斯的信息不会从cookie中泄露出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        #弗朗西斯访问首页
        #页面中看不到伊迪斯的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        #弗朗西斯输入新的待办事件
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Do homework')
        inputbox.send_keys(Keys.ENTER)

        #弗朗西斯获得了他的唯一url
        time.sleep(5)
        francis_list_url = self.browser.current_url
        time.sleep(5)
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Do homework',page_text)
        

        self.fail("Finish the test!")

        #她访问那个URL，发现她的待办事件清单还在
        #她很满意，去睡觉了
