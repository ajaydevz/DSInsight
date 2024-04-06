arr = [34,45,65,43,56,66,52]
x = 56

def binarysearch(arr,x):
    low = 0
    high = len(arr) - 1

    while low <= high:

        mid  = (low+high)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] <= x:
            low = mid+1
        else:
            high = mid-1

    return -1

result = binarysearch(arr,x)

if (result == -1):
    print("element not found")
else:
    print("element found at index",result)

