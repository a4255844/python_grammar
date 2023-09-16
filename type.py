"""
类型注解
python可以自动进行类型推断,包括模块化中的文件也可以自动进行类型推断
如果变量已经赋值, python就会自动推断类型并提示
"""
import random
from my_package import type_test

# 基础数据类型注解
val_1: int = 3
val_2: str = '123'
val_3: float = 1.12
val_4: bool = False
# 容器数据类型注解
my_list = [1, 2, 3, 4, '21']
my_tuple = ('str', False, my_list)
my_dict = {'age': 12}

# 在注释中类型注解
val_11 = random.randint(1, 11)  # type: int
"""
 python可以自动进行类型推断,包括模块化中的文件也可以自动进行类型推断
"""
val_5 = type_test.val_5
modules_type = type_test.TestType()
modules_type.test_func(False, '12', [1])
val_6 = type_test.val_T1


class TestType:
    name: str
    age: int

    def test_func(self, p1: bool, p2: str, p3: list):
        return [1, 2] or False
