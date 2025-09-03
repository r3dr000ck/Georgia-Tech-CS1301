def techLibs():
    name = input("Enter your name: ")
    bf = input("Enter your best friend's name: ")
    sp = input("Enter your favorite study spot: ")
    print(f"The other day, I saw {name} and {bf} up to no good.")
    print(f"They were loudly gossiping at {sp} instead of studying.")

def diningDollars():
    cur = float(input("How many dining dollars do you currently have? "))
    sp  = float(input("How many dining dollars do you spend per week? "))
    week = int(input("How many weeks are left? "))
    print(f"You will have ${round(cur - (sp * week),2)} left over.")

def sphereVol():
    r = float(input("Enter the radius of your sphere: "))
    print(f"The volume of your sphere is {round((3.14) * (r ** 3) * (4/3) ,2)}.")

def italianNight(time):
    if time < 20.0:
        print("We'll cook some othertime.")
    elif time < 35.0:
        print("Breadsticks")
    elif time < 50:
        print("Pasta")
    else:
        print("Lasagna")

def toCook(numclass, dollar):
    if numclass > 3 and dollar > 10.0:
        print("Let's get Panda Express!")
    elif numclass <= 3 and dollar >= 50.0:
        print("Let's splurge on Chick-fil-A!")
    else:
        print("Guess I'll have to cook myself.")

def cookingClass(date, isw):
    if date % 2 == 1 and isw:
        return "Unsure"
    elif date % 2 == 0 and not isw:
        return "No"
    else:
        return "Yes"
