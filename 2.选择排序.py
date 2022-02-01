# 算法思想: 在未排序队列取最小值,将其放到排序队列尾部
# 时间复杂度: 固定o(N^2)

import random
lst = []

for i in range(10):
    lst.append(random.randint(0,99))


def sort(lst):
    l = len(lst)

    for i in range(0,l):
        min_index = i
        min_value = lst[i]
        for j in range(i,l):
            if lst[j] < min_value:
                min_index = j
                min_value = lst[j]
        
        tmp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = tmp
    


    return lst

print("原数组:",lst)
print("排序后",sort(lst))