#coding=gbk
import  os
import time
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #����by����
from element_infos.login_page import LoginPage
from common.login_utils import logger
from common.base_page import BasePage




class MainPage(BasePage):   #object ��������ĸ���
    def __init__(self, driver):
        super().__init__(driver)  # ������ø��������
        ##��ҳһ��Ҫ�ȵ�¼�����ܽ�����Щ�����������������¼��,�ҵ�¼�ɹ�
        login_pagen = LoginPage(driver)
        login_pagen.open_url("http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html")
        self.set_browser_max()
        login_pagen.input_username("admin")
        login_pagen.input_password("201314ANQIER1")
        login_pagen.click_login()

        self.companyname_showbox ={'element_name':'��˾����',
                                'locator_type':'xpath',
                                'locator_value':'//h1[@id="companyname"]',
                                'time_out':2}

        self.myzone_menu ={'element_name':'�ҵĵ���',
                            'locator_type':'xpath',
                            'locator_value':"//li[@data-id='product']",
                            'time_out':3}

        self.product_menu ={'element_name':'��Ʒ',
                            'locator_type':'xpath',
                            'locator_value':"//li[@data-id='product']",
                            'time_out':3}


        self.username_showspan = {'element_name': '�û���',
                             'locator_type': 'xpath',
                             'locator_value': "//span[@class='user-name']",
                             'time_out': 1}


    def get_companyname(self):   #����===>�ؼ��Ĳ���
        value=self.get_title(self.companyname_showbox)
        return value

    def goto_myzone(self):   #�����ҵĵ���
        self.click(self.myzone_menu)

    def goto_product(self):   #�����Ʒ
        self.click(self.product_menu)

    def get_username(self):  #��ȡ�û���
        value = self.get_text(self.username_showspan)
        return value


if __name__ == '__main__':
    driver = webdriver.Chrome()
    main_pagin=MainPage(driver)
    time.sleep(3)
    main_pagin.get_companyname()
    time.sleep(3)
    main_pagin.get_username()
    main_pagin.goto_myzone()
    main_pagin.goto_product()








