from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('td')
        self.assertIn(row_text,[row.text for row in rows])
        time.sleep(1)
        

    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪斯听说有一个很酷的应用
        #她去看了应用的首页
        self.browser.get("http://localhost:8000")

        #她注意到网页的标题和头部都包含“TO-DO”这个词
        self.assertIn("To-Do",self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        #self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a To-Do item')
        #她在一个文本框中输入了“Buy peacock feathers”(购买孔雀羽毛)
        #伊迪斯的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车键后，页面更新了
        #待办事件表格中显示了“1.Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)
        
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        
        #页面中又显示了一个文本框，可以输入其他事项
        #她输入了“Use peacock feathers to make a fly”(使用孔雀羽毛做假蝇)
        #伊迪斯做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        #页面再次更新，请单中显示了这两个待办事项
        self.check_for_row_in_list_table('3:Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        

        self.fail("Finish the test!")

if __name__=="__main__":
    unittest.main(warnings='ignore')
