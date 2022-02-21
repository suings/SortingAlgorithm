# 算法思想: 1.分割 2.归并
# 时间复杂度: 

import random
lst = []

for i in range(10):
    lst.append(random.randint(0,99))

def meger(arr,l,mid,r):
    l1 = arr[l:mid+1]+[float("inf")]
    l2 = arr[mid+1:r+1]+[float("inf")]
    i,j = 0,0
    for k in range(l,r+1):
        if l1[i]<l2[j]:
            arr[k] = l1[i]
            i+=1
        else:
            arr[k] = l2[j]
            j+=1
def MegerSort(arr,l,r):
    if l<r:
        mid = l+ (r-l)//2
        MegerSort(arr,l,mid)
        MegerSort(arr,mid+1,r)

        meger(arr,l,mid,r)
def sort(lst):
    l = len(lst)

    MegerSort(lst,0,l-1)
    return lst

print("原数组:",lst)
print("排序后",sort(lst))