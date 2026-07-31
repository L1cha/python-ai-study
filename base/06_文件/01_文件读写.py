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
file_w = open('./a.txt','w', encoding = 'utf-8')
# read()默认对出所有内容，也可以指定读取的大小read(1024)
# write返回实际写入文件的字符数
data = file_w.write('我是qqs，请给我掏钱')
print(data)
file_w.close()

file_r = open('./a.txt','r', encoding = 'utf-8')
# read()默认对出所有内容，也可以指定读取的大小read(1024)
data = file_r.read()
print(data)
file_r.close()

file_w = open('./a.txt','a', encoding = 'utf-8')
# read()默认对出所有内容，也可以指定读取的大小read(1024)
data = file_w.write("如果如果可以的话请给我三个亿\n"
                    '我很想要三个忆')
print(data)
file_w.close()