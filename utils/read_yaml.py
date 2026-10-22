"""
用于读取yaml文件配置
"""


import yaml
import os
import pandas as pd
from typing import Union,List,Dict


def read_yaml(file_path):
    """
    读取yaml文件
    :param file_path:
    :return:
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"c：{file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def read_csv(file_path:str,
             to_dict_list:bool=True,
             encoding:str = 'utf-8',
             chunksize:Union[int,None] = None
             ) -> Union[List[Dict],pd.DataFrame]:
    """
    读取csv文件
 读取csv文件

    :param file_path: csv文件路径
    :param to_dict_list: True 返回[{},{}]列表；False 返回pandas.DataFrame
    :param encoding: 文件编码，默认为utf-8
    :param chunksize: 分块读取的行数，None表示不分块
    :return: 根据to_dict_list参数返回字典列表或DataFrame
    :raises FileNotFoundError: 当文件不存在时
    :raises PermissionError: 当没有文件读取权限时
    :raises pd.errors.EmptyDataError: 当文件为空时
    :raises UnicodeDecodeError: 当文件编码不匹配时
    """
    #验证文件路径：
    if not isinstance(file_path,str) or not file_path.split():
        raise ValueError("文件路径必须是非空字符串")

    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"csv文件不存在：{file_path}")

    #检查文件权限：
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"没有读取csv文件的权限：{file_path}")


    try:
        # 使用pandas读取csv文件
        df = pd.read_csv(file_path,
                         encoding=encoding,
                         chunksize=chunksize,
                         on_bad_lines='skip')#跳过格式错误的行
        #处理分块读取的情况
        if chunksize is not None:
            if to_dict_list:
                return [chunk.to_dict('records') for chunk in df]
            return df

        #处理常规读取

        if to_dict_list:
            # 转为字典列表，每条数据一行字典，适合pytest参数化
            return df.to_dict('records')
        return df
    except pd.errors.EmptyDataError:
        raise ValueError(f"csv文件为空：{file_path}")

    except UnicodeDecodeError:
        raise ValueError(f"csv文件编码不是{encoding}")

    except Exception as e:
        raise RuntimeError(f"读取csv文件出错：{file_path}，错误信息：{e}")

