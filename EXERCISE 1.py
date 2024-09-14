seasons = ("Winter", "Spring", "Summer", "Autumn")

def getSeasons(month):
    if month in [12,1,2]:
        return seasons[0]
    elif month in [3,4,5,]:
        return seasons[1]
    elif month in [6,7,8]:
        return seasons[2]
    elif month in [9,10,11]:
        return seasons[3]
    else:
        return none
month = int(input("Enter a number of a month:"))

season = getSeasons(month)

if season:
    print(f"The corresponding season is: {season}.")
else:
    print("Invalid month. Kindly enter a number between 1 and 12.")
