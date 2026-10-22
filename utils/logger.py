"""
日志记录器模块,用于生成日志记录器工具生成日志配置
"""




import logging
import os
from datetime import datetime

#创建日志文件夹

log_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')
if not os.path.exists(log_path):
    os.makedirs(log_path)

log_file=os.path.join(log_path,f"run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

def get_logger():

    """
    获取一个日志记录器实例
    Returns:
        logging.Logger: 配置好的日志记录器实例
    """
    # 创建名为"ecommerce_auto"的日志记录器
    logger = logging.getLogger("ecommerce_auto")
    # 设置日志记录器的级别为INFO，即记录INFO级别及以上的日志
    logger.setLevel(logging.INFO)
    #避免重复打印日志，检查是否已存在处理器
    if not logger.handlers:
        # 文件输出
        file_handler = logging.FileHandler(log_file,encoding="utf-8")

        #控制台输出
        console_handler = logging.StreamHandler()

        formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        file_handler.setFormatter(formatter)

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

    return logger

log = get_logger()


