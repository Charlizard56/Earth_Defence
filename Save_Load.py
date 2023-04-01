import Stats

def save():
    # Write
    file2write = open("Save_File", 'w')
    #Set Bools
    if Stats.Drill_Sargent:
        x = 1
    else:
        x = 0
    file2write.write(f"Money:{str(Stats.resorces.money)} Rations:{str(Stats.resorces.rations)} "
                     f"Soldiers:{str(Stats.Unit_Soldiers.amount)} Drill_Sargent:{x} Time:{Stats.Time} "
                     f"Heavy:{str(Stats.Unit_Heavy.amount)} end")
    file2write.close()

def load():
    # READ
    f = open('Save_File', 'r')

    new = f.readline()
    f.close()

    list = []

    t = ""

    n_line = False
    for x in new:
        if n_line:
            t += x
        if x == ":":
            n_line = True
        elif x == " ":
            n_line = False
            list.append(t)
            t = ""

    print(list)

    #Change Variables
    Stats.resorces.money = float(list[0])
    Stats.resorces.rations = int(list[1])
    Stats.Unit_Soldiers.amount = int(list[2])
    Stats.Drill_Sargent = int(list[3])
    Stats.Drill_Sargent = bool(Stats.Drill_Sargent)
    Stats.Time = int(list[4])
    Stats.Unit_Heavy.amount = int(list[5])
    print(Stats.Drill_Sargent)
    print(type(Stats.Drill_Sargent))

