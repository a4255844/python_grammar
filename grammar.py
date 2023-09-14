# 数据类型
# Number(int, float, complex, bool); String; List; Tuple; Set; Dictionary;

# 字符串拼接
age = 18
name = "小明"
print('1' + name + '今年18岁了!')
# print( name + age + '岁了' ) error: 字符串不允许拼接数字
# 占位符拼接法 %s:将数据转换为字符串并拼接, %d: 转换成整数; %f: 转换成浮点数,
# m.n:  m控制整数宽度, .n:控制小数长度
print("2%s今年18了" % name)
print('3%s今年%.2f' % (name, age))  # 可以拼接数字
# 快速拼接: 字符串前面加 f
print(f"4{name}今年{age}岁了")

# input() 获取用户输入 type(): 获取值的数据类型
# val = input("请输入")
# print(f"您的输入是{val},它的类型是{type(val)}")
# 数据类型转换
print(type(str(age)))
print(type(int(age)))
print(type(float(age)))
# 测试if语句: if条件内代码必须有缩进 if else if 在python中被写为 if elif
# 对结果取反用not关键字, if 内的代码块，没有自己的作用域，变量可以在全局中访问
if 2 == 3:
    print('if内部进来了')
elif not None:
    testVal = '1'
    print('elif进来了')
else:
    print("else进来了")
print('全局代码')
print('访问if内的变量var:' + testVal)
i = 1
sum = 0
while (i <= 100):
    sum += i
    i += 1
print(f"从1累加至100的结果是:{sum}")
# for 循环 类似 js for in 循环, 可遍历:  字符串, 列表, 元俎
for x in 'shaoyabo':
    print(x)
# range语句: 获取数列, range(a, b, step): 从a到b(不包含b), step: 步长, 如果接收一个数字则从0开始, 一般配合for循环使用
for x in range(6, 20, 3):
    print(x)

# 函数， 如果不返回结果，默认返回None， 函数有作用域， 和其他编程语言类似
testFunVal = 100


def customSum(a, b):
    """
    相加
    :param a: first
    :param b: second
    :return: 相加的结果
    """
    print(testFunVal)
    return a + b


print(customSum(989, 2321))


def testReturn(a):
    # print(testFunVal) #报错, 不能再定义前使用，并且不会访问全局变量
    global testFunVal  # 如果需要影响全局变量需要这么写，否则全局变量不会被修改
    global testFunVal1
    testFunVal1 = 33
    testFunVal = 1000
    print(testFunVal)
    a += 1


print(testReturn(1))
print(f'在函数内使用全局同名变量并重新赋值的结果：{testFunVal}, {testFunVal1}')

# 数据容器
# list : 类似与js数组, 区别，可以使用负数下标，倒着取， -1开始递减
myList = ['j', 'a', 'y', 'element', 'element', 'element']
print(myList[-1], myList[1], myList)
myList.insert(1, 'element')  # 追加元素, 直接插入到指定位置
myList.append('element')  # 末尾追加
myList.extend([1, 2, 3])  # 追加数据组
del myList[1]  # 删除指定下标位置的元素
myList.pop(1)  # 删除指定下标位置的元素，并返回删除的元素
myList.remove('element')  # 删除指定元素，如果有多个则删除第一个
myList.clear()  # 清空列表
count = myList.count('element')  # 统计元素在列表中的个数
length = len(myList)  # 获取长度
# 元组 元素不可修改，可定义任意类型
myTuple = ('j', 'a', 'y', True, myList)
myTuple2 = (1,)  # 单个元素必须加,
# 集合 ：无序，不可重复， 可使用for循环
mySet = {'j', 'a', 'y', 'j'}  # 输出可能为 {'a', 'j', 'y'}
mySet2 = set()  # 定义空集合
print(mySet)
# dict 字典： 类似于js的objct， pyton字典的key:value可以为任意类型（key类型不可以为字典）
