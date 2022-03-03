def quick_sort(arr, L, R):
    if L < R :
        position_pivot = Partition(arr,L, R)
        quick_sort(arr, L, position_pivot - 1)
        quick_sort(arr, position_pivot + 1, R)
    return(arr)

def Partition(arr, L, R):
    pivot = arr[R]
    low = L - 1
    for i in range(L,R) :
        if arr[i] <= pivot:
            low +=1
            swap(arr, i, low)
    swap(arr, R, low +1)
    return(low + 1)

def swap(arr , i , low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
    
arr = [8,4,23,42,16,15]
n = len(arr)

print(quick_sort(arr, 0, n-1))
