
# User Input
while True:
    try: 
        number = int(input("Number: "))
        if number > 0:
            break
    except ValueError:
        continue


# change number into string to count length of number
numlength = 0
tempnum = str(number)
for count in range(len(tempnum)):
    numlength += 1

# makes sure length is between 13 and 16
if numlength < 13 or numlength > 16:
    print("INVALID")
    exit()


#checksum
def luhn(num):
    even = []
    values = []
    odd = []
    sumeven = 0
    sumodd = 0


    for i in range(1, numlength + 1, 2):            # iterate through list 
        even.append((num % (10 * 10**i)) // 10**i)   # append each value to make new list of every digit

    for times2 in even:                 # multiply the digits by 2
        values.append(times2 * 2)

    for digits in values:
        split = (digits % 100//10) + (digits % 10)   # splits the digits up and adds them
        sumeven = sumeven + split

    for i in range(0, numlength, 2):            # iterates through digits not multiplied by 2
        odd.append((num % (10 * 10**i)) // 10**i)

    for digits in odd:              # adds even and odd digits
        sumodd = sumodd + digits
    totalsum = sumeven + sumodd
    totalsum = totalsum % 10
    return totalsum             # returns the number % 10 to check if it is 0

if luhn(number) != 0:
    print("INVALID")
    exit()
if luhn(number) == 0:
    firstdigit = int(tempnum[0])
    seconddigit = int(tempnum[1])
    if firstdigit == 4 and (numlength == 13 or numlength == 16):          # VISA
        print("VISA")
    elif firstdigit == 3 and seconddigit == 4 or seconddigit == 7 and numlength == 15:          # AMEX
        print("American Express")
    elif firstdigit == 5 and 0 < seconddigit < 6 and numlength == 16:           # MasterCard
        print("MASTERCARD")
    else:
        print("INVALID")
    


