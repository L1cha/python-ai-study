zhengshu = int(input('请输入一个整数：'))
# if zhengshu%2==0:
#     print('这个整数是偶数')
# else:
#     print('这个整数是奇数')

result = '偶数' if zhengshu %2 == 0 else '奇数'
print(result)



# height = float(input('你的身高（m）是：'))
# weight = float(input('你的体重（kg）是：'))
#
# BMI = weight / (height * height)
#
# if BMI >= 28:
#     print('肥胖')
# elif BMI >= 24:
#     print('超重')
# elif BMI >= 18.5:
#     print('正常')
# else:
#     print('偏瘦')

# cost = float(input('你的消费金额（元）是：'))
# dengji  = input("用户状态（会员/非会员）：")
# if dengji == "会员":
#     if cost >= 200:
#         shijihuafei = cost - 50
#     else:
#         shijihuafei = cost *0.9
# else:
#     shijihuafei = cost
# print(f'你最终消费：{shijihuafei:.1f}')