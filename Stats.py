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
        self.process_time_left = process_time
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
                while self.process_time_left > 0:
                    TimeClock.Clock()
                    self.process_time_left -= 1
                    sleep(1)
                self.process_time_left = self.process_time



    def sell(self):
        if self.amount > 0:
            print(f"How many?({self.amount}): ")
            x = input()
            if int(x) > 0 and int(x) <= self.amount:
                total = self.cost / 2 * int(x)
                print(total)
                resorces.money += total
                self.amount -= int(x)
                print(f"{x} {self.name}(s) Sold for {total}")
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
        if self.process_time_left <= 0:
            self.amount += 1
            self.process_amount -= 1
            self.process_time_left = self.process_time
        else:
            self.process_time_left -= 1
        print(f"{self.name}(s) Left In Training: {self.process_amount}")


class Resorces:
    def __init__(self, money, rations, med_kit, in_mission):
        self.money = money
        self.rations = rations
        self.ration_price = 10
        self.med_kit = med_kit
        self.med_kit_price = 50
        self.in_mission = in_mission

    def buy_med_kit(self):
        print(f"How many?({self.med_kit}): ")
        amount = input()
        if check(self.money,self.med_kit_price,amount):
            print(f"Bought {amount} Med-Kit(s)")
            self.med_kit += int(amount)
        else:
            print("Not enough money")

    def buy_rations(self):
        print(f"How many?({self.rations}): ")
        amount = input()
        if check(self.money,self.ration_price,amount):
            print(f"Bought {amount} Ration(s)")
            self.rations += int(amount)
        else:
            print("Not enough money")


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
Money = 10000
Rations = 0
Med_Kit = 5
In_Mission = False
resorces = Resorces(Money, Rations, Med_Kit, In_Mission)

# Troops
Unit_Soldiers = Units("Soldiers", 0, 100, 1, 0)
Unit_Heavy = Units("Heavy", 0, 200, 2, 0)
Unit_Tanks = Units("Tank", 0, 500, 3, 0)

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
