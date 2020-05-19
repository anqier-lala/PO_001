#coding=gbk
import time
from common.base_page import BasePage
from common.config_utils import config
from common.set_driver import set_driver
from element_infos.login.login_page import LoginPage
from selenium.webdriver.common.by import By

# ##调试代码
# class Test(BasePage):
#
#     def login(self,driver):
#         driver.find_element(By.XPATH, '//input[@name="account"]').send_keys("admin")
#         driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys("201314ANQIER1")
#         driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()
#
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get(config.get_url)
#     test=Test(driver)
#     test.login(driver)

driver=set_driver()
base_page = BasePage(driver)
driver.maximize_window()
driver.get(config.get_url)

# driver.find_element(By.XPATH, '//input[@name="account"]').send_keys("admin")
# driver.find_element(By.XPATH, "//input[@class='form-control'][@name='password']").send_keys("201314ANQIER2")
# driver.find_element(By.XPATH, "//button[@type='submit'][@class='btn btn-primary']").click()

login = LoginPage(driver)
login.input_username("admin")
# login.ctrl_a(login.username_inputbox)
# time.sleep(2)
# login.ctrl_x(login.username_inputbox)
# time.sleep(2)
# login.ctrl_v(login.username_inputbox)

# login.back_space(login.username_inputbox)  ##删除
# login.clear_input(login.username_inputbox)  #清空
login.input_password('201314ANQIER1')
login.enter(login.login_button)  ##回车登录
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='input-group-btn']").click() # 识别OK
time.sleep(1)
# driver.find_element(By.XPATH,'//a[@data-value="project"]').click()
driver.find_element(By.XPATH,'//a[@data-value="project"]').click()

driver.find_element(By.XPATH,"//input[@id='searchInput']").send_keys('002')
driver.find_element(By.XPATH,'//a[@href="javascript:$.gotoObject();"]').click()
# print(driver.find_element(By.XPATH,'//span[@class="text"]').text)   #BUG、需求、任务、用例
time.sleep(1)
print(driver.find_element(By.XPATH,'//button[@id="currentItem"]').text)   #项目、产品








