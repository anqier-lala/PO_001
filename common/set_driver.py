from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options


def set_driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')  # �ȸ��ĵ��ᵽ��Ҫ����������������bug
    chrome_options.add_argument('lang=zh_CN.UTF-8')  # ����Ĭ�ϱ���Ϊutf-8
    chrome_options.add_experimental_option('useAutomationExtension', False)  # ȡ��chrome���Զ�������ʾ
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # ȡ��chrome���Զ�������ʾ
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def __get_remote_driver(self):  # selenium֧�ֲַ�ʽ grid == > ���ã����Լ��Ĵ����д�����ã�
    pass

if __name__ == '__main__':
    set_driver()