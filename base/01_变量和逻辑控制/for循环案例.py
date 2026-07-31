'''
案例：用for循环实现用户登录
① 输入用户名和密码
② 判断用户名和密码是否正确（username='student'，password='python123'）
③ 登录仅有2次机会，超过2次会提示“登录失败，次数已用完”
分析：用户登陆情况有3种:
① 用户名错误(此时便无需判断密码是否正确) -- 登陆失败
② 用户名正确 密码错误 --登陆失败
③ 用户名正确 密码正确 --登陆成功
'''

# for i in range(2):
#     username = input('请输入用户名：')
#     pwd = input('请输入密码：')
#     if username == 'student':
#         if pwd == 'python123':
#             print(f'用户名正确 密码正确 --登陆成功')
#             break
#         else:
#             print(f'用户名正确 密码错误 -- 登陆失败')
#             continue
#     print(f'用户名错误 -- 登陆失败')

for i in range(2):
    username = input('请输入用户名：')
    pwd = input('请输入密码：')
    if username == 'student' and pwd == 'python123':
        print(f'用户名正确 密码正确 --登陆成功')
        break
    elif username != 'student':
        print(f'用户名错误 -- 登陆失败')
    else:
        print(f'用户名正确 密码错误 -- 登陆失败')
else:
    print(f'登录失败，次数已用完')