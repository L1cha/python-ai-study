'''
函数用法
'''

'''
函数先定义再调用
'''

def size(num1, num2):
    jia = num1 + num2
    jian = num1 - num2
    cheng = num1 * num2
    chu = 0
    if num2 != 0:
        chu = num1 / num2
    return jia, jian, cheng, chu

jia, jian,cheng, chu = size(3,4)
print(jia, jian, cheng, chu)