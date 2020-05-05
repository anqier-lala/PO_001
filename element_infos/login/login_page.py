#coding=gbk
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logger
from common.base_page import BasePage
from common.config_utils import config
from common import login
from common.set_driver import set_driver
from common.element_data_utils import ElementdataUtils
from common.element_yamldate_utils import ElementdataYamlUtils

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        ####-----------------��һ�ַ�ʽ��ֱ��д�ֵ���ʽ---------------------####
        # self.username_inputbox = {'element_name':'�û��������',
        #                           'locator_type':'xpath',
        #                           'locator_value':'//input[@name="account"]',
        #                           'timeout': 5 }
        # self.password_inputbox = {'element_name': '���������',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//input[@name="password"]',
        #                           'timeout': 4}
        # self.login_button = {'element_name': '��¼��ť',
        #                           'locator_type': 'xpath',
        #                           'locator_value': '//button[@id="submit"]',
        #                           'timeout': 2}
        ####-----------------�ڶ��ַ�ʽ��ʹ��excecl��ȡ---------------------####
        elements=ElementdataUtils('login_page').get_element_info()
        ####-----------------�����ַ�ʽ��ʹ��yaml��ȡ---------------------####
        # current_path = os.path.dirname(__file__)
        # yaml_path = os.path.join(current_path, '../element_info_datas/element_login_infos.yaml')
        # elements=ElementdataYamlUtils().get_yaml_element_info(yaml_path)
        #####����###
        self.username_inputbox =elements['username_inputbox']
        self.password_inputbox=elements['password_inputbox']
        self.login_button=elements['login_button']
        self.change_language=elements['change_language']

    def input_username(self,username): #���� == ���ؼ��Ĳ���
        self.input( self.username_inputbox , username )


    def input_password(self,password):
        self.input( self.password_inputbox , password )

    def click_login(self):
        self.click( self.login_button )

    def moveto_change_language(self):
        self.moveto_element(self.change_language)


if __name__=="__main__":
    driver=set_driver()
    login_page =  LoginPage(driver)
    login_page.open_url('http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html')
    login_page.input_username('admin')
    login_page.input_password('201314ANQIER1')
    login_page.click_login()
    login_page.screenshot_as_file()  ##���ܽ���

#     from common.base_page import BasePage
#     driver=set_driver()
# # ����
#     login_page = LoginPage(driver)
#     login.test_login(config.get_url, config.get_user_name, config.get_password, driver)
#     login_page.screenshot_as_file()


##������������쳣������������룬����У�顣
# �쳣1-�û����������
#     login_page = LoginPage(driver)
#     login.test_login(config.get_url, config.get_error_user_name, config.get_password, driver)
#     time.sleep(2)
#     print(login_page.get_alert_content(driver))

# #�쳣2-�����������
#     login_page = LoginPage(driver)
#     login.test_login(config.get_url, config.get_user_name, config.get_error_password, driver)
#     time.sleep(2)
#     print(login_page.get_alert_content(driver))






