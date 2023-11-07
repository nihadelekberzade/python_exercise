num = int(input('Number : '))

number_of_divisers = 0
for n in range(1, num + 1):
    if num % n == 0:
        number_of_divisers += 1

if number_of_divisers <= 2:
    print('Number is prime')
else:
    print('Number is not prime')
