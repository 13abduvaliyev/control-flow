jumla = str(input("Jumla kiriting: "))

words = jumla.split()
long_word = jumla[0]

for i in words:
    if len(i) > len(long_word):
        long_word = i

print(long_word)
