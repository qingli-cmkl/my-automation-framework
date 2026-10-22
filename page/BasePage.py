from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import log
import os
from datetime import datetime

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)  #显示等待15秒

    #等待元素可见
    def wait_visible(self,locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            log.error(f"等待元素可见超时:{locator}")
            self.save_screenshot()
            raise

    #等待元素可点击
    def wait_clickable(self,locator):
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            log.error(f"等待元素可点击超时:{locator}")
            self.save_screenshot()
            raise



    #点击元素
    def click(self,locator):
        """
        点击指定元素
        :param locator: 元定位器，如(By.ID, 'element_id')
        :return: 无
        """
        ele=self.wait_clickable(locator)
        ele.click()
        log.info(f"点击元素:{locator}")


    #输入文本
    def input_text(self,locator,text):
        """
        在指定元素中输入文本
        :param locator: 元定位器，如(By.ID, 'element_id')
        :param text: 要输入的文本内容
        :return: 无
        """
        ele=self.wait_visible(locator)
        ele.click()
        ele.clear()
        ele.send_keys(text)
        log.info(f"输入文本:{locator}，输入内容为:{text}")



    #获取文本

    def get_text(self,locator):
        """
        获取指定元素的文本内容
        :param locator: 元定位器，如(By.ID, 'element_id')
        :return: 元素的文本内容
        """
        ele=self.wait_visible(locator)
        text = ele.get_attribute('textContent') or ele.text
        log.info(f"获取文本:{text}")
        return text


    #打开页面地址
    def open_url(self,url):
        """
        打开指定URL页面
        :param url: 要打开的页面URL
        :return: 无
        """
        self.driver.get(url)
        log.info(f"打开页面地址:{url}")

    #截图保存，失败自动调用
    def save_screenshot(self):
        """
        保存当前页面截图
        :return: 无
        """
        screenshot_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'report')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        file_name = f"error_{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        file_path = os.path.join(screenshot_dir,file_name)
        self.driver.save_screenshot(file_path)
        log.info(f"截图保存成功，文件路径为:{file_path}")


    #关闭浏览器

    def close_driver(self):
        """
        关闭浏览器驱动
        :return: 无
        """
        self.driver.quit()
        log.info("关闭浏览器")

