import Stats
import Create
from time import sleep

import mission
from Save_Load import save

import TimeClock


def menu():
    print(f"###############\n"
          f"# TIME: {Stats.Time}:00 ##\n"
          f"###############"
          f"\n\nMoney:${Stats.resorces.money} Rations: {Stats.resorces.rations} Med-Kits:-\n "
          f"S:{Stats.Unit_Soldiers.amount} H:{Stats.Unit_Heavy.amount}"
          f" T:-\n"
          f"--------------------------------------")
    print(f"1. Create  2. Missions  3. Hires \n4. Shop  0. Exit  9. Play\nS. Save\n"
          "--------------------------------------")

    Select = input()
    print(Select)

    #EXIT
    if Select == "0":
        print("Exit")
        Stats.Game = False
    #TRAIN SOLDIERS,HEAVY,& TANKS
    elif Select == "1":
        Create.Train()
    #MISSIONS
    elif Select == "2":
        mission.Missions()
    #HIRE
    elif Select == "3":
        print("Hires: ")
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
                x -= 1
                TimeClock.Clock()
                sleep(1)
                if Stats.Unit_Soldiers.process_amount > 0:
                    #Create
                    Stats.Unit_Soldiers.process()
                if Stats.resorces.in_mission:
                    Stats.Evacuate.in_mission()

        except:
            print("Try an actual number")

#Save
    elif Select == "s":
        try:
            save()
            print("Saved")
        except:
            print("Saved Failed!")



