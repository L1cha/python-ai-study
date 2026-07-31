'''
lambda表达式
'''

def func(str):
    return'hello'+str
fn = lambda str : 'hello' + str
print(fn('123'))

fn1 = lambda num1,num2:num1+num2
print(fn1(1,2))
fn2 = lambda num1,num2= 20:num1+num2
print(fn2(1))

print('-'*100)
def func_if(name):
    if name == 'a':
        return 1
    else:
        return 2
print(func_if('a'))
print(func_if('b'))

def func_if1(name):
    return 1 if name == 'a' else 2
print(func_if1('a'))
print(func_if1('b'))

fn = lambda name : 1 if name =='a' else 2
print(fn('a'))
print(fn('b'))

students = [
    {'name':'a', 'age':10},
    {'name':'b', 'age':20},
    {'name':'c', 'age':30},
]
print(students)
students.sort(key=lambda x:x['name'])
print(students)
students.sort(key=lambda x:x['age'])
print(students)