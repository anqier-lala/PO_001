#coding=gbk
import  os
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #导入by方法
from element_infos.login_page import LoginPagin
from common.login_utils import logger



class MainPage(object):   #object 是所有类的父类
    def __init__(self):
        ##主页一定要先登录，才能进入这些操作，所以先引入登录类,且登录成功
        login_pagin = LoginPagin()
        login_pagin.input_username("admin")
        login_pagin.input_password("201314ANQIER1")
        login_pagin.click_login()
        ##执行下面的识别操作需要driver，而且上面没有定义，所以这里引入driver，把login_page的对象属性转移到mainpage
        self.driver=login_pagin.driver   #因为driver在LoginPage 类中已经具有该属性，所以这里直接使用类的实例化对象去调用该属性就可以
        #属性===>页面上的控件
        self.companyname_showbox=self.driver.find_element(By.XPATH, '//h1[@id="companyname"]')
        self.myzone_menu =self.driver.find_element(By.XPATH, "//li[@data-id='my']")
        self.product_menu = self.driver.find_element(By.XPATH, "//li[@data-id='product']")
        self.username_showspan=self.driver.find_element(By.XPATH, "//span[@class='user-name']")


    def get_companyname(self):   #方法===>控件的操作
        value=self.companyname_showbox.get_attribute('title')
        return value
        logger.info('获取公司名成功，公司名是'+str(value))

    def goto_myzone(self):   #进入我的地盘
        self.myzone_menu.click()

    def goto_product(self):   #进入产品
        self.product_menu.click()

    def get_username(self):  #获取用户名
        value=self.username_showspan.text
        return  value


if __name__ == '__main__':
    main_pagin=MainPage()   #初始化的时候已经全部识别所有元素
    companyname=main_pagin.get_companyname()
    print(companyname)
    username=main_pagin.get_username()
    print(username)
    main_pagin.goto_myzone()   ##不能点击到我的地盘，线性脚本是识别一个元素操作一个元素，目前版本的是PO模式，实例化页面对象之后，识别所有
    #的元素，然后再去操作，可能发生元素不能识别的问题。
    main_pagin.goto_product()









