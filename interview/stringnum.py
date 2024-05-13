word =  " 1  3  4  5  6  8  7  5  4  12  13 24 "

num = [int(num) for num in word.split()]
sum_of_odd = sum(i for i in num if i % 2 != 0)

print(sum_of_odd)



