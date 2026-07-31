'''
变量 = input(字符串)
input是一个阻塞型函数
字符串是可选的，用来提示用户内容
'''

# name = input('用户名字为：')
# pwd = input('用户密码为：')
# print(f'用户姓名为：{name},用户密码为：{pwd}')
# age = input('请输入年龄')
# print(f'用户年龄为：{age}，其数据类型为{type(age)}')

price = input('请输入商品价格（元）')
count = input('请输入商品数量（个）')
total_price = int(price) * int(count)
print(total_price)