arr = [12,34,54,64,33,65,23,21]
x = 65

def linearsearch(arr,x):
    n = len(arr)
    for i in range(0,n):
        if arr[i] == x:
            return i
    return -1

result = linearsearch(arr,x)

if (result == -1):
    print("elment not found")
else:
    print(f"the element present at inex: {result} ")



