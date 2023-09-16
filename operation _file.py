# 操作文件
# 读 read
import time

f = open("D:/testPython.txt", 'r', encoding='UTF-8')
# print(f.read(10))
# print(f.readline())  # 每次读取会接上次读取的进度
for p in f:  # for循环每次读取一行
    print(p)
lines = f.readlines()  # 返回一个存储每一行的列表
print(lines, 'l')
f.close()  # 停止占用文件

# 使用 with open 来打开文件, 会在代码段执行完毕后自动关闭文件.close()
with open("D:/testPython.txt", 'r', encoding='UTF-8') as f2:
    for row in f2:
        print(row)
# 写 write 如果没有文件则创建,如果有则会清空文件内容
f3 = open("D:/testPython2.txt", 'w', encoding='UTF-8')
f3.write('测试python写入')  # 先写在内存中并没有实际写在文件内
f3.flush()  # 正式写入文件中
f3.close()  # 关闭占用前,会先自动调用flush()
# time.sleep(1000)
with open("D:/testPython3.txt", 'w', encoding='UTF-8') as f4:
    f4.write('我是用python代码生成的写入的文件')
# 追加 add
with open("D:/testPython3.txt", 'a', encoding='UTF-8') as f5:
    f5.write('我是在文件中追加的内容')  # 默认在尾部追加
    f5.write('\n我是在文件中追加的内容')  # 换行
