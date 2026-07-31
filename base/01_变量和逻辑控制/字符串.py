# digits = '0123456789'
# print(digits[0:5:1])
# print(digits[0:5:2])
# print(digits[9])
# print(digits[:5])
# print(digits[6:])
# print(digits[:-1])
#
# index = 5
# str = 'photo.jpg'
# name = str[:5]
# suffix = str[5:]
# print(f'文件名是：{name},文件后缀是：{suffix}')
#
# massage = 'welcome to Python Programming, Python is great'
# sub_str = 'Python'
# position = massage.find(sub_str)
# if position == -1:
#     print(f'{sub_str}不在{massage}中')
# else:
#     print(f'{sub_str}在{massage}中，它的位置在{position}')
#
# file_name = input('请输入文件名：')
# dot_pos = file_name.find('.')
# if dot_pos == -1:
#     print('文件名输入错误')
# else:
#     print(f'找到.的位置，他在{dot_pos}')
#     print(f'文件名称为：{file_name[:dot_pos]}')
#     print(f'文件后缀为：{file_name[dot_pos:]}')

# # 字符串的替换.replace
# text = 'I love Java programming and Java is great'
# new_text = text.replace('Java','Python')
# print(new_text)
#
# # 字符串切割.split
# data_str = '2026.07.26'
# data_str1 = data_str.split('.')
# print(data_str1)
#
# # 邮箱切割
# email = 'user@example.com'
# parts = email.split('@')
# print(f'用户名为：{parts[0]}')
# print(f'邮箱后缀为：{parts[1]}')
#
# # 拼接字符串'连接符'.join()
# fruits = ['apple','banana','mango']
# lianjie = '-'.join(fruits)
# print(lianjie)

# import random
# length = 6
# index = ''
# uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# lowercase = 'abcdefghijklmnopqrstuvwxyz'
# digits = '0123456789'
# all_cases = uppercase + lowercase + digits
# all_cases_len = len(all_cases)
# rand_index = random.randint(0,all_cases_len-1)
# print(f'获取字符索引为{rand_index}')
# print(f'获取字符为{all_cases[rand_index]}')
# for i in range(length):
#     rand_index = random.randint(0, all_cases_len - 1)
#     print(f'获取字符索引为{rand_index}')
#     print(f'获取字符为{all_cases[rand_index]}')
#     index += all_cases[rand_index]
#
# print(index)

import random
length = 6
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'
all_cases = uppercase + lowercase + digits
all_cases_len = len(all_cases)
while True:
    code = ''
    for i in range(length):
        index = random.randint(0,all_cases_len-1)
        code += all_cases[index]

    has_digit = False
    has_letter = False

    for c in code:
        if '0' <= c <= '9':
            has_digit = True
        else:
            has_letter = True

    if has_digit and has_letter:
        break
print(f'验证码为：{code}')











