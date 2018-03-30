from selenium import  webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        #self.browser.impalicitly_wait(3)
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #伊迪斯听说有一个很酷的应用
        #她去看了应用的首页
        self.browser.get("http://localhost:8000")

        #她注意到网页的标题和头部都包含“TO-DO”这个词
        self.assertIn("To-Do",self.browser.title)
        self.fail("Finish the test!")

if __name__=="__main__":
    unittest.main(warnings='ignore')
