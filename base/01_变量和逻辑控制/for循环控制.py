'''
序列本质上是一个可以被迭代的对象
'''

str = 'i love you'
for char in str:
    # char是一个临时变量，用str中依次取出每一个字符
    print(char, end='')
print()
print('for循环结束了')

# sum = 0
# for num in range(1,51):
#     sum += num
# print(sum)

odd_sum = 0
for i in range(1,51):
    if i % 2 != 0:
        odd_sum += i
print(odd_sum)