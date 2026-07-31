"""
💡 题目：给定一个连续递增的整数列表，找出中断的位置。
例如：[1, 2, 3, 5, 6, 8] 中，3→5 断了，6→8 也断了。
"""
list =  [1, 2, 3, 5, 6, 8]
last = None
for item in list:
    if last is None:
        last = item
    else:
        if item != last+1:
            print(f'{last}到{item}断了')
        last = item

for i in range(1,len(list)):
    if list[i] != list[i-1]+1:
        print(f'{list[i-1]}到{list[i]}断了')
"""
💡 题目：一个数组中除了两个数字只出现一次外，其他数字都出现两次。
       找出这两个只出现一次的数字。
输入: [4, 1, 2, 1, 2, 3, 5, 5]
输出: 3 和 4

思路：
1. 准备集合A和列表B，集合A用来存储出现的数字，集合B用来记录只出现过1次的数字
2. 将出现的数字和集合A判断，如果集合A中有数字，说明这个数字出现过，将数字从集合B
中删除。
如果A中没有这个数字，说明数字没出现过，将数字放入集合A和集合B
3. 最后循环结束，打印集合B，就是只出现一次的数字了
"""
list = [4, 1, 2, 1, 2, 3, 5, 5]
set_a = set()
set_b = set()
for i in list:
    if i not in set_a:
        set_a.add(i)
        set_b.add(i)
        continue
    else:
        set_b.remove(i)
print(f'出现1次的数字为：')
for i in set_b:
    print(i,end='\t')
print()
"""
💡 题目：统计列表中每个数字出现的次数，并按数字大小排序输出。
输入: [4, 2, 2, 8, 3, 3, 1, 4, 3]
"""
num_list = [4, 2, 2, 8, 3, 3, 1, 4, 3]
num_list1 = []
for i in sorted(set(num_list)):
    print(f'数字{i}出现{num_list.count(i)}次')
#     num_list1.append(i)
# num_list1.sort()
# print(f'由低到高顺序为：{num_list1}')

"""
💡 题目：判断一个列表中的数字是否能组成连续序列。
例如：[4, 2, 3, 1] → True（可以重排成 [1,2,3,4]）
      [5, 3, 2, 6] → False（范围是 2~6，缺了 4）
"""
# num_list = [4, 2, 3, 1]
# for i in range(len(num_list)):
#     TF = False
#     if num_list[i]-1 or num_list[i]+1 in num_list:
#         TF = True
#         continue
# if TF:
#     print(f'{num_list}列表中的数字能组成连续序列')
# else:
#     print(f'{num_list}列表中的数字不能组成连续序列')

num_list = [4, 2, 3, 1]
is_continuous = True
for i in range(min(num_list),max(num_list)+1):
    if i not in num_list:
        is_continuous = False
        print(f'该队列不能组成连续序列，缺失{i}')
        break

if is_continuous:
    print(f'该列表中的数字能组成连续序列，为{sorted(num_list)}')

"""
💡 题目：给你一个 1 到 n 的数组，但缺少了一些数字。
       找出所有 1~n 范围内消失的数字。
输入: [4, 3, 2, 7, 8, 2, 3, 1]  (n=8，但数组里缺了 5, 6)
"""
num_list = [4, 3, 2, 7, 8, 2, 3, 1]
set_num = set(num_list)
missing_num = []
for i in range(1,max(num_list)+1):
    if i not in set_num:
        print(i)
        missing_num.append(i)
print(f'数组中缺{missing_num}')

