list_a = [1, 1, 2, 2, 3]


def remove_duplicates(l):
    unique_list = list(set(l))
    return unique_list


print(remove_duplicates(list_a))
