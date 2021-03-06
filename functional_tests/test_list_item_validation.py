from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
import time
class ItemValidationTest(FunctionalTest):
    #验证空的待办事项
    def test_cannot_add_empty_list_items(self):
        #伊迪斯访问首页时，不小心提交了一个空的待办事项
        #输入框没输入内容，她就按下了回车键
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('\n')
        inputbox.send_keys(Keys.ENTER)

        #首页刷新了，显示一个错误消息
        #提示待办事项不能为空
        #error = self.browser.find_element("css selector","")
        error = self.browser.find_element_by_class_name("help-block")
        self.assertEqual(error.text,"You can't have an empty list item")

        #她输入一些文字，然后再次提交，这次没问题了
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy milk')

        #她有点儿调皮，又提交了一个空待办事项
        inputbox = self.get_item_input_box()
        inputbox.send_keys('\n')
        inputbox.send_keys(Keys.ENTER)
        
        #在清单页面她看到了一个类似的错误消息
        self.check_for_row_in_list_table('1:Buy milk')
        error = self.browser.find_element_by_class_name("help-block")
        self.assertEqual(error.text,"You can't have an empty list item")
        
        #输入文字后就没问题了
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Make tea')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        self.check_for_row_in_list_table('1:Buy milk')
        self.check_for_row_in_list_table('2:Make tea')

    #验证重复待办事项
    def test_cannot_add_duplicate_items(self):
        #伊迪斯访问首页，新建一个清单
        self.browser.get(self.server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy bananas')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy bananas')

        #她不小心输入了一个重复的待办事项
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy bananas')
        inputbox.send_keys(Keys.ENTER)

        #她看到一条有帮助的错误信息
        self.check_for_row_in_list_table('1:Buy bananas')
        error = self.browser.find_element_by_class_name("help-block")
        self.assertEqual(error.text,"You've already got this in your list")
        
