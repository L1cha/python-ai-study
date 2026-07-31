def func2():
    return 1/0
def func1():
    func2()
def main():
    try:
        func1()
    except Exception as e:
        print(f'异常为：{e}')
if __name__ == '__main__':
    main()