'''
字典
'''

person = {'name':'小明',
          'age':18,
          'sex':'男'}
print(person['name'])
print(person['age'])
print(person)
print(type(person))

# 构建空字典
dict1 = {}
print(dict1)
print(type(dict1))
dict2 = dict()
print(dict2)
print(type(dict2))

print('-'*100)

for key in person:
    print(key)
    print(person[key])

# 新增操作
person['salary'] = 30000
print(person)
#修改
person['age'] = 25
print(person)
del person['age']
print(person)
#字典清空
person.clear()
print(person)

#查找一个不存在的key
person = {'name':'小明',
          'age':18,
          'sex':'男'}
# 获取字典所有的key
print(person.keys())
# 遍历
for key in person.keys():
    print(key)
print('-'*100)
# 获取字典中所有的values，将字典中的value构成序列返回
# 遍历
print(person.values())
for value in person.values():
    print(value)
print('-'*100)

# 获取字典中所有的items，将字典中的item构成序列返回
print(person.items())
for item in person.items():
    print(item)
    print(item[0])
    print(item[1])
    print('*'*100)
    # 元组拆包 key接受item[0],value接受value[1]
    key, value = item
    print(key)
    print(value)