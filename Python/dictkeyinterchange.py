original_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56, 'E': 12, 'F': 69, 'G': 67, 'H': 23}


new_dict = {k:v for v,k in original_dict.items()}
print(new_dict)

