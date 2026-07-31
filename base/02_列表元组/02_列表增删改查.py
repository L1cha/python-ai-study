'''
列表的查找
'''

'''
列表名[下标] 获取指定下标得元素
count() 统计指定数据在当前列表中出现得次数
index() 获取指定数据所在位置的下标
in 判断在不在，在就返回
not in 判断不在，不在返回
'''

# 定义列表
name_list = ['小明','x','b','z','c','v','b','g']
index = name_list.index('x')
print(index)

count = name_list.count('b')
print(count)

if 'x' in name_list:
    print('x在名字列表中')
else:
    print('x不在名字列表中')

if '2' not in name_list:
    print('2不在名字列表中')
else:
    print('2在名字列表中')

'''
append() 在列表后面追加元素
extend() 在列表结尾追加元素
insert() 插入
'''

name_list2 = ['a','s']
name_list.extend(name_list2)
print(name_list)

name_list.insert(3,'w')
print(name_list)

name_list.append('0')
print(name_list)

print('-------------------------------')
list1 = [1,2,3,4]
list2 = [5,6,7,8]
# list1.extend(list2)
# print(list1)
list3 = list1 + list2
print(list3)

print('-'*50)
# 元素删除
del list3[-1]
print(list3)
del_num = list3.pop() #列表.pop() 是有返回值的
print(f'被删除的元素是：{del_num}')
print(list3)
del_num = list3.pop(4)
print(f'删除的元素是{del_num}')
print(f'list3 is {list3}')

'''
列表更改
'''
name_list[0] = '大明'
print(name_list)

print('reverse用法')
list3.reverse()
print(list3)

print('sort用法')
list3.sort()
print(list3)

print('reverse反转')
list3.sort(reverse=True)
print(list3)

print('-'*100)
'''
列表嵌套
'''
class1 = ['1','2','3']
class2 = ['a','b','c']
class3 = ['A','B','C']
classes = [class1,class2,class3]
print(classes)
print('-'*100)

for c in classes:
    print(c)
    for d in c:
        print(d)
print('-'*100)

# 断言
assert classes[0][0] == '1'
print(classes[0][0])