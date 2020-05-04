from selenium import webdriver
from common.config_utils import config
from selenium.webdriver.chrome.options import Options


def set_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('disable-infobars')
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    return driver

# def __get_remote_driver(self):  # selenium֧�ֲַ�ʽ grid == > ���ã����Լ��Ĵ����д�����ã�
#     pass

if __name__ == '__main__':
    set_driver()