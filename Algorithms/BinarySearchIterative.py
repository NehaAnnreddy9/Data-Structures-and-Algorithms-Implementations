#Binary Search using Iterative method-
def BinarySearchIter(arr,low,high,val):
    if len(arr) == 0: return -1
    while(low <= high):
        mid = (low+high)//2
        if(arr[mid] == val): return mid
        elif(arr[mid] > val): high = mid - 1
        elif(arr[mid] < val): low = mid + 1
    return -1
