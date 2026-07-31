'''
演示文件读写
'''

'''
1. file = open(文件路径,模式,编码)
file是文件对象，里面包含了文件描述符
模式 r 只读，如果文件不存在则报错
w 只写，如果文件不存在则创建，创建则清空并且覆盖写
a 追加，如果文件不存在则创建，存在则追加
2 file.read()读取  file.write(内容)
3 file.close()
'''

'''
相对路径：以.或者..开始的路径表示相对路径
.表示当前目录， ..表示上一级目录
./a.txt 表示当前目录下的a.txt文件
../b.txt表示上一级目录的b.txt文件
绝对路径：linux环境下以/（根目录开始）的路径就是绝对路径
例：E:\\ProgramData\\anaconda3

'''
with open('./b.txt','w', encoding = 'utf-8') as f:
    f.write('我是qqs，请给我掏钱\n我需要三个忆')

# 读取文件内容
with open('./b.txt','r', encoding = 'utf-8') as f:
    # 读取所有行，每一行数据是列表的一个元素
    data_list = f.readlines()
    print(data_list)

with open('./b.txt','r', encoding = 'utf-8') as f:
    while True:
        # 按行读取，一次读取一行
        line = f.readline()
        if line:
            print(line.rstrip())
            continue
        # 走到这里说明数据为空
        break

with open('./b.txt','r', encoding = 'utf-8') as f:
    # for循环冲文件读取中一次读取一行
    for line in f:
        print(line.rstrip())

lines = ['第一行\n','第二行\n','第三行\n']
with open('./c.txt','w', encoding = 'utf-8') as f:
    f.writelines(lines)
with open('./c.txt','r', encoding = 'utf-8') as f:
    for line in f:
        print(line.rstrip())