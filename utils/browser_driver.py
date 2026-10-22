# A方案：：


# """
# 浏览器驱动初始化工具
# """
# import os
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# from utils.read_yaml import read_yaml
#
#
#
# #读取全局配置
# config_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.yaml')
# config = read_yaml(config_path)
#
# def get_driver():
#     """
#     初始化chrome浏览器驱动
#     """
#     chrome_options = Options()
#     #无头模式配置-配置文件控制开关
#     if config['browser']['headless']:
#         chrome_options.add_argument('--headless')
#     chrome_options.add_argument('--window-size=1920,1080')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--no-sandbox')
#
#     #屏蔽自动化提示条
#     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#
#     #自动下载匹配驱动
#     service= Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     #全局页面加载超时
#     driver.set_page_load_timeout(30)
#     driver.implicitly_wait(10)
#     return driver

# B方案：：

"""
浏览器驱动初始化工具
"""
# import os
# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from utils.read_yaml import read_yaml
#
#
# # 读取全局配置
# config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'config.yaml')
# config = read_yaml(config_path)
#
#
# def get_driver():
#     """
#     初始化chrome浏览器驱动
#     """
#     chrome_options = Options()
#
#     # 无头模式配置-配置文件控制开关
#     if config['browser']['headless']:
#         chrome_options.add_argument('--headless')
#
#     chrome_options.add_argument('--window-size=1920,1080')
#     chrome_options.add_argument('--disable-gpu')
#     chrome_options.add_argument('--no-sandbox')
#
#     # 屏蔽自动化提示条
#     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#     chrome_options.add_experimental_option('useAutomationExtension', False)
#
#     # ✅ 直接用本地手动下载的驱动
#     driver_path = r"D:\ecommerce_selenium\drivers\chromedriver.exe"
#     service = Service(driver_path)
#
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#
#     # 全局页面加载超时
#     driver.set_page_load_timeout(30)
#     driver.implicitly_wait(10)
#     return driver

#C方案：：
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def chrome_driver():
    """
    创建并配置一个Chrome浏览器驱动实例
    Returns:
        webdriver.Chrome: 配置好的Chrome浏览器驱动对象
    """
    # 创建Chrome选项对象
    chrome_options = Options()
    # ... 你的其他配置 ...
    # 设置Chrome浏览器启动时最大化窗口
    chrome_options.add_argument("--start-maximized")

    # 使用配置的选项创建Chrome浏览器驱动实例
    driver = webdriver.Chrome(options=chrome_options)
    # 返回创建好的驱动对象
    return driver

