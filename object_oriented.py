"""
    面向对象
"""
import winsound


class Person:
    name = None
    gender = None
    age = None

    def say_hi(self):  # self 基本等同于 js this
        print(f"哈喽,我是{self.name}")


class Rap:
    menu = "七里香"

    def sing_rap(self):
        print(f"哈喽我是{self.name or '无名'},由我来表演一首{self.menu}")


class Student(Person, Rap):  # 继承语法, 可继承多个父类,如有同名属性或方法, 优先使用最先继承的
    nationality = None  # 国籍
    native_place = None  # 籍贯
    __private = "我是私有属性"

    # __init__ : 类似 constructor
    def __init__(self, name, gender, age, nationality, native_place):
        self.name = name
        self.gender = gender
        self.age = age
        self.nationality = nationality
        self.native_place = native_place

    def say_hi(self):  # 复写父类中的方法
        print(f"哈喽大家好大神大神达到23,我是{self.name}")
        Rap.sing_rap(self)  # 调用父类的方法 super: 所有父类
        super().say_hi()  # 调用父类的say_hi方法

    def __private_func(self):
        pass  # pass 用于代替编写功能,使通过编译器


stu_1 = Student('jay chou', '男', 22, '台湾', '台湾')
print(stu_1.native_place, stu_1.name)
stu_1.say_hi()
stu_1.sing_rap()


class Clock:
    id = None

    def ring(self):
        winsound.Beep(2000, 3000)


obj_clock1 = Clock()
obj_clock1.id = "88888888"
# obj_clock1.ring()
