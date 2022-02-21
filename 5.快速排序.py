def quick_sort(arr,left=None,right=None):
    left = left if left != None else 0
    right = right if right != None else len(arr)-1

    if left<right:
        index = partition(arr,left,right) 
        quick_sort(arr,0,index-1)
        quick_sort(arr,index+1,right)
    return arr
def partition(arr,left,right):
    pivot = left
    index = left+1
    i = index

    while i <=right:
        if arr[i]<arr[pivot]:
            swap(arr,i,index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


arr = [2,3,1,1,2,5,7,2,3,2]
arr = quick_sort(arr)
print(arr)