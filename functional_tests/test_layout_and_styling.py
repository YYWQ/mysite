from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        #伊迪斯访问首页
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024,768)

        #她看到输入框完美的居中展示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2,
                               #512,
                               self.browser.get_window_size().get("width")/2,
                               delta=7)
        #她新建了一个清单，看到输入框仍完美的居中显示
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width'] / 2,
                               512,delta=7)

