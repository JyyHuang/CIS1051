# Get User Input
counter = 0
while True:
    try:
        weight = int(input("Weight(lbs): "))
        height = int(input("Height(in): "))
        age = int(input("Age: "))
        break
# Only accepts int
    except:
        print("Please input an int.")


# Woman BMR
WBMR = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)

# Man BMR
MBMR = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)


# Output
print("The amount of chocolate bars a", weight,"pound,", height,"inch tall,", age, "year old woman should consume to maintain one's weight is:", WBMR/214)
print("The amount of chocolate bars a", weight,"pound,", height,"inch tall,", age, "year old man should consume to maintain one's weight is:", MBMR/214)