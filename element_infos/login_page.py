#coding=gbk
import  os
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #����by����
from common.login_utils import logger
from common.base_page import BasePage


class LoginPage(BasePage):   #object ��������ĸ���
    def __init__(self,driver):
        super().__init__(driver)  #������ø��������
        #����===>ҳ���ϵĿؼ�
        self.username_inputbox ={'element_name':'�û��������',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="account"]',
                                'time_out':6}

        self.password_inputbox ={'element_name':'���������',
                                'locator_type':'xpath',
                                'locator_value':"//input[@class='form-control'][@name='password']",
                                'time_out':3}

        self.login_button = {'element_name': '��¼��ť',
                             'locator_type': 'xpath',
                             'locator_value': "//button[@type='submit'][@class='btn btn-primary']",
                             'time_out': 1}


    def input_username(self,username):   #����===>�ؼ��Ĳ���
        self.input(self.username_inputbox,username)

    def input_password(self,password):
        self.input(self.password_inputbox,password)

    def click_login(self):
        self.click(self.login_button)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    login_pagen=LoginPage(driver)
    login_pagen.open_url("http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html")
    login_pagen.input_username("admin")
    login_pagen.input_password("201314ANQIER1")
    login_pagen.click_login()




