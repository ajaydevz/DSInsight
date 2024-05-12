# remove duplicate

nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
result = []
for i in nums:
    if i not in result:
        result.append(i)
        
print(result)

print(list(set(nums)))

def remove_duplicate(lst):
    result = []
    seen = []
    for i in lst:
        if i not in seen:
            result.append(i)
            seen.append(i)
    return result
    
print(remove_duplicate(nums))

        