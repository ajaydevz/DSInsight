words = ['hello','how','are','you']

results = {}

for i in words:
    for j in i:
        results[j] = results.get(j,0)+1

print(results)