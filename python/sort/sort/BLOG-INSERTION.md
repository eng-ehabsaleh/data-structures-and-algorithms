### Algorithm

_To sort an array of size 5 : 1: Iterate from arr[1] to arr[5] over the array. 2: Compare the current element to its next element . 3: If the current element is smaller than its next element , compare it to the elements before. Move the greater elements one position up to make space for the swapped element._

- Pseudocode :

```
InsertionSort(int[] arr)

FOR i = 1 to arr.length

  int j <-- i - 1
  int temp <-- arr[i]

  WHILE j >= 0 AND temp < arr[j]
    arr[j + 1] <-- arr[j]
    j <-- j - 1

  arr[j + 1] <-- temp
```

- Code:

```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = temp
    return arr
```

**_Trace:_**

**@ the Beginning**

```
[8,4,23,42,16,15]
```

- pass1: For the first itteration , current value = 4 , j = 0 , i = 1 then it go to while loop and check if the index greater or equal to 0 and the value of i index smaller than j index value , it's true so the value of j index will be assigned to the next place , then the j index decrement by one ,then it will check the condition in the while loop , it's false so it will change the value of index j to be equal to the current value , like this we switch the first two values of the array .

```
[4,8,23,42,16,15]
```

- pass 2 : For the secound itteration , current value = 23 , j = 1 , i = 2 then it go to while loop and check if the index greater or equal to 0 and the value of i index smaller than j index value , it's false so it will keep every thing the same and just change the value of index j to be equal to the current value .

```
[4,8,23,42,16,15]
```

- pass 3 : For the third itteration , current value = 42 , j = 2 , i = 3 then it go to while loop and check if the index greater or equal to 0 and the value of i index smaller than j index value , it's false so it will keep every thing the same and just change the value of index j to be equal to the current value .

```
[4,8,23,42,16,15]
```

- pass 4 : For the fourht itteration , current value = 16 , j = 3 , i = 4 then it go to while loop and check if the index greater or equal to 0 and the value of i index smaller than j index value , it's true so the value of j index will be assigned to the next place , then the j index decrement by one ,then it will check the condition in the while loop , j = 2 , current = 16 , arr[2] = 23 , it's true so the value of j index will be assigned to the next place , then the j index decrement by one ,then it will check the condition in the while loop , j = 1 , current = 16 , arr[1] = 8 , it's false o it will keep every thing the same and just change the value of index j to be equal to the current value . untile now my array look like :

```
[4,8,16,23,42,15]
```

- pass 5 : For the fifth itteration , current value = 15 , j = 4 , i = 5 then it go to while loop and check if the index greater or equal to 0 and the value of i index smaller than j index value , it's true so the value of j index will be assigned to the next place , then the j index decrement by one ,then it will check the condition in the while loop , j = 3 , current = 15 , arr[3] = 23 it's true so the value of j index will be assigned to the next place , then the j index decrement by one ,then it will check the condition in the while loop , j = 2 , current = 15 , arr[2] = 16 ,it's true so the value of j index will be assigned to the next place , then the j index decrement by one ,then it will check the condition in the while loop , j = 1 , current = 16 , arr[1] = 8 ,it's false o it will keep every thing the same and just change the value of index j to be equal to the current value . untile now my array look like :

```
 [4,8,15,16,23,42]
```
