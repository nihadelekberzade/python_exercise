
def reverse(str_a):
    words = str_a.split()
    new_str = ''
    for i in range(len(words) - 1, -1, -1):
        new_str += ' '+ words[i]
    return new_str

str_a = 'My name is Michele'

print(reverse(str_a))
