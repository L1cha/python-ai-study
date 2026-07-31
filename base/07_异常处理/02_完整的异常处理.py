with open('a3.txt','w',encoding='utf-8') as f:
    f.write('hello world')

def total_exp_deal(filename,mode,encoding='utf-8'):
    try:
        with open(filename,mode,encoding=encoding) as f:
            content = f.read()
    except FileNotFoundError:
        print('错误，文件不存在')
    except Exception as e:
        print(f'发生错误：{e}')
    else:
        print(f'读取内容{content}')
        print(f'文件读取成功，内容长度{len(content)}')
    finally:
        print('文件操作完成')
total_exp_deal('a2.txt','r')
total_exp_deal('a.txt','r')
total_exp_deal('a3.txt','r')