number = int(input("Enter number : "))

numbers_list = []
for n in range(1, number + 1):
    if number % n == 0:
        numbers_list.append(n)

for item in numbers_list:
    print(item)
