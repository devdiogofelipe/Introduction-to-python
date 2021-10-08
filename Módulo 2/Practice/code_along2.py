name = input("Tell me your first name: ")
count = 0

print(name, "is spelled:")

for x in name:
    
        print(x, end = ' ')

        count += 1


print("and your name have", count, "letters")
