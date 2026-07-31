import random
answer = random.randint(1,20)
# 初级编程
# while True:
#     guess = int(input('请输入猜测的数字：'))
#     if guess == answer:
#         print('恭喜你猜对了！')
#         break
#     if guess > answer:
#         print('你猜大了，请继续。。。')
#     else:
#         print('你猜小了，请继续。。。')

'''
防御式编程
不要相信用户的输入，对输入的数据，以及传递函数的参数等，都进行判断。
将符合条件的提前处理，处理完成后提前跳过后续的逻辑。
防御式编程的有点：
1.让代码更加简洁，可以提前处理判断的情况
2.可以配合分治思想，实现递归调用
'''

#防御式编程
while True:
    guess = int(input('请输入猜测的数字：'))
    if guess == answer:
        print('恭喜你猜对了！')
        break
    if guess > answer:
        print('你猜大了，请继续。。。')
        continue
    # 走到这里完全肯定是猜小了
    print('你猜小了，请继续。。。')