"""
Georgia Institute of Technology - CS1301
Homework 5 - Lists, Tuples, and Modules
"""

#########################################

"""
Function Name: roundOf16()
Parameters: teams (list), points (list)
Returns: advancedTeams (list)
"""

def roundOf16(teams, points):
    ret = []
    for i in range(len(teams)):
        if points[i] >= 15:
            ret.append(teams[i])
    return sorted(ret)

#########################################

"""
Function Name: stadiumCapacity()
Parameters: stadiumData (list)
Returns: largest (tuple)
"""

def stadiumCapacity(stadiumData):
    d = {}
    for i in stadiumData:
        s = ""
        j = 0
        while i[j].isalpha():
            s += i[j]
            j += 1
        d[int(i[j:])] = s
    d = sorted(d.items(), reverse=True)
    largest = (d[0][0], d[0][1])
    smallest = (d[-1][0], d[-1][1])
    print(f"{smallest[1]} has the lowest capacity. We shouldn't choose this one!")
    return largest

#########################################

"""
Function Name: snackPlan()
Parameters: availableSnacks (list), budget (int)
Returns: shoppingList (list)
"""

def snackPlan(snacks, budget):
    d = {}
    for i in snacks:
        d[i[1]] = (i[0], i[2])
    d = dict(sorted(d.items(), reverse=True))
    rem = budget
    ret = []
    for i in d:
        rem -= (i * int(d[i][1]))
        if rem < 0:
            rem += (i * int(d[i][1]))
            pass
        else:
            ret.append(d[i])
    if len(ret) == 0:
        return "No more shopping!"
    else:
        return sorted(ret, key=lambda x: (x[0]))

#########################################

"""
Function Name: topScorer()
Parameters: data (list)
Returns: player (str)
"""

def topScorer(data):
    s = sorted(data, key=lambda x: (x[1]), reverse=True)
    s = sorted(s, key=lambda x: (x[2]), reverse=True)
    ret = []
    for i in s:
        ret.append(i[0])
    print(f"{ret[0]} is the best!")
    return ret

#########################################

"""
Function Name: whichMatches()
Parameters: matchSchedule (list), dayOfWeek (int)
Returns: matches (list)
"""

import datetime

def whichMatches(sch, n):
    ret = []
    for i in sch:
        dd = i[2]
        d = datetime.date(int(dd[0]), int(dd[1]), int(dd[2]))
        day = d.weekday()
        if day == n:
            ret.append((i[0], i[1]))
    return sorted(ret, key=lambda x: (x[0]))

#########################################