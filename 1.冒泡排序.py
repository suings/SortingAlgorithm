# 算法思想: 比较相邻2个元素,如果顺序错误则交换
# 时间复杂度为o(N^2)
# 最好情况下时间复杂度为o(N)

import random
lst = []

for i in range(20):
    lst.append(random.randint(0,999))


def sort(lst):
    flag = True
    while flag:
        flag = False
        for index,value in enumerate(lst[:-1]):
            if lst[index] > lst[index+1]:
                tmp = lst[index]
                lst[index] = lst[index+1]
                lst[index+1] = tmp
                flag = True
    return lst

print("原数组:",lst)
print("排序后",sort(lst))