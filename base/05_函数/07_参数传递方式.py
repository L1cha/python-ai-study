'''
参数传递的几种方式
'''

'''
位置传参
'''
def pick_item(user, item, num):
    '''
    捡物品的函数
    :param user: 捡东西的人
    :param item: 捡什么东西
    :param num: 捡起物品的数量
    :return: str
    '''
    return f'用户【{user}】捡起【{num}】个物品【{item}】'
print(pick_item('理查','理查德米勒',3))

'''
关键字传参
调用方式
函数名(形参1=实参1,形参2=实参2,...)
'''
print(pick_item(user='理查',item='理查德米勒',num=6))

'''
默认值参数
函数定义时设定一个默认值
'''
def hard_challenge(user,item,num=1):
    '''
    演示游戏中深渊挑战掉落
    :param user: 用户名
    :param item: 物品
    :param num: 数量
    :return: str
    '''
    return f'用户【{user}】挑战深渊掉落物品【{item}】,数量为【{num}】'
print(hard_challenge('licha','python'))
print(hard_challenge('licha','python',3))

'''
不定长参数
'''

def hard_challenge_args(*args):
    '''
    深渊挑战
    :param args:是一个元组
    :return: str
    '''
    return f'用户【{args[0]}】挑战深渊掉落物品【{args[1]}】,数量为【{args[2]}】'
# 将下述参数打包成元组
print(hard_challenge('licha','python',3))

'''
不定长关键字参数
'''
def hard_challenge_kwargs(**kwargs):
    '''
    深渊挑战
    :param kwargs: 是一个字典
    :return: str
    '''
    return f'用户【{kwargs['name']}】挑战深渊掉落物品【{kwargs['item']}】,数量为【{kwargs['num']}】'
# 函数调用时自动将下述转为字典
print(pick_item(user='理查',item='理查德米勒',num=6))

'''
万能函数
def func(*args, **kwargs):
    pass
'''
def func(*args, **kwargs):
    print('元组信息如下')
    for item in args:
        print(item)
    print('字典信息如下')
    for i, j in kwargs.items():
        print(f'{i}: {j}')

tuple_data = (1,2,3,4,5)
dict_data = {'a':1,'b':2,'c':3,'d':4}
#将(1,2,3,4,5)打包成i一个元组((1,2,3,4,5),)
func(tuple_data)
#将{'a':1,'b':2,'c':3,'d':4}打包成元组({'a':1,'b':2,'c':3,'d':4},)
func(dict_data)
# *tuple_data将(1,2,3,4,5)拆包，拼成多个位置参数1，2，3，4，5
# 参数1，2，3，4，5会被自动打包成元组传递给args,所以args=(1,2,3,4,5)
func(*tuple_data)
# **dict_data是将字典拆包，拆成关键字传参a=1,b=2...
# 再将a=1,b=2...进行打包，生成{'a':1,'b':2,'c':3,'d':4}赋值给kwargs
func(**dict_data)

func(1,2,3,4,5 ,a=1,b=2,c=3,d=4)
