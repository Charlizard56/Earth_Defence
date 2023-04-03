import Stats

def Clock():
    if Stats.Time == 23:
        Stats.Time = 0
        x = Stats.Unit_Soldiers.amount + Stats.Unit_Heavy.amount + Stats.Unit_Tanks.amount
        if x < 0:
            Stats.resorces.rations += x
        else:
            Stats.resorces.rations = 0
        print(f"It's a new day! (Rations: {Stats.resorces.rations} > {Stats.resorces.rations - x})")
    else:
        Stats.Time += 1
    if Stats.resorces.rations <= 0:
        Stats.resorces.rations= 0

        print("NO RATIONS! MEN HAVE LEFT YOUR GROUP!")

        #LOST

        Stats.Unit_Soldiers.amount -= 1
        Stats.Unit_Heavy.amount -= 1
        Stats.Unit_Tanks.amount -= 1
        if Stats.Unit_Soldiers.amount < 0:
            Stats.Unit_Soldiers.amount = 0
        if Stats.Unit_Heavy.amount < 0:
            Stats.Unit_Heavy.amount = 0
        if Stats.Unit_Tanks.amount < 0:
            Stats.Unit_Tanks.amount = 0


    print(f"Time: {Stats.Time}:00")