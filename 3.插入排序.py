# 算法思想: 遍历数组,将当前值向前遍历插入对应位置
# 时间复杂度: o(n^2)

import random
lst = []

for i in range(10):
    lst.append(random.randint(0,99))


def sort(lst):
    l = len(lst)
    for i in range(l):
        value = lst[i]
        position = i
        while position>0 and lst[position-1]>value:
            lst[position] = lst[position-1]
            position-=1

        lst[position] = value
    
    return lst

print("原数组:",lst)
print("排序后",sort(lst))