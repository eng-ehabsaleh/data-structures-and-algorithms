## Pseudo Code:

```
ALGORITHM QuickSort(arr, left, right)
if left < right
// Partition the array by setting the position of the pivot value
DEFINE position <-- Partition(arr, left, right)
// Sort the left
QuickSort(arr, left, position - 1)
// Sort the right
QuickSort(arr, position + 1, right)
ALGORITHM Partition(arr, left, right)
// set a pivot value as a point of reference
DEFINE pivot <-- arr[right]
// create a variable to track the largest index of numbers lower than the defined pivot
DEFINE low <-- left - 1
for i <- left to right do
if arr[i] <= pivot
low++
Swap(arr, i, low)
     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1
ALGORITHM Swap(arr, i, low)
DEFINE temp;
temp <-- arr[i]
arr[i] <-- arr[low]
arr[low] <-- temp
```

## Code :

```
def quickSort(arr, L, R):
if L < R :
position_pivot = Partition(arr,L, R)
quickSort(arr, L, position_pivot - 1)
quickSort(arr, position_pivot + 1, R)
return(arr)
def Partition(arr, L, R):
pivot = arr[R]
low = L - 1
for i in range(L,R) :
if arr[i] <= pivot:
low +=1
arr[low],arr[i] = arr[i], arr[low]
arr[low + 1], arr[R] = arr[R], arr[low+1]
return(low + 1)
arr = [8,4,23,42,16,15]
n = len(arr)
print(quickSort(arr, 0, n-1))
```

## Trace:

    pass1:

-   Pass 1 of quick Sort
    In the first pass through of the merge sort, divide the array into 2 arrays, define a pivot, and put the numbers above it on the right and on the left put the smaller numbers. [8,4,23,42,16,15]=> pivot = 15, left array = [8,4], right array = [16,23,42]

    Pass 2:

-   Pass 2 of quick Sort
    repeated the first step with new pivot which is the last element

    Pass 3:

-   Pass 3 of quick Sort
    The third pass merge the entire new array and return it. [4,8,15,16,32,42] Efficiency
