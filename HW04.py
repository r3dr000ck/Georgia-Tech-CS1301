"""
Georgia Institute of Technology - CS1301
Homework 4 - Strings
"""

#########################################

"""
Function Name: encodeMessage()
Parameters: message (str)
Returns: encoded_message (str)
"""

nums = "0123456789 "

def encodeMessage(msg):
    ret = ""
    cnt = 0
    for i in msg:
        if (i not in nums) and (not i.upper() == i):
            ret += i
        elif i in nums and not i == " ":
            cnt += 1
    return ret[::-1] + str(cnt * 12)

#########################################

"""
Function Name: codeBreaker()
Parameters: message (str)
Returns: decoded_message (str)
"""

def codeBreaker(msg):
    t = msg.replace("_", " ")
    ret = ""
    for i in range(1, min(len(t), 30), 2):
        ret += t[i]
    return ret

#########################################

"""
Function Name: getCoordinates()
Parameters: location (str)
Returns: coordinates (str)
"""

def getCoordinates(loc):
    c1, c2 = -1, -1
    for i in range(len(loc)):
        if loc[i] == "e":
            if c1 < 0:
                c1 = i * 9
            else:
                c2 = i
                return f"Secret Lair Coordinates: ({c1}, {c2})"


#########################################

"""
Function Name: spyBudget()
Parameters: gadgets (str), budget (int)
Returns: cost_outcome (str)
"""

def spyBudget(g, d):
    tot = 0
    cntp = 0
    cntc = 0
    for i in g:
        if i == "G":
            tot += 25
        elif i == "L":
            tot += 15
        elif i == "P":
            cntp += 1
            if cntp == 1:
                tot += 30
        else:
            cntc += 1
            if cntc == 2:
                pass
            elif cntc > 2:
                tot += 10
            else:
                tot += 20
    if tot > d:
        return f"This mission will cost ${tot - d} too much!"
    else:
        return "Ready for action!"

#########################################

"""

Function Name: findMole()
Parameters: suspect (str), codenames (str)
Returns: suspect_status (str)
"""

def findMole(s, l):
    lst = l.split(":")
    for i in lst:
        if i[len(i) - 1] == s[len(s) - 1]:
            if i[::-1] == i:
                return f"{s}, codename {i}, is a double agent!"
            else:
                return f"{s}, codename {i}, is not the mole."
    return f"{s} is still a suspect."


#########################################