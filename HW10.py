"""
Georgia Institute of Technology - CS1301
HW10 - OOP
"""

#########################################

class Visitor:
    def __init__(self, name: str, height: int, money: float, funLevel: int = 0, nauseaLevel: int = 15):
        self.name = name
        self.height = height
        self.money = money
        self.funLevel = funLevel
        self.nauseaLevel = nauseaLevel
        self.park = None
    
    def enter_park(self, p):
        if self.money < p.admissionFee:
            return f"{self.name} did not enter the park."

        if not p.isOpen:
            return f"{self.name} did not enter the park."

        self.park = p
        p.visitors.append(self)
        self.money -= p.admissionFee
        p.revenue += p.admissionFee

        return f"{self.name} has entered the park."

    def leave_park(self):
        if self.park is None:
            return f"{self.name} is not in a park."
        
        p = self.park
        p.visitors.remove(self)
        
        rev = 5 * (self.funLevel / (self.funLevel + self.nauseaLevel))
        rev = round(rev, 1)
        
        p.reviews.append(rev)
        self.park = None
        return f"{self.name} gave the park {rev} stars!"

    def get_in_line(self, ri):
        if self.park is None:
            return f"{self.name} is not in a park."
        
        p = self.park
        if ri not in p.rides:
            return f"{ri.name} is at a different park."
        
        if len(ri.visitorsInLine) < ri.lineCapacity and ri.isOpen and self.height >= ri.minHeight:
            p.visitors.remove(self)
            ri.visitorsInLine.append(self)
            return f"{self.name} got in line for {ri.name}."
        else:
            self.funLevel = max(self.funLevel - 30, 1)
            return f"{self.name} could not get in line for {ri.name}."

    def buy_food(self, f):
        if self.park is None:
            return f"{self.name} is not in a park."
        
        p = self.park
        
        if f in p.food and self.money >= p.food[f]:
            self.money -= p.food[f]
            self.funLevel += 40
            self.nauseaLevel += 60
            p.revenue += p.food[f]
            return f"{self.name} purchased {f} for lunch."
        else:
            self.funLevel = max(self.funLevel - 30, 1)
            if f in p.food:
                return f"{self.name} did not have enough money to buy {f}!"
            else:
                return f"The item {self.name} wanted was unavailable."
            
    def __eq__(self, visitor):
        return (self.funLevel == visitor.funLevel and self.nauseaLevel == visitor.nauseaLevel)
    
    def __str__(self):
        return f"{self.name} - fun: {self.funLevel}, height: {self.height}, nausea: {self.nauseaLevel}, money: {self.money}"

#########################################

class Ride:
    def __init__(self, name: str, funAmount: int, nauseaAmount: int, isOpen: bool = True, lineCapacity: int = 10, minHeight: int = 48, durability: int = 99):
        self.name = name
        self.funAmount = funAmount
        self.nauseaAmount = nauseaAmount
        self.isOpen = isOpen
        self.lineCapacity = lineCapacity
        self.minHeight = minHeight
        self.durability = durability
        self.totalRides = 0
        self.visitorsInLine = []
        self.park = None

    def open_ride(self):
        self.isOpen = True
        return f"{self.name} is now open."

    def close_ride(self):
        self.isOpen = False
        l = self.visitorsInLine
        for i in l:
            if i.park is not None:
                p = i.park
                p.visitors.append(i)
            i.funLevel = max(i.funLevel - 30, 1)
        
        self.visitorsInLine = []
        return f"{self.name} has closed."

    def run_ride(self):
        if not self.isOpen:
            return "The ride is closed!"

        n = len(self.visitorsInLine)

        self.durability -= n * 2
        if self.durability <= 0:
            self.close_ride()
            return f"The ride {self.name} has broken!"

        for v in self.visitorsInLine:
            v.funLevel += self.funAmount
            v.nauseaLevel += self.nauseaAmount
            v.park.visitors.append(v)

        self.totalRides += n
        self.visitorsInLine = []

        return f"{n} went on {self.name}."

    def fix_ride(self, d):
        self.isOpen = True
        self.durability = d
        p = self.park
        p.revenue -= 450.0
        return f"A mechanic has fixed {self.name}, which now has a durability of {d}."
    
    def increase_line_capacity(self, n):
        self.lineCapacity += n
        return f"{self.name} now has a line capacity of {self.lineCapacity}."
    
    def __gt__(self, other):
        a = len(self.visitorsInLine) + self.totalRides
        b = len(other.visitorsInLine) + other.totalRides
        
        return a > b
    
    def __str__(self):
        return f"{self.name} has {len(self.visitorsInLine)} waiting in line and {self.totalRides} visitors have been on it today!"

#########################################

class Park:
    def __init__(self, name: str, admissionFee: float = 60.0, isOpen: bool = True, food: dict = {"hotdog": 10.00, "salad": 8.50}, maxVisitors: int = 100):
        self.name = name
        self.admissionFee = admissionFee
        self.isOpen = isOpen
        self.food = food
        self.maxVisitors = maxVisitors
        self.rating = 2.5
        self.reviews = []
        self.rides = []
        self.visitors = []
        self.revenue = 0.0
    
    def add_ride(self, ri):
        self.rides.append(ri)
        ri.park = self
        ri.isOpen = True
        return f"A new ride has just been built in {self.name}, {ri.name}!"
    
    def remove_ride(self, ri):
        self.rides.remove(ri)
        ri.park = None
        ri.isOpen = False
        
        return f"The ride {ri.name} has been decommissioned!"
    
    def update_rating(self):
        if self.reviews:
            self.rating = round(sum(self.reviews) / len(self.reviews), 1)
        return f"{self.name}'s new rating is {self.rating}!"
    
    def update_park_status(self, op):
        self.isOpen = op
        if op:
            l = self.rides
            for i in l:
                i.open_ride()
            return f"{self.name} is now open!"
        else:
            l = self.rides
            for i in l:
                i.close_ride()
            for v in self.visitors[:]:
                v.leave_park() 
            self.visitors = []
            return f"{self.name} has closed for the day."

    def fireworks_show(self, le):
        for i in self.rides:
            i.close_ride()
        
        for i in self.visitors:
            i.funLevel += (le * 5)
            i.nauseaLevel = max(0, i.nauseaLevel - 40)
        
        for i in self.rides:
            i.open_ride()
        
        return f"Everyone enjoyed a {le}-minute fireworks show."

    def find_rides_for_visitor(self, vi, m):
        result = []
        for r in self.rides:
            if r.isOpen and len(r.visitorsInLine) < r.lineCapacity and len(r.visitorsInLine) <= m and vi.height >= r.minHeight:
                result.append(r.name)
        return result

    def __lt__(self, other):
        return self.revenue < other.revenue

    def __str__(self):
        return f"{self.name} has {len(self.rides)} rides, {len(self.visitors)} visitors, and has made ${self.revenue} today!"













        
