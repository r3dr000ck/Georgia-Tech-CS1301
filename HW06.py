"""
Georgia Institute of Technology - CS1301
Homework 6 - Dictionaries
"""

#########################################

"""
Function Name: favoriteSpells()
Parameters: spells (dict), student (str)
Returns: house_spell_counts (dict)
"""

def favoriteSpells(d, na):
    print(f"{na} from {d[na]['House']}'s favorite spell is {d[na]['Favorite Spell']}.")
    ret = {}
    for i in d:
        if d[i]["Favorite Spell"] in ret:
            ret[d[i]["Favorite Spell"]] += 1
        else:
            ret[d[i]["Favorite Spell"]] = 1
    return ret

#########################################

"""
Function Name: pointsTally()
Parameters: events (list)
Returns: points (dict)
"""

def pointsTally(l):
    r = {}
    for t in l:
        if t[0] in r:
            r[t[0]] += t[1]
        else:
            r[t[0]] = t[1]
    q = sorted(r.items(), key=lambda x: x[0])
    s = {}
    for i in q:
        if i[1] < 0:
            pass
        else:
            s[i[0]] = i[1]
    if len(s) == 0:
        return "No winners!"
    return s

#########################################

"""
Function Name: spellDuel()
Parameters: gryff_spells (dict), sly_spells (dict)
Returns: results (str)
"""

def avg(l):
    ret = 0
    for i in l:
        ret += i
    return ret / len(l)

def spellDuel(gr, sl):
    ret = {}
    for i in gr:
        if i in sl:
            if avg(gr[i]) > avg(sl[i]):
                ret[i] = "Gryffindor"
            elif avg(gr[i]) < avg(sl[i]):
                ret[i] = "Slytherin"
            else:
                ret[i] = "Tie"
        else:
            ret[i] = "Gryffindor"
    for j in sl:
        if j not in gr:
            ret[j] = "Slytherin"
    return ret

#########################################

"""
Function Name: potionTracker()
Parameters: potion_recipes (dict), ingredient_stock (dict)
Returns: potion_complete (dict)
"""

def potionTracker(po, ing):
    ret = {}
    for i in po:
        l = po[i]
        ch = 1
        for j in l:
            k = j[0]
            if k in ing:
                if ing[k] >= j[1]:
                    pass
                else:
                    ch = 0
            else:
                ch = 0
        if ch:
            ret[i] = "Complete"
        else:
            ret[i] = "Incomplete"
    return ret

#########################################

"""
Function Name: gringotts()
Parameters: deposits (list)
Returns: filtered_deposits (dict)
"""

def gringotts(dep):
    ret = {}
    for i in dep:
        name = i[0]
        bank = i[1]
        am = i[2]
        if name in ret:
            if bank in ret[name]:
                ret[name][bank] += am
            else:
                ret[name][bank] = am
        else:
            ret[name] = {bank: am}
    fin = {}
    for j in ret:
        if j not in fin:
            fin[j] = {}
        for k in ret[j]:
            if ret[j][k] > 100:
                fin[j][k] = ret[j][k]
        if len(fin[j]) == 0:
            del fin[j]
        
    return fin

#########################################