"""
    将Json数据和python 字典 | 列表相互转换
"""
import json

data = [{"name": "小王", "age": 11}, {"name": "小绿", "age": 12}, {"name": "小红", "age": 18}]
json_str = json.dumps(data, ensure_ascii=False)  # ensure_ascii: 控制编码格式,默认true 中文转ascii编码
print(type(json_str))
print(json_str)
my_l = json.loads(json_str)  # 转回python list数据类型
print(type(my_l))
print(my_l)
