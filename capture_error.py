# 捕获异常
# f = open('./error.txt', 'r', encoding='UTF-8') # 报错
# 通过异常捕获来防止报错
# 捕获所有异常
try:
    1 / 0
    print(name)
    f = open('./error.txt', 'r', encoding='UTF-8')
except Exception as e:
    print(e)
    f = open('./error.txt', 'w', encoding='UTF-8')
# 捕获指定的异常
try:
    # 1/0
    print(name)
except NameError as e:  # 只能捕获变量未定义相关的error
    print(f'捕获到的异常{e}')
# 捕获多个指定异常
try:
    1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print(f'捕获到的异常{e}')
# 异常else: 如果没有异常会执行else分支
try:
    f = open('./error.txt', 'r', encoding='UTF-8')
except (NameError, ZeroDivisionError) as e:
    print(f'捕获到的异常{e}')
else:
    print('很高兴没有异常!!')
# 异常finally: 声明后一定会执行
try:
    f = open('./error.txt', 'r', encoding='UTF-8')
except (NameError, ZeroDivisionError) as e:
    print(f'捕获到的异常{e}')
else:
    print('很高兴没有异常!!')
finally:
    print('我是必须会执行的!')


# 异常的传递
# 捕获函数调用栈中的所有异常
def test_error_transmit1(a=0):
    name = 1 / a  # 除以0的异常代码
    return name


def test_error_transmit2(a):
    test_error_transmit1(0)
    return 1 + a


def test_error_transmit():
    test_error_transmit2(1)
    # try:
    #     test_error_transmit2(1)
    # except Exception as e2:
    #     print(f'异常传递测试捕获到的异常{e2}')


try:
    test_error_transmit()
except Exception as e3:
    print(e3)
