"""
Georgia Institute of Technology - CS1301
Homework 7 - File I/O and CSV Files
"""

#########################################

"""
Function Name: travelBudget()
Parameters: budget (float)
Returns: remaining (float)
"""

def travelBudget(budget):
    rem = budget
    ret = []
    f = open("travelPlans.txt", "r")
    l = f.readlines()
    for i in range(0, len(l), 4):
        dep, des = l[i].strip().split(" to ")
        cost = float(l[i + 1])
        typ = l[i + 2].strip()
        if typ == "PLANE":
            cost += 30.0
        if rem >= cost:
            rem -= cost
            ret.append(des)
    if ret == []:
        print("Stay home this time...")
    else:
        print(sorted(ret))
    f.close()
    return round(rem, 2)

"""
Function Name: findAffordableHotels()
Parameters: maxPrice (float)
Returns: None (NoneType)
"""

def findAffordableHotels(m):
    f = open("hotelDetails.txt", "r")
    hotels = []
    costs = []
    avg = 0.0
    l = f.readlines()
    for i in range(0, len(l), 5):
        name = l[i].strip()
        pn = float(l[i + 1])
        nights = int(l[i + 2])
        rate = float(l[i + 3])
        if pn <= m and rate >= 5.0:
            hotels.append(name)
            costs.append(format(pn * nights, ".2f"))
            avg += rate
    if hotels == []:
        with open("bestHotels.txt", "w") as of:
            of.write("There are no good hotels available.")
            of.close()
    else:
        with open("bestHotels.txt", "w") as of:
            of.write("The following hotels are great choices:\n\n")
            for i in range(len(hotels)):
                of.write(f"The cost to stay in {hotels[i]}'s hotel is ${costs[i]}.\n")
            of.write("\n")
            r = format(avg / len(hotels), ".2f")
            of.write(f"The average rating of all affordable hotels is {r}.")
            of.close()
    f.close()
    
findAffordableHotels(125.50)

#########################################

"""
Function Name: csvToList()
Parameters: fileName (str)
Returns: flightsList (list)
"""

def csvToList(n):
    try:
        f = open(n, "r")
        h = f.readline()
        fl = f.readlines()
        ret = []
        for i in fl:
            a,b,c = i.strip().split(",")
            ret.append((a,b,int(c)))
        f.close()
        return ret
    except FileNotFoundError:
        return []

#########################################

"""
Function Name: csvToDict()
Parameters: fileName (str)
Returns: flightsDict (dict)
"""

def csvToDict(n):
    try:
        f = open(n, "r")
        h = f.readline()
        fl = f.readlines()
        ret = {}
        for i in fl:
            a,b,c = i.strip().split(",")
            if ((a,b)) in ret:
                ret[(a,b)].append(int(c))
            else:
                ret[(a,b)] = [int(c)]
        f.close()
        return ret
    except FileNotFoundError:
        return {}

#########################################

"""
Function Name: worstRoutes_list()
Parameters: originCountry (str), destCountry (str), flightsList (list)
Returns: message (str)
"""

def worstRoutes_list(org, dest, fl):
    m = 0
    for i in fl:
        if i[0] == org and i[1] == dest:
            m = max(m, i[2])
    return f"{org} to {dest}: {m} carbon emissions."

flightsList = csvToList("flight_emissions_data_short.csv")
# print(worstRoutes_list("Ethiopia", "United Kingdom", flightsList))

#########################################

"""
Function Name: worstRoutes_dict()
Parameters: originCountry (str), destCountry (str), flightsDict (dict)
Returns: message (str)
"""

def worstRoutes_dict(org, dest, fd):
    l = fd[((org, dest))]
    return f"{org} to {dest}: {max(l)} carbon emissions."

flightsDict = csvToDict("flight_emissions_data_short.csv")
# print(worstRoutes_dict("Ethiopia", "United Kingdom", flightsDict))


#########################################
