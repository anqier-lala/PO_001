#coding=gbk
import  os
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from common.login_utils import logger


class LoginPagin(object):   #object 是所有类的父类
    def __init__(self):
        self.driver=webdriver.Chrome()    #属性
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html')
        #属性===>页面上的控件
        self.username_inputbox=self.driver.find_element(By.XPATH, '//input[@name="account"]')
        self.password_inputbox =self.driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']")
        self.login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']")


    def input_username(self,username):   #方法===>控件的操作
        self.username_inputbox.send_keys(username)
        logger.info('用户名输入框输入：'+str(username))   #直接引用外部的对象，不能加self

    def input_password(self,password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入框输入：' + str(password))

    def click_login(self):
        self.login_button.click()
        logger.info('点击登录按钮')

if __name__ == '__main__':
    login_pagin=LoginPagin()
    login_pagin.input_username("admin")
    login_pagin.input_password("201314ANQIER1")
    login_pagin.click_login()




