"""
Georgia Institute of Technology - CS1301
Homework 3 - Iteration
"""

#########################################

"""
Function Name: decryptMessage()
Parameters: secretMessage (str)
Returns: finalTransmission (str)
"""

def decryptMessage(msg):
    cnt = 0
    ret = ""
    
    for i in msg:
        if not i.isalpha():
            cnt += 1
        else:
            ret += i 
    
    return f"Message [{ret}] received. {cnt} alien symbols found!"

#########################################

"""
Function Name: calculateFuel()
Parameters: operations (str), values (str), initialFuel (int)
Returns: finalFuel (str)
"""

def calculateFuel(op, val, ini):
    ret = ini
    for i in range(len(op)):
        o = op[i]
        num = int(val[i])
        if o == "+":
            ret += num
        elif o == "-":
            ret -= num
        elif o == "/":
            ret = ret // num
        else:
            ret *= num
    
    if ret >= 0:
        return f"Mission success! Remaining fuel: {ret}"
    else:
        return "Mission failed: not enough fuel!"

#########################################

"""
Function Name: decodingData()
Parameters: data (str)
Returns: decodedData (str)
"""

def decodingData(d):
    ret = ""
    for i in range(len(d) // 3):
        sp = d[(3 * i) : (3 * i + 3)]
        if sp == "314":
            ret += "pi"
        elif (int(d[3 * i + 1]) - 1 == int(d[3 * i])) and (int(d[3 * i + 2]) - 1 == int (d[3 * i + 1])):
            ret += sp
    if len(ret) > 0:
        return ret
    else:
        return "No sequences found!"


#########################################

"""
Function Name: extinguishFire()
Parameters: password (str), maxTime (int)
Returns: outcome (str)
"""

n = "02468"
v = "aiueoAIUEO"

def extinguishFire(psw, t):
    sp = 0

    for i in psw:
        if i in v:
            sp += 2
        elif i in n:
            sp += 5
    
    if sp < t:
        return f"Congrats! You have put out the fire with {t - sp} minute(s) to spare!"
    else:
        return "Oh no! I was too late to save the engine room!"

#########################################

"""
Function Name: dockAlign()
Parameters: corridor (str), limit (int)
Returns: dockingStatus (str)
"""

def dockAlign(cor, lim):
    now = 0
    j = 0

    while j < len(cor):
        i = cor[j]
        if i == ">":
            now += 1
        elif i == "<":
            now -= 1
        elif i == "=":
            if now < 0:
                now += 1
            elif now > 0:
                now -= 1
        elif i == "!":
            now *= 2
        else:
            j += 1
        
        j += 1

        if abs(now) > lim:
            return f"Docking failed at position {j} (offset {now})."
        
    if now == 0:
        return "Docking was a complete success!"
    else:
        return f"Docking complete with residual offset {now}."

#########################################
