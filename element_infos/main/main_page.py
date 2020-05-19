#coding=gbk
import time
from selenium import webdriver
from common.base_page import BasePage
from common.config_utils import config
from common.element_data_utils import ElementdataUtils
from element_infos.login.login_page import LoginPage
# from actions.login_action import LoginAction
from common.set_driver import set_driver


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # ������ø��������
        elements = ElementdataUtils('main','main_page').get_element_info()
        self.companyname_showbox =elements['companyname_showbox']
        self.myzone_menu=elements['myzone_menu']
        self.product_menu=elements['product_menu']
        self.username_showspan=elements['username_showspan']
        self.project_menu=elements['project_menu']
        self.test_menu=elements['test_menu']
        self.file_menu=elements['file_menu']
        self.user_menu=elements['user_menu']
        self.quit_button=elements['quit_button']
        # ����Ԫ������У��link��ת
        self.myzone_menu_homepage=elements['myzone_menu_homepage']
        self.product_menu_productpage=elements['product_menu_productpage']
        self.project_menu_projectpage=elements['project_menu_projectpage']
        self.test_menu_testpage=elements['test_menu_testpage']
        self.file_menu_filepage=elements['file_menu_filepage']
        # ����Ԫ������У����������
        self.search_general_options=elements['search_general_options']
        self.search_options_bug=elements['search_options_bug']
        self.search_options_story=elements['search_options_story']
        self.search_options_task=elements['search_options_task']
        self.search_options_testcase=elements['search_options_testcase']
        self.search_options_project=elements['search_options_project']
        self.search_options_product=elements['search_options_product']
        self.search_input =elements['search_input ']
        self.search_go_button=elements['search_go_button']
        self.title_bug_story_task_testcase=elements['title_bug_story_task_testcase']
        self.title_project_product=elements['title_project_product']


    def get_companyname(self):   #����===>�ؼ��Ĳ���
        value=self.get_element_attribute(self.companyname_showbox,'title')
        return value

    def goto_myzone(self):   #�����ҵĵ���
        self.click(self.myzone_menu)
        value=self.get_text(self.myzone_menu_homepage)
        return value

    def goto_product(self):   #�����Ʒ
        self.click(self.product_menu)
        value=self.get_text(self.product_menu_productpage)
        return value

    def get_username(self):  #��ȡ�û���
        value = self.get_text(self.username_showspan)
        return value

    def click_username(self):
        self.click( self.user_menu )

    def click_quit_button(self):
        self.click( self.quit_button )

    def goto_project(self):   #������Ŀ���ȡ��Ŀ��ҳ��ʶ
        self.click(self.project_menu)
        value = self.get_text(self.project_menu_projectpage)
        return value

    def goto_test(self):   #������Ժ��ȡ������ҳ�İ���ʶ
        self.click(self.test_menu)
        value = self.get_text(self.test_menu_testpage)
        return value

    def goto_file(self):  #�����ĵ���ȡ�ĵ���ҳ��ʶ
        self.click(self.file_menu)
        value = self.get_text(self.file_menu_filepage)
        return value

    def search_by_bug(self):
        self.select_drop_down_box(self.search_general_options,self.search_options_bug)

    def search_by_story(self):
        self.select_drop_down_box(self.search_general_options,self.search_options_story)

    def search_by_task(self):
        self.select_drop_down_box(self.search_general_options,self.search_options_task)

    def search_by_testcase(self):
        self.select_drop_down_box(self.search_general_options,self.search_options_testcase)

    def search_by_project(self):
        self.select_drop_down_box(self.search_general_options,self.search_options_project)

    def search_by_product(self):
        self.select_drop_down_box(self.search_general_options,self.search_options_product)

    def input_search_content(self,content):
        self.input(self.search_input,content)  #������������

    def click_search_go(self):
        self.click(self.search_go_button)

    def get_title_bug_story_task_testcase(self):
        value=self.get_text(self.title_bug_story_task_testcase)   #�������ȡ������Ϣ�����ں˶�������ȷ
        return value

    def get_title_project_product(self):
        value=self.get_text(self.title_project_product)
        return value

if __name__ == '__main__':
    from actions.login_action import LoginAction
    driver =set_driver()
    driver.get(config.get_url)
    main_page = LoginAction(driver).default_login()
    main_page.wait(2)   #���Ե��÷�װ�ĵȴ�����
    main_page.search_by_bug()
    main_page.input_search_content('003') ##����BUG�������
    main_page.click_search_go()
    print(main_page.get_title_bug_story_task_testcase())
    main_page.search_by_product()
    main_page.input_search_content('001')  ##���ݲ�Ʒ�������
    main_page.click_search_go()
    print(main_page.get_title_project_product())











    # print(main_page.get_companyname())
    # main_page.wait(1)
    # print(main_page.get_username())
    # main_page.wait(1)
    # print(main_page.goto_myzone())
    # main_page.wait(1)
    # print(main_page.goto_product())
    # main_page.wait(1)
    # print(main_page.goto_project())
    # main_page.wait(1)
    # print(main_page.goto_test())
    # main_page.wait(1)
    # print(main_page.goto_file())





