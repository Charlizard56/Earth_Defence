import random

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
                if check(resorces.money, self.cost, amount):
                    self.process_amount = self.process_amount + int(amount)
            except:
                print("Try an actual number...")
        # BUY INDIVIDUAL
        else:
            if check(resorces.money, self.cost, 1):
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
        print(f"Soldiers Left In Training: {self.process_amount}")
        self.amount += 1
        self.process_amount -= 1


class Resorces:
    def __init__(self, money, rations, med_kit, in_mission):
        self.money = money
        self.rations = rations
        self.med_kit = med_kit
        self.in_mission = in_mission


class Missions:
    def __init__(self, mission_number, name, description, soldiers, heavy, tanks, rations, medical_kits, duration,
                 difficulty, reward):
        self.mission_number = mission_number
        self.name = name
        self.description = description
        self.soldiers = soldiers
        self.heavy = heavy
        self.tanks = tanks
        self.rations = rations
        self.medical_kits = medical_kits
        self.duration = duration
        self.duration_left = duration
        self.difficulty = difficulty
        self.reward = reward

    def info(self):
        return print(f"{self.mission_number} {self.name} - {self.description} (S:{self.soldiers},H:,T:,R:,M:) "
                     f"- Lenght: {self.duration} Hours - Difficulty: {self.difficulty} - ${self.reward}")

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
        resorces.in_mission = True

    def in_mission(self):
        if self.duration_left > 1:
            self.duration_left -= 1
            print(f"{self.name} Mission. T-: {self.duration_left}")
        else:
            resorces.in_mission = False
            lost = random.randrange(0, self.difficulty / 10)
            print(f"\nLoss S:({lost}/{self.soldiers})")
            Unit_Soldiers.amount += self.soldiers - lost
            resorces.money += self.reward
            self.duration_left = self.duration
            print(f"\nMission Complete - Rewarded ${self.reward}")



# Resorces
Money = 1000
Rations = 100
Med_Kit = 0
In_Mission = False
resorces = Resorces(Money, Rations, Med_Kit, In_Mission)

# Troops
Unit_Soldiers = Units("Soldiers", 0, 100, 1, 0)
Unit_Heavy = Units("Heavy", 0, 200, 2, 0)

# Upgrades
Drill_Sargent = False
Drill_Sargent_Cost = 1000

# Missions
In_Mission = False
Evacuate = Missions("1.", "Evacuation", "Evacuate the citizens", 10, 0, 0, 0, 0, 10, 30, 600)


def check(money, cost, amount):
    print(f"-${cost * int(amount)}")
    if money >= cost * int(amount):
        resorces.money -= cost * int(amount)
        return True

    else:
        print("Not enough Money")
        return False
