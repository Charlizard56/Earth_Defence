import Stats

def Clock():
    if Stats.Time == 23:
        Stats.Time = 0
        print(f"It's a new day! (Rations: {Stats.resorces.rations} > {Stats.resorces.rations - Stats.Unit_Soldiers.amount})")
        Stats.resorces.rations -= Stats.Unit_Soldiers.amount
    else:
        Stats.Time += 1
    if Stats.resorces.rations <= 0:
        Stats.resorces.rations= 0

        print("NO RATIONS! MEN HAVE LEFT YOUR GROUP!")

        #LOST
        Stats.Unit_Soldiers.amount -= 1
        if Stats.Unit_Soldiers.amount < 0:
            Stats.Soldiers = 0

    print(f"Time: {Stats.Time}:00")