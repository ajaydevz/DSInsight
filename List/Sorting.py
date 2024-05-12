# Sort a list of strings based on the length of each string

my_strings = ["apple", "banana", "pear", "kiwi", "orange"]

def bubble_sort_string_by_length(string):
    n = len(string)
    for i in range(n):
        for j in range(0,n-i-1):
            if len(string[j]) > len(string[j+1]):
                string[j],string[j+1] = string[j+1],string[j]
    return string

print(bubble_sort_string_by_length(my_strings))

