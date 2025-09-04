import math
import requests

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
        return "We'll cook some other time."
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

def numInventions(inv):
    ret = 0
    for i in inv:
        if i[1]:
            ret += 1
    return ret

def helpPhineas(want, l):
    for i in l:
        if i[0] == want:
            if 1 <= i[1] and i[1] <= 8:
                return True
    return False

def agentDispatch(coo, agen):
    shr = 1e10
    m = ""
    for i in agen:
        d = math.dist(coo, i[1])
        if d < shr:
            m = i[0]
            shr = d
    return m

def bestCity(vd):
    c = ""
    ma = 0
    for i in vd:
        cnt = len(vd[i])
        if cnt > ma:
            ma = cnt
            c = i
    return c

def winningTeam(d):
    ret = []
    for i in d:
        if d[i][1] >= 25:
            ret.append(i)
    return sorted(ret)

def fantasyF1(cat, pick):
    ret = 0
    for i in pick:
        for j in cat:
            if i in cat[j]:
                ret += cat[j][i]
    return ret

with open("swiftieFlights.txt", "r", encoding="utf-8") as f:
    d1 = f.readline()
    d2 = f.readline()
    txt = f.read()

flights = []

tmp = []
j = 0

for i in txt.split("\n"):
    if j == 0:
        tmp.append(i)
        j += 1
    elif j == 1:
        fl = i.split(" ")
        tmp.append(int(fl[0]))
        j += 1
    elif j == 2:
        fl = i.split(" ")
        tmp.append(int(fl[0]))
        j += 1
    elif j == 3:
        tmp.append(int(i[1:]))
        j += 1
    elif j == 4:
        fl = i.split(" ")
        tmp.append(float(fl[0]))
        j += 1
    else:
        j = 0
        flights.append(tmp)
        tmp = []

flights.append(tmp)

def taylorEmissions(r):
    for i in flights:
        if i[0] == r:
            return i[4]

def taylorFlights(c):
    ret = []
    for i in flights:
        if i[4] > c:
            ret.append(i[0])
    return sorted(ret)

def transportationModes(city):
    with open("transportationModes.txt", "w", encoding="utf-8") as f:
        f.write("Transportation Modes\n")
        f.write("\n")
        for j in range(len(city)):
            i = city[j]
            f.write(f"{i[0]}: {i[1]}")
            if j < len(city) - 1:
                f.write("\n")

def letterLover(s):
    url = "https://ghibliapi.vercel.app/films"

    response = requests.get(url)
    ghibli = response.json()

    ret = []
    for film in ghibli:
        if film["title"][0].lower() == s.lower():
            ret.append(film["title"])
    return sorted(ret)

def speciesFinder(eye):
    l = "https://ghibliapi.vercel.app/people"

    rp = requests.get(l)
    eyes = rp.json()

    for e in eyes:
        if eye == e["eye_color"]:
            return True
        
    return False

def characters(name):
    ret = []

    url = "https://ghibliapi.vercel.app/films"

    response = requests.get(url)
    ghibli = response.json()

    for film in ghibli:
        if film["title"] == name:
            l = film["people"]
            for a in l:
                if a == "https://ghibliapi.vercel.app/people/":
                    return []
                else:
                    resp = requests.get(a)
                    n = resp.json()
                    ret.append(n["name"])
    
    return sorted(ret)

def foulCount(l):
    if l == []:
        return 0
    af = l.pop()
    return (af[1] + foulCount(l))

def convertTeams(tu):
    if len(tu) == 0:
        return []
    tmp = list(tu)
    a = tmp.pop()
    tu = tuple(tmp)
    if isinstance(a, str):
        return convertTeams(tu) + [a]
    else:
        return convertTeams(tu)

def mergeTeamNames(t1, t2):
    if t1 == "" and t2 == "":
        return ""
    elif t1 == "":
        if t2[0] == "=":
            return t2[1:]
        else:
            return t2
    elif t2 == "":
        if t1[0] == "=":
            return t1[1:]
        else:
            return t1
    else:
        if t1[0] == "=":
            if len(t1) > 1:
                return t1[1] + mergeTeamNames(t1[2:], "=" + t2)
            else:
                return t1[1] + mergeTeamNames("", t2)
        elif t2 [0] == "=":
            if len(t2) > 1:
                return t2[1] + mergeTeamNames("=" + t1, t2[2:])
            else:
                return t2[1] + mergeTeamNames(t1, "")
        else:
            if len(t1) > 0:
                return t1[0] + mergeTeamNames(t1[1:], "=" + t2)
            else:
                return t1[0] + mergeTeamNames("", t2)
