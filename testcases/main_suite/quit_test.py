#coding=gbk
import unittest
from common.set_driver import set_driver
from common.base_page import BasePage
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.config_utils import config
from common.selenium_base_case import SeleniumBaseCase

class QuitTest(SeleniumBaseCase):

    def test_quit(self):
        login_action = LoginAction(self.base_page.driver)
        main_page = login_action.default_login()
        main_page.wait(3)
        print("登录成功")
        quit_action = QuitAction( main_page.driver )
        login_page = quit_action.quit()
        actual_result = login_page.get_title()
        print(actual_result)
        self.assertEqual( actual_result.__contains__('用户登录'),True,'test_quit用例不通过' )

if __name__=='__main__':
    unittest.main()





