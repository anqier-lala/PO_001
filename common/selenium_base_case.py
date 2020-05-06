#coding=gbk
import unittest
from common.base_page import BasePage
from common.set_driver import set_driver
from common.config_utils import config

class SeleniumBaseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.base_page = BasePage(set_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(config.get_url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

