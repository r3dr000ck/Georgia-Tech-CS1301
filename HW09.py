"""
Georgia Institute of Technology - CS1301
Homework 9 - Recursion
"""

#########################################

"""
Function Name: cityHopper()
Parameters: city_str (str)
Returns: city_upper (str)
"""

def cityHopper(s):
    if len(s) == 1:
        if s.isupper():
            return s
        else:
            return ""
    else:
        if s[0].isupper():
            return s[0] + cityHopper(s[1:])
        else:
            return cityHopper(s[1:])


#########################################

"""
Function Name: traderJoes()
Parameters: receipt (list)
Returns: total_cost (float)
"""

def traderJoes(l):
    if len(l) == 0:
        return 0.0
    else:
        i = l[0]
        c = 0.0
        if len(i) == 3 and i[2] == "S":
            c = i[1] * 0.8
        else:
            c = i[1]
        return round(c + traderJoes(l[1:]), 1)

#########################################

"""
Function Name: partyPlanner()
Parameters: guest_foods (list)
Returns: food_votes (dict)
"""

def partyPlanner(l):
    if len(l) == 0:
        return {}
    else:
        i = l[0]
        y = partyPlanner(l[1:])
        if i in y:
            y[i] += 1
        else:
            y[i] = 1
        return y

#########################################

"""
Function Name: firstSemTAs()
Parameters: tasks (list), p_or_v (str)
Returns: assignments (list)
"""

def firstSemTAs(t, p):
    if len(t) == 0:
        return []
    else:
        i = t[0]
        l = firstSemTAs(t[1:], p)
        if i[1] == p or i[1] == "Both":
            l.append(i[0])
        return sorted(l)

#########################################

"""
Function Name: coffeeCreation()
Parameters: menu_items (list)
Returns: final_item (str)
"""

def coffeeCreation(l):
    if len(l) == 0:
        return ""
    else:
        i = l[0]
        j = coffeeCreation(l[1:])
        if type(i) == str:
            return i + j
        elif type(i) == list:
            return coffeeCreation(i) + j

#########################################
