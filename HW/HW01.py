"""
Georgia Institute of Technology - CS1301
Homework 1 - Functions & Expressions
"""

#########################################

"""
Function Name: weekOfWelcome()
Parameters: N/A
Returns: None (NoneType)
"""

def weekOfWelcome():
    day = input("Enter the day of the week: ")
    time = input("Enter the time of the event: ")
    location = input("Enter the location of the event: ")
    club = input("Enter the name of the club hosting the event: ")
    print(f"{day}, {time}, {location}: WoW event by the {club}")

#########################################

"""
Function Name: ramblinReck()
Parameters: N/A
Returns: None (NoneType)
"""

def ramblinReck():
    dis = int(input("How far away are you from the Reck? "))
    P = 1e4
    pi = 3.14
    print(f"The Ramblin' Reck is {round(P / (4 * pi * dis ** 2), 2)} Watts loud!")

#########################################

"""
Function Name: diningDollars()
Parameters: N/A
Returns: None (NoneTyoe)
"""

def diningDollars():
    drink = float(input("How many drinks are you having? "))
    app = float(input("How many appetizers are you having? "))
    ma = float(input("How many main courses are you having? "))
    des = float(input("How many desserts are you having? "))
    total = (3.0 * drink + 6.0 * app + 11.0 * ma + 3.0 * des) * 1.2
    print(f"You have spent a total of {total} dining dollars and have {round(23.0 - total, 1)} dining dollars left!")

diningDollars()

#########################################

"""
Function Name: findTs()
Parameters: N/A
Returns: None(NoneType)
"""

def findTs():
    loc = int(input("How many locations do we need to search on campus? "))
    ppl = int(input("How many people do we plan on searching with? "))
    t = loc ** 2
    time = t * (ppl / 2)
    print(f"It will take {int(time // 60)} hour(s) and {round((time % 60), 1)} minute(s) to find all of the T's!")


#########################################

"""
Function Name: leftOverTime()
Parameters: N/A
Returns: None (NoneType)
"""

def leftOverTime():
    ans = 24 * 7
    ans -= int(input("How many credit hours are you taking? ")) * 4
    ans -= int(input("How much sleep do you want to get each night? ")) * 7
    ans -= int(input("How many extracurriculars do you participate in? ")) * 4
    hobby = input("What activity do you want to do in your free time? ")
    print(f"You have {ans} hours this week to do {hobby}.")

#########################################
