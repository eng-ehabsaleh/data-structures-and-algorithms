def merge_sort(arr):
    if len(arr) > 1:
        mid = int(len(arr)/2)
        Left = arr[:mid]
        Right = arr[mid:]
        merge_sort(Left)
        merge_sort(Right)
        return merge(Left, Right, arr)
        


    # return arr
def merge(Left, Right, arr):
        i = 0
        j = 0
        k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1

        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1
            
        return arr







print(merge_sort([8,4,23,42,16,15]))




