"""
  总共有两个月份的数据
 计算每一天的销售额
 实现数据可视化
"""
from typing import List

from file_define import TextReader, JsonReader
from data_define import DataRecord

data_1 = TextReader("G:/BaiduNetdiskDownload/python/资料/第13章资料/2011年1月销售数据.txt").read_data()
data_2 = JsonReader("G:/BaiduNetdiskDownload/python/资料/第13章资料/2011年2月销售数据JSON.txt").read_data()

merge_data = data_1 + data_2
print(merge_data, 'merge_data')


def count_money(data: List[DataRecord]):
    """
    分别计算每一天的销售额
    :param data:
    :return: dict
    """
    count_dict: {str: int} = {}
    for item in data:
        try:
            count_dict[item.date] += item.money
        except KeyError:
            count_dict[item.date] = item.money

    return count_dict


_data = count_money(merge_data)
# print(count_money(merge_data))
