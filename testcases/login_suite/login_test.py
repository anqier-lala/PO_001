#coding=gbk
import unittest
from common.set_driver import set_driver
from common.base_page import BasePage
from actions.login_action import LoginAction
from common.config_utils import config
from common.selenium_base_case import SeleniumBaseCase

class LoginTest(SeleniumBaseCase):

    def setUp(self) -> None:
        super().setUp()
        print('hello,我是一个方法类方法层面上的setup')

    def test_login_success(self):
        login_action = LoginAction( self.base_page.driver )
        main_page = login_action.login_success('admin','201314ANQIER1')
        actual_result = main_page.get_username()
        self.assertEqual(actual_result,'admin','test_login_success用例执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result = login_action.login_fail('admin1','201314ANQIER1')
        print('actual:%s'%actual_result)
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。')


if __name__ == '__main__':
    unittest.main()




