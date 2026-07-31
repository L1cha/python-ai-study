# r = 1
# while r < 10:
#     l =9
#     while l >0:
#         if r <=l:
#             x = r * l
#             print(f'{r}*{l}={x}',end=' ')
#             l -= 1
#         else:
#             break
#     r += 1
#     print()

# r = 1
# while r < 10:
#     l =9
#     while l >= r:
#         print(f'{r}*{l}={r * l}',end='\t')
#         l -= 1
#     r += 1
#     print()

print('#'*50)
row = 1
while 0 < row < 10:
    col =1
    while col <= row:
        print(f'{col}*{row}={row * col}',end='\t')
        col += 1
    row += 1
    print()

print('#'*50)

for i in range(1,10):
    for j in range(1,5):
        if i >= j:
            print(f'{j}*{i}={i * j}',end='\t')
    print()

print('#'*50)

for i in range(1,10):
    for j in range(1,i+1):
        print(f'{j}*{i}={i * j}',end='\t')
    print()

print('#'*50)



