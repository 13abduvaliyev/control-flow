word = str(input("Biror so'z kiriting: "))

for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        print("Palindrom emas") 
        break   
    else: 
        print("Palindrom")
        break
