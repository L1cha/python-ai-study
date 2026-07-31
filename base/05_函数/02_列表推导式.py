'''
演示列表推导式
'''

'''
变量名 = [表达式 for 变量 in 列表]
变量名 = [表达式 for 变量 in 列表 if 条件]
变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]
'''

num_list = [i for i in range(10)]
print(num_list)

num_list = [i for i in range(10) if i % 2 ==0]
print(num_list)

num_list = [(i,j) for i in range(3) for j in range(4)]
print(num_list)

'''
生成 2×3 的棋盘坐标（从 (1,1) 开始）
'''
num_list = [(i,j) for i in range(1,3) for j in range(1,4)]
print(num_list)

num_list = [(i,j) for i in range(1,4) for j in range(1,4) if i==j]
print(num_list)

num_list = [(i,j) for i in range(1,5) for j in range(1,5) if i % 2 == 0 and j % 2 == 0]
print(num_list)

num_list = [(i,j) for i in range(1,10) for j in range(1,10) if i>=j]
print(num_list)

'''
案例一：使用列表推导式生成平方数集合
例如, 用户输入10, 表示要生成 1~10的每一个数字的平方的集合
'''
n = int(input('请输入一个正整数：'))
num_list = [(i*i) for i in range(1,n+1)]