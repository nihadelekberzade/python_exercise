length = int(input('Length : '))

list = [1,1]

for n in range(2,length):
    list.append(list[n - 2] + list[n-1])

print(list)