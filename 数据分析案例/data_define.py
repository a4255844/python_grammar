"""
  根据数据格式定义数据解析类
"""


class DataRecord:
    def __init__(self, date: str, order_id: str, money: int, province: str):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province

    def __str__(self):
        show_dict = {"date": self.date, 'order_id': self.order_id, 'money': self.money, 'province': self.province}
        return f'{show_dict}'
