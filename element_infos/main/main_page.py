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
        super().__init__(driver)  # 子类调用父类的属性
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
        # 以下元素用于校验link跳转
        self.myzone_menu_homepage=elements['myzone_menu_homepage']
        self.product_menu_productpage=elements['product_menu_productpage']
        self.project_menu_projectpage=elements['project_menu_projectpage']
        self.test_menu_testpage=elements['test_menu_testpage']
        self.file_menu_filepage=elements['file_menu_filepage']
        # 以下元素用于校验搜索功能
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


    def get_companyname(self):   #方法===>控件的操作
        value=self.get_element_attribute(self.companyname_showbox,'title')
        return value

    def goto_myzone(self):   #进入我的地盘
        self.click(self.myzone_menu)
        value=self.get_text(self.myzone_menu_homepage)
        return value

    def goto_product(self):   #进入产品
        self.click(self.product_menu)
        value=self.get_text(self.product_menu_productpage)
        return value

    def get_username(self):  #获取用户名
        value = self.get_text(self.username_showspan)
        return value

    def click_username(self):
        self.click( self.user_menu )

    def click_quit_button(self):
        self.click( self.quit_button )

    def goto_project(self):   #进入项目后获取项目主页标识
        self.click(self.project_menu)
        value = self.get_text(self.project_menu_projectpage)
        return value

    def goto_test(self):   #进入测试后获取测试主页文案标识
        self.click(self.test_menu)
        value = self.get_text(self.test_menu_testpage)
        return value

    def goto_file(self):  #进入文档获取文档主页标识
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
        self.input(self.search_input,content)  #输入搜索内容

    def click_search_go(self):
        self.click(self.search_go_button)

    def get_title_bug_story_task_testcase(self):
        value=self.get_text(self.title_bug_story_task_testcase)   #搜索后获取标题信息，用于核对搜索正确
        return value

    def get_title_project_product(self):
        value=self.get_text(self.title_project_product)
        return value

if __name__ == '__main__':
    from actions.login_action import LoginAction
    driver =set_driver()
    driver.get(config.get_url)
    main_page = LoginAction(driver).default_login()
    main_page.wait(2)   #调试调用封装的等待方法
    main_page.search_by_bug()
    main_page.input_search_content('003') ##根据BUG编号搜索
    main_page.click_search_go()
    print(main_page.get_title_bug_story_task_testcase())
    main_page.search_by_product()
    main_page.input_search_content('001')  ##根据产品编号搜索
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





