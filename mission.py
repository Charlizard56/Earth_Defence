import Stats

def Missions():
    if not Stats.resorces.in_mission:
        print(f"\nChoose Mission:")
        Stats.Evacuate.info()
        choice = input()
        if choice == "1":
            Stats.Evacuate.check_amount()
    else:
        print("Already in mission")
