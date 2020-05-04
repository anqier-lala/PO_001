from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options


def set_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

# def __get_remote_driver(self):  # selenium支持分布式 grid == > 配置（你自己的代码编写、配置）
#     pass

if __name__ == '__main__':
    set_driver()