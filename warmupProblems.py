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
        return "We'll cook some othertime."
    elif time < 35.0:
        return "Breadsticks"
    elif time < 50:
        return "Pasta"
    else:
        return "Lasagna"

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

def captureTheFlag(dir):
    t = dir[::-1]
    for s in t:
        if s == "L":
            print("Turn left!")
        else:
            print("Turn right!")

def demystifyMessage(msg):
    t = ""
    for i in msg:
        if i.isalpha():
            t += i
    return t

def gnomeAccounting(msg):
    for i in range(len(msg) // 6):
        print(msg[(6 * i) : (6 * (i + 1))])

def countCase(let):
    up = 0
    lo = 0
    for i in let:
        if i.isalpha():
            if i.islower():
                lo += 1
            else:
                up += 1
    if up == lo:
        return "Perfectly balanced!"
    elif up > lo:
        return f"{up - lo} more uppercase letter(s)."
    else:
        return f"{lo - up} more lowercase letter(s)."

def findLove(cand, city):
    ret = []
    for i in cand:
        if i[1] == city:
            ret.append(i[0])
    return sorted(ret)

def mutualInterests(your, their):
    ret = []
    for i in your:
        if i in their:
            ret.append(i)
    return sorted(ret)



