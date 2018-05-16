from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
import time
import unittest
from unittest import skip
import sys

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls): #①
        for arg in sys.argv: #②
            if 'liveserver' in arg: #③
                cls.server_url = 'http://' + arg.split('=')[1] #④
                return #⑤
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(10)
        
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements("css selector","tr")
        self.assertIn(row_text,[row.text for row in rows])

    def get_item_input_box(self):
        return self.browser.find_element_bt_id('id_text')
        

