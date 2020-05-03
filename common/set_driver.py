from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options


def set_driver():
    chrome_options = Options()
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
    chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def __get_remote_driver(self):  # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
    pass

if __name__ == '__main__':
    set_driver()