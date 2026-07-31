"""
格式化输出
通过字符串和变量拼接的方式就叫做格式化输出
方式一 f-string
print(f'字符串{变量名}‘）
"""
#对整数进行补零，控制整数位数
num = 1
print(f"学号：{num:06d}")

# 基础用法
name = "licha"
age = 23
score = 96.77777
print(f'姓名为:{name},年龄为:{age},学分为:{score}')
#对小数进行控制，保留两位小数
print(f'姓名为:{name},年龄为:{age},学分为:{score:.2f}')
