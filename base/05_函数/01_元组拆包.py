'''
元组拆包
'''

tuple1 = ('小明',20,30000)

# 拆包
name, age, salary = tuple1
print(name)
print(age)
print(salary)
print(f'{name},{age},{salary}')

# 自动拆包
a, b = (10, 20)
print(a, b)

# 两个变量交换
c1 = '2'
c2 = '3'

t = c1
c1 = c2
c2 = t
print(f'c1为{c1}, c2为{c2}')

# 快速交换
c2, c1 = c1, c2
print(f'c1为{c1}, c2为{c2}')

