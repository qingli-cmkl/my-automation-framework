from page.BasePage import BasePage
from selenium.webdriver.common.by import By
from utils.logger import log


#商品页面

class ProductPage(BasePage):
    """
    商品页面类，继承自BasePage，包含商品页面的所有元素定位和操作方法
    """
    # 页面元素定位器 (元组：定位方式, 表达式)
    product_name = (By.XPATH, "//div[@class='block_product_name']")  # 商品名称元素定位器
    product_price = (By.XPATH, "//div[@class='product_price']")  # 商品价格元素定位器
    product_add_cart = (By.XPATH, "//div[@class='secondary_btn product-cart control-product_detail-cart']")  # 添加购物车按钮元素定位器
    product_cart = (By.XPATH, "//div[@class='product-cart']")  # 购物车元素定位器
    product_cart_count = (By.XPATH, "//div[@class='cart']")  # 购物车数量元素定位器
    product_cart_total = (By.XPATH, "//div[@class='cart_total_price']")  # 购物车总价元素定位器
    product_cart_checkout = (By.XPATH, "//div[@class='cart_order_btn']")  # 购物车结算按钮元素定位器
    product_cart_empty = (By.XPATH, "//div[@class='cart_list_delete_all']")  # 空购物车元素定位器-删除购物车按钮
    product_cart_delete = (By.XPATH, "//div[@class='mo-handle-btn mo-handle-ok']")  # 空购物车元素定位器-删除购物车
    product_cart_empty_text = (By.XPATH, "//div[@class='cart_empty_content']")  # 空购物车提示文本元素定位器
    product_cart_empty_btn = (By.XPATH, "//div[@class='continue_shopping_btn']")  # 继续购物按钮元素定位器

    def get_product_name(self):
        """
        获取商品名称
        :return: 商品文本内容
        """
        return self.get_text(self.product_name)
    def get_product_price(self):
        """
        获取商品价格
        :return: 商品价格文本内容
        """
        return self.get_text(self.product_price)

    def add_product_to_cart(self):
        """
        点击添加购物车按钮，将商品添加到购物车
        """
        self.click(self.product_add_cart)

    def get_product_cart_count(self):
        """
        获取购物车中的商品数量
        :return: 购物车数量文本内容
        """
        return self.get_text(self.product_cart_count)

    def get_product_cart_total(self):
        """
        获取购物车中的商品总价
        :return: 购物车总价文本内容
        """
        return self.get_text(self.product_cart_total)

    def click_product_cart_checkout(self):
        """
        点击购物车结算按钮
        """
        self.click(self.product_cart_checkout)

    def get_product_cart_empty_text(self):
        """
        获取空购物车的提示文本
        :return: 空购物车提示文本内容
        """
        return self.get_text(self.product_cart_empty_text)


