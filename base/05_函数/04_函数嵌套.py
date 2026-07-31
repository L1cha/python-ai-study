def func_a():
    return 1
def func_b():
    return func_a()
print(func_b())

'''
递归，一个函数自己调用自己 就是递归
必要条件 要有结束条件
'''

def func_c(num: int):
    if num <= 1:
        return 1
    return num * func_c(num - 1)
print(func_c(3))

'''
分治思想
将一个大问题，拆成相似的小问题，逐个击破
'''
'''
需求：有一个小青蛙，每次可以跳1个台阶，或者跳2个台阶，总共10个台阶，问有多少种走法
思路：
1. 当仅有一个台阶，那么就是1中走法，fn(1) = 1
2. 当有两个台阶，那么有两种走法,f(2) = 2
3. 当有三个台阶， 那么有这些走法 f(3) = f(2) + f(1)
4. 如果有四级台阶， 那么走法为f(4) = f(3) + f(2)
5. 如果有n级台阶，那么走法为f(n) = f(n-1) + f(n-2)
'''

def fn_steps(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fn_steps(n - 1) + fn_steps(n - 2)
print(fn_steps(10))

def hannuota(n,a,b,c):
    if n == 1:
        print(f'{a}👉{c}')
        return
    hannuota(n-1,a,c,b)
    print(f'{a}👉{c}')
    hannuota(n-1,b,a,c)
hannuota(4,'a','b','c')
