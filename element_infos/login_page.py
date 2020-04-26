#coding=gbk
import  os
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from common.login_utils import logger
from common.base_page import BasePage


class LoginPage(BasePage):   #object 是所有类的父类
    def __init__(self,driver):
        super().__init__(driver)  #子类调用父类的属性
        #属性===>页面上的控件
        self.username_inputbox ={'element_name':'用户名输入框',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="account"]',
                                'time_out':6}

        self.password_inputbox ={'element_name':'密码输入框',
                                'locator_type':'xpath',
                                'locator_value':"//input[@class='form-control'][@name='password']",
                                'time_out':3}

        self.login_button = {'element_name': '登录按钮',
                             'locator_type': 'xpath',
                             'locator_value': "//button[@type='submit'][@class='btn btn-primary']",
                             'time_out': 1}


    def input_username(self,username):   #方法===>控件的操作
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




