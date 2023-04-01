import Stats
import Create
from time import sleep

import mission
from Save_Load import save

import TimeClock

#TO DO - CHANGE DIRECTORIES
def menu():
    print(f"###############\n"
          f"# TIME: {Stats.Time}:00 ##\n"
          f"###############"
          f"\n\nMoney:${Stats.resorces.money} Rations: {Stats.resorces.rations} Med-Kits:-\n S:{Stats.Unit_Soldiers.amount} H:{Stats.Unit_Heavy.amount}"
          f" T:-\n"
          f"--------------------------------------")
    print(f"1. Create  2. Missions  3. Upgrade \n4. Shop  0. Exit  9. Play\nS. Save\n"
          "--------------------------------------")

    Select = input()
    print(Select)

    if Select == "0":
        print("Exit")
        Stats.Game = False

    elif Select == "1":
        Create.Train()

    elif Select == "2":
        mission.Missions()

    elif Select == "3":
        print("Upgrades: ")
        if not Stats.Drill_Sargent:
            print(f" 1. Drill_Sargent (${Stats.Drill_Sargent_Cost})")
            Select = input()
            if Select == "1":
                if Stats.resorces.money >= Stats.Drill_Sargent_Cost:
                    Stats.resorces.money -= Stats.Drill_Sargent_Cost
                    Stats.Drill_Sargent = True
                    print("Bought Drill_Sargent!")
                else:
                    print("Not enough Money")
        else:
            print("Drill Sargent already bought")


    elif Select == "9":
        print("Pass Time: ")
        amount = input()

        try:
            x = int(amount)
            while x > 0:
                if Stats.Unit_Soldiers.process_amount > 0:
                    #Create
                    Stats.Unit_Soldiers.process()
                x -= 1
                TimeClock.Clock()
                sleep(1)

        except:
            print("Try an actual number")

#Save
    elif Select == "s":
        try:
            save()
            print("Saved")
        except:
            print("Saved Failed!")



