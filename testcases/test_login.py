import pytest
from utils.browser_driver import chrome_driver
from page.login_page import LoginPage
import os
from utils.read_yaml import read_yaml


root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg_path=os.path.join(root_path,'config','config.yaml')
config = read_yaml(cfg_path)
# 全局fixture，每个用例自动创建/销毁浏览器
@pytest.fixture(scope="function")
def driver():
    dr = chrome_driver()
    yield dr
    dr.quit()

# 正常登录用例
def test_login_success(driver):
    login_page = LoginPage(driver)
    login_page.login(config["user"]["username"],
                    config["user"]["password"]
                )

    import time
    time.sleep(3)
    # 断言：登录成功后页面包含用户名（根据你的电商页面修改xpath）
    assert "xiaoyi xiaoyi" in driver.page_source

# 错误密码登录失败用例
def test_login_fail_wrong_pwd(driver):
    login_page = LoginPage(driver)
    login_page.login(config["user"]["username"], "wrong123")

    tip = login_page.get_error_tip()
    assert "邮箱或密码不正确" in tip