from page.BasePage import BasePage
from utils.read_yaml import read_yaml
from selenium.webdriver.common.by import By
import os

root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg_path=os.path.join(root_path,'config','config.yaml')
config = read_yaml(cfg_path)
class LoginPage(BasePage):
    # 页面元素定位器 (元组：定位方式, 表达式)
    username_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//input[@name='password']")
    login_btn = (By.ID, "confirm")
    error_msg = (By.XPATH, "//div[@class='mo-form-item-error']")

    # 页面URL
    @staticmethod
    def get_login_url():
        try:
            base_url = config["env"]["test"]
            login_url = config["env"]["login"]
            return f"{base_url}{login_url}"
        except KeyError :
            return "https://wen-10-discount.oemsaas.cn"

    # 登录业务方法
    def login(self, username, password):
        self.open_url(self.get_login_url())
        self.input_text(self.username_input, username)
        self.input_text(self.password_input, password)
        self.click(self.login_btn)

    # 获取登录错误提示
    def get_error_tip(self):
        return self.get_text(self.error_msg)



#调试：：
# if __name__ == '__main__':
#     from selenium import webdriver
#
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#
#     try:
#         page = LoginPage(driver)   # ✅ 传入 driver
#         page.login(
#             config["user"]["username"],
#             config["user"]["password"]
#         )
#         import time
#         time.sleep(3)
#         assert "密码的长度应在6-15之间" in page.get_error_tip()
#     finally:
#         input("按回车关闭浏览器...")
#         driver.quit()