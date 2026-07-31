'''
列表的初步使用
'''

fruits = ['apple','banana','mango']
print(fruits)
print(type(fruits))

print(fruits[0])
print(fruits[-1])
print('--------------------------------------')
for name in fruits:
    print(name)
print('--------------------------------------')
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1