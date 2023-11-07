list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlapping_numbers = []
for a in list_a:
    for b in list_b:
        if a == b:
            if not a in overlapping_numbers: overlapping_numbers.append(a)

for item in overlapping_numbers:
    print(item)
