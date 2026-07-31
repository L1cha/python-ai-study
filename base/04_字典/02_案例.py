'''
给定一个字符串my_string，现在要求统计每个字符出现的次数:
形成结果: {'字符':出现次数,'字符2':次数}
例如: 'abcdecf' ==> {'a':1,'b':1,'c':2,'d':1,'e':1,'f':1}
实现思路
①定义一个字符串
②初始化空字典，来存储对应字符和出现次数
③循环遍历字符串中每个字符
④如果字符串已经在字典中，计数加1，如果不在，初始化计数1: 字典['key'] += 1
⑤输出统计每个字符出现的次数
'''
str = 'abcdecf'
num_dict = dict()
for char in str:
    if char not in num_dict:
        num_dict[char] = 1
        continue
    num_dict[char] += 1
for key, value in num_dict.items():
    print(f'{key}出现了{value}次')




'''
需求: 编写一个程序将字符串转换为字典 例如:输入: '8=Eight 9=Nine 10=Ten' 
输出: {'8': 'Eight', '9': 'Nine', '
'''

num_str = '8=Eight 9=Nine 10=Ten'
num_dict1 = dict()
pair = num_str.split(' ')
for part in pair:
    part1 = part.split('=')
    num_dict1[part1[0]] = part1[1]
print(num_dict1)
