string = 'hello world'
vowel_count = {}
vowels = 'aeiou'

for char in string:
    if char.lower() in vowels:
        vowel_count[char.lower()] = vowel_count.get(char.lower(),0)+1


print(vowel_count)


my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

for value in my_dict.values():
    print(value)

                
data = [
    {'numbers': [1, 2, 3]},
    {'numbers': [4, 5, 6]},
    {'numbers': [7, 8, 9]}
]

results = sum(sum(obj['numbers']) for obj in data)
print(results)