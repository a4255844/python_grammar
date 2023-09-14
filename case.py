import random

# 99乘法表
for x in range(1, 10):
    row = ''
    for j in range(1, x + 1):
        row += f'{x} * {j}={x * j}  '
    print(row)
# 发工资案例
money = 10000
for x in range(1, 21):
    performance = random.randint(0, 10)
    if (performance < 5):
        print(f'{x}号员工,绩效分为{performance}, 不合格,不发工资')
    else:
        money -= 1000
        print(f'{x}号员工,绩效分为{performance}, 合格,发工资1000,账户余额{money}')
        if money < 1000:
            print(f'发至第{x}位员工,本轮发工资已结束')
            break
