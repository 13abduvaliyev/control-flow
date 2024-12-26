numbers = input("Sonlarni kiriting: ")

num  = numbers.split()

for n in num:
    if int(n) % 3 == 0 and int(n) % 2 == 1:
        print(n, end = "")
 