#coding=gbk
import  os
from  selenium import  webdriver
from selenium.webdriver.common.by import By  #����by����
from element_infos.login_page import LoginPagin
from common.login_utils import logger



class MainPage(object):   #object ��������ĸ���
    def __init__(self):
        ##��ҳһ��Ҫ�ȵ�¼�����ܽ�����Щ�����������������¼��,�ҵ�¼�ɹ�
        login_pagin = LoginPagin()
        login_pagin.input_username("admin")
        login_pagin.input_password("201314ANQIER1")
        login_pagin.click_login()
        ##ִ�������ʶ�������Ҫdriver����������û�ж��壬������������driver����login_page�Ķ�������ת�Ƶ�mainpage
        self.driver=login_pagin.driver   #��Ϊdriver��LoginPage �����Ѿ����и����ԣ���������ֱ��ʹ�����ʵ��������ȥ���ø����ԾͿ���
        #����===>ҳ���ϵĿؼ�
        self.companyname_showbox=self.driver.find_element(By.XPATH, '//h1[@id="companyname"]')
        self.myzone_menu =self.driver.find_element(By.XPATH, "//li[@data-id='my']")
        self.product_menu = self.driver.find_element(By.XPATH, "//li[@data-id='product']")
        self.username_showspan=self.driver.find_element(By.XPATH, "//span[@class='user-name']")


    def get_companyname(self):   #����===>�ؼ��Ĳ���
        value=self.companyname_showbox.get_attribute('title')
        return value
        logger.info('��ȡ��˾���ɹ�����˾����'+str(value))

    def goto_myzone(self):   #�����ҵĵ���
        self.myzone_menu.click()

    def goto_product(self):   #�����Ʒ
        self.product_menu.click()

    def get_username(self):  #��ȡ�û���
        value=self.username_showspan.text
        return  value


if __name__ == '__main__':
    main_pagin=MainPage()   #��ʼ����ʱ���Ѿ�ȫ��ʶ������Ԫ��
    companyname=main_pagin.get_companyname()
    print(companyname)
    username=main_pagin.get_username()
    print(username)
    main_pagin.goto_myzone()   ##���ܵ�����ҵĵ��̣����Խű���ʶ��һ��Ԫ�ز���һ��Ԫ�أ�Ŀǰ�汾����POģʽ��ʵ����ҳ�����֮��ʶ������
    #��Ԫ�أ�Ȼ����ȥ���������ܷ���Ԫ�ز���ʶ������⡣
    main_pagin.goto_product()









