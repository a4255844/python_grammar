"""
 用于读取文件的类, 两种格式 文本 和 json, 使用多态思想来封装
"""
from typing import List

from data_define import DataRecord
import json


class FileReader:
    def read_data(self) -> List[DataRecord]:
        pass


class TextReader(FileReader):
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> List[DataRecord]:
        text_file = open(self.path, 'r', encoding='UTF-8')
        data_list: List[DataRecord] = []
        for row in text_file.readlines():
            row = row.strip()
            row_list = row.split(',')
            # for item in row_list:
            data_list.append(DataRecord(row_list[0], row_list[1], int(row_list[2]), row_list[3]))
        text_file.close()
        return data_list


class JsonReader(FileReader):
    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> List[DataRecord]:
        json_data = open(self.path, 'r', encoding='UTF-8')
        data_list: List[DataRecord] = []

        for row in json_data.readlines():
            row_dict = json.loads(row)
            # print(row_dict, type(row_dict))
            # for item in row_list:
            data_list.append(
                DataRecord(row_dict['date'], row_dict['order_id'], int(row_dict['money']), row_dict['province']))
        json_data.close()
        return data_list


if __name__ == "__main__":
    t = TextReader("G:/BaiduNetdiskDownload/python/资料/第13章资料/2011年1月销售数据.txt")
    t_data = t.read_data()
    j = JsonReader("G:/BaiduNetdiskDownload/python/资料/第13章资料/2011年2月销售数据JSON.txt")
    j_data = j.read_data()
    for r in t_data:
        print(r, 't')
    for r in j_data:
        print(r, 'j')
