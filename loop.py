# for in 循环
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum) # 55

# range()函数,可以生成一个整数序列
print(range(10)) # range(0,10)
# list()函数 可以转换range()为list。比如range(10)生成的序列是从0开始小于10的整数
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sum2 = 0
for x in range(101):
    sum2 = sum2 + x
print(sum2) #5050

# while循环
sum3 = 0
n = 99
while n > 0:
    sum3 = sum3 + n
    n = n - 2
print('while循环结果为%s' % sum3)

# break 语句
n = 1
while n <= 10:
    if n > 4: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 语句
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

