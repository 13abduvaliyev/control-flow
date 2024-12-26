num = int(input("Son kiriting: "))
count = 0
i = 2

while i < num:
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count <= 2:
        count = 0
        print(i)
    count = 0
    i += 1

    
    
