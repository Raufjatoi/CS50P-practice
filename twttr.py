vowels = ('A', 'E', 'I', 'U', 'O', 'a', 'e', 'i', 'o', 'u')
i = input('Input: ')
for c in i:
    if c not in vowels:  
        print(c, end='')

