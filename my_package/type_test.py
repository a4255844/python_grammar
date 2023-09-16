# 在注释中类型注解
import random

val_5 = random.randint(1, 10)
val_T1 = {'name': 'jay', 'age': 15}


class TestType:
    name: str
    age: int

    def test_func(self, p1: bool, p2: str, p3: list):
        return [1, 2] or False
