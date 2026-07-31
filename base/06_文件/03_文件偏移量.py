'''
文件偏移量
'''

'''
演示文件偏移操作
'''
with open('./a.txt','r', encoding = 'utf-8') as f:
    # tell()获取当前文件指针的位置,这里是字节偏移量
    print(f'文件开始的偏移量', f.tell())
    # 读取5个字符
    content = f.read(5)
    print(f'读取的内容：{content}')
    # 中文可能是3~6个字节
    print(f'文件开始的偏移量', f.tell())
    #回到头部
    f.seek(0)

    content = f.read(5)
    print(f'读取的内容：{content}')

    f.seek(6,0)
    content = f.read(5)
    print(f'读取内容：{content}')

    # 将文件指针移动到末尾，2表示文件末尾，1表示当前位置
    f.seek(0,2)
    # 因为文件指针已经移动到末尾，所以f.tell获取的是文件大小
    file_size = f.tell()
    print(f'文件总大小为：{file_size}')

