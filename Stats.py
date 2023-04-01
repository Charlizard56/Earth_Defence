import TimeClock
from time import sleep

Game = True

Time = 0


# Classes
class Units:
    def __init__(self, name, amount, cost, process_time, process_amount):
        self.name = name
        self.amount = amount
        self.cost = cost
        self.process_time = process_time
        self.process_amount = process_amount

    def buy(self, money):
        if Drill_Sargent:
            print("How many? ")
            amount = input()
            try:
                if check(money, self.cost, amount):
                    self.process_amount = self.process_amount + int(amount)
            except:
                print("Try an actual number...")
        # BUY INDIVIDUAL
        else:
            if check(money, self.cost, 1):
                self.amount += 1
                print(f"\nBought 1 {self.name}")
                TimeClock.Clock()

    def sell(self):
        if self.amount > 0:
            print(f"How many?({self.amount}): ")
            x = input()
            if int(x) > 0 and int(x) <= self.amount:
                total = self.cost / 2 * int(x)
                print(total)
                resorces.money += total
                self.amount -= int(x)
                print(f"{x} Soldiers Sold for {total}")
            else:
                print(f"You don't have that many {self.name}")

        else:
            print("You have no Soldiers")

    def cancel(self):
        if self.process_amount > 0:
            print(f"{self.process_amount} {self.name} canceled. Return of ${self.process_amount * self.cost}")
            resorces.money += self.process_amount * self.cost
            self.process_amount = 0
        else:
            print("No orders")

    def process(self):
        total_amount = self.process_amount
        print(f"Soldiers Created: ({self.process_amount}/{total_amount})")
        sleep(1)
        TimeClock.Clock()
        while self.process_amount > 0:
            self.amount += 1
            self.process_amount -= 1
            sleep(1)
            print(f"Soldiers Created: ({self.process_amount}/{total_amount})")
            TimeClock.Clock()


class Resorces:
    def __init__(self, money, rations, med_kit, in_mission):
        self.money = money
        self.rations = rations
        self.med_kit = med_kit
        self.in_mission = in_mission


class Missions:
    def __init__(self, mission_number, name, description, soldiers, heavy, tanks, rations, medical_kits):
        self.mission_number = mission_number
        self.name = name
        self.description = description
        self.soldiers = soldiers
        self.heavy = heavy
        self.tanks = tanks
        self.rations = rations
        self.medical_kits = medical_kits

    def info(self):
        return print(f"{self.mission_number} {self.name} - {self.description}(S:{self.soldiers},H:,T:,R:,M:)")

    def check_amount(self):
        print("Are you sure?(y/n): ")
        x = input()
        if x == "y":
            if Unit_Soldiers.amount >= self.soldiers:
                print("Pass")
                self.deploy(self.soldiers, self.heavy, self.tanks, self.rations, self.medical_kits)

            else:
                print(f"Not enough! (S:{Unit_Soldiers.amount}/{self.soldiers})")
        else:
            print("Mission Canceled")

    def deploy(self, soldiers, heavy, tanks, rations, medical_kits):
        print(f"Deployed S:{soldiers},H:,T:,R:,M:")
        Unit_Soldiers.amount -= soldiers

    def success(self, soldiers):
        if soldiers >= self.soldiers:
            print("Pass")
        else:
            print("You don't have enough!")


# Resorces
Money = 10000
Rations = 100
Med_Kit = 0
In_Mission = False
resorces = Resorces(Money, Rations, Med_Kit, In_Mission)

# Troops
Unit_Soldiers = Units("Soldiers", 0, 100, 1, 0)

# Upgrades
Drill_Sargent = False
Drill_Sargent_Cost = 1000

# Missions
In_Mission = False
Evacuate = Missions("1.", "Evacuation", "Evacuate the citizens", 10, 0, 0, 0, 0)


def check(money, cost, amount):
    if money >= cost * int(amount):
        resorces.money -= cost * int(amount)
        return True

    else:
        print("Not enough Money")
        return False
