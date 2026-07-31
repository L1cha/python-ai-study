# 定义空集合
empty_set = set()
print(empty_set)
print(type(empty_set))

# 定义空字典
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

name_set = {'a', 'b', 'c','a', 'b', 'c'}
print(name_set)
print(type(name_set))

name_set = {'大明', '大红', '大张'}
name_set.add('大纲')
print(name_set)
name_set.remove('大纲')
print(name_set)

if '大明' in name_set:
    print(f'大明在集合中')
else:
    print('大明不在集合中')