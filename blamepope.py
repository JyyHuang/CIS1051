def leapyear(year):
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


while True:
    try:
        date = input("Please enter a date in MM/DD/YYYY format: ")
        month = int(date[0:2])
        day = int(date[3:5])
        year = int(date[6:])
        if (month in [4,6,9,11]):
            if 1 <= day <= 30:
                print("valid date")
            else:
                print("invalid day")
                continue
            break
        elif month in [1,3,5,7,8,10,12]:
            if 1 <= day <= 31:
                print("valid date")
            else:
                print("invalid day")
                continue
            break
        elif month == 2:
            if 1 <= day <= 28:
                print("valid date")
            elif day == 29 and leapyear(year) == True:
                print("valid day")
            elif day == 29 and leapyear(year) ==  False:
                print("invalid day")
                continue
            break
        else:
            print("invalid month")
            continue
    except ValueError:
        print("Please enter a valid date")
        continue

