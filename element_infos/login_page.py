#coding=gbk
import  os
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法


class LoginPagin(object):   #object 是所有类的父类
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby9teS5odG1s.html')
        #属性===>页面上的控件
        self.username_inputbox=self.driver.find_element(By.XPATH, '//input[@name="account"]')
        self.password_inputbox =self.driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']")
        self.login_button = self.driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']")


    def input_username(self,username):   #方法===>控件的操作
        self.username_inputbox.send_keys(username)

    def input_password(self,password):
        self.password_inputbox.send_keys(password)

    def click_login(self):
        self.login_button.click()


if __name__ == '__main__':
    login_pagin=LoginPagin()
    login_pagin.input_username("admin")
    login_pagin.input_password("201314ANQIER1")
    login_pagin.click_login()




