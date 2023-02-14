while True:
    try:
        height = int(input("Height: "))
        if height > 0 and height < 9:
            break
    except ValueError:
        continue


for i in range(1, height + 1):
    for j in range(height - i): # height-i since first line always prints one #
        print(" ", end="")
    print("#"*i, end="")
    print("  ", end="")
    print("#"*i, end="")
    print()
