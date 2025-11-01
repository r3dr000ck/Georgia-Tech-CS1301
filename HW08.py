"""
Georgia Institute of Technology - CS1301
Homework 08 - APIs
"""

#########################################
import mock_requests as requests # Use this import for the mock-requests module

"""
Function Name: languageCapitals()
Parameters: language (str)
Returns: capitals (list)
"""


def languageCapitals(lang):
    url = f"https://restcountries.com/v3.1/lang/{lang}"
    resp = requests.get(url)
    data = resp.json()
    capitals = []
    for country in data:
        if 'capital' in country:
            if 'area' in country:
                if country['area'] >= 1000000:
                    capitals.append(country['capital'][0])
    return sorted(capitals)

#########################################

"""
Function Name: maximizeCountries()
Parameters: countryName (str)
Returns: borderingList (list)
"""

def maximizeCountries(cnt):
    main_cnt_url = f"https://restcountries.com/v3.1/name/{cnt}"
    main_cnt_resp = requests.get(main_cnt_url)
    main_cnt_data = main_cnt_resp.json()
    ret = []
    count = 0
    if "borders" in main_cnt_data[0]:
        borders = main_cnt_data[0]["borders"]
        cur = main_cnt_data[0]["currencies"]
        
        for c in borders:
            b_url = f"https://restcountries.com/v3.1/alpha/{c}"
            b_resp = requests.get(b_url)
            b_data = b_resp.json()
            b_cur = b_data[0]["currencies"]
            
            if list(b_cur) == list(cur):
                count += 1
                ret.append(b_data[0]["name"]["common"])
                
    print(f"There are {count} bordering countries that use the same currency.")
    return sorted(ret)

#########################################

"""
Function Name: findConnections()
Parameters: country1 (str), country2 (str)
Returns: connections (list)
"""

def findConnections(c1, c2):
    c1_url = f"https://restcountries.com/v3.1/name/{c1}"
    c1_resp = requests.get(c1_url)
    c1_data = c1_resp.json()
    
    c2_url = f"https://restcountries.com/v3.1/name/{c2}"
    c2_resp = requests.get(c2_url)
    c2_data = c2_resp.json()
    
    ret = []
    if "borders" in c1_data[0] and "borders" in c2_data[0]:
        c1_b = c1_data[0]["borders"]
        c2_b = c2_data[0]["borders"]
        
        for i in c1_b:
            if i in c2_b:
                b_url = f"https://restcountries.com/v3.1/alpha/{i}"
                b_resp = requests.get(b_url)
                b_data = b_resp.json()
                n = b_data[0]["name"]["common"]
                if not n == c1:
                    ret.append(n)
    if len(ret) == 0:
        return "No way to compromise for this meetup!"
    return sorted(ret)


#########################################

"""
Function Name: currencyCountries()
Parameters: currency (str)
Returns: countryCapitals (dict)
"""

def currencyCountries(cur):
    cur_url = f"https://restcountries.com/v3.1/currency/{cur}"
    cur_resp = requests.get(cur_url)
    cur_data = cur_resp.json()
    ret = {}
    if not cur_data == {"status":404,"message":"Not Found"}:
        for i in cur_data:
            r = i["region"]
            n = i["name"]["common"]
            if r in ret:
                ret[r].append(n)
                ret[r] = sorted(ret[r])
            else:
                ret[r] = [n]
    else:
        print("No countries found!")
    return ret

#########################################

"""
Function Name: mostPopulated()
Parameters: region (str), numCountries (int)
Returns: largestCountries (dict)
"""

def mostPopulated(reg, n):
    url = f"https://restcountries.com/v3.1/region/{reg}"
    resp = requests.get(url)
    data = resp.json()
    ret = {}
    cs = {}
    for i in data:
        cs[i["name"]["common"]] = int(i["population"])
    sorted_cs = dict(sorted(cs.items(), key=lambda item: item[1], reverse=True))
    
    j = n
    for i in sorted_cs:
        if j <= 0:
            break
        ret[i] = sorted_cs[i]
        j -= 1
    return ret


#########################################
