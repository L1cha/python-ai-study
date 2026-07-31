'''
异常演示
'''

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('除数不能为0！')
        return None
    except TypeError:
        print('参数类型错误！')
        return None

print(divide(10,2))
divide(10,0)
divide(10,'a')

with open('./a.txt','w',encoding='gbk') as f:
    f.write('hello world')
    f.write('你好')

def read_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print('错误，文件不存在')
    except UnicodeDecodeError:
        print('错误，编码错误')
    except PermissionError:
        print('错误，权限错误')

read_file('./a.txt')

def read_file2(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            content = f.read()
            print(content)
    except (FileNotFoundError,PermissionError,UnicodeDecodeError):
        print('错误文件访问错误')

read_file2('ab.txt')
read_file2('a.txt')

def read_file3(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            content = f.read()
            print(content)
    except Exception as e:
        print(f'异常的类型为：{type(e)}')
        print(f'异常信息：{e}')

read_file3('a.txt')