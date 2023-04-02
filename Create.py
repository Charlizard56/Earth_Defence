import Stats

def Train():
    print(f"Create?\n1. Soldiers(Now: {Stats.Unit_Soldiers.amount})(To be trained: {Stats.Unit_Soldiers.process_amount})"
          f"\n2. Heavy(Now: {Stats.Unit_Heavy.amount})(To be trained: {Stats.Unit_Heavy.process_amount})\n"
          f"3. Tank(Now: {Stats.Unit_Tanks.amount})(To be trained: {Stats.Unit_Tanks.process_amount})\n")
    choice = input()
    #Soldiers
    if choice == "1":
        print("\n1. Buy 2.Sell 3.Cancel")
        choice = input()
        #Buy Soldier
        if choice == "1":
            Stats.Unit_Soldiers.buy(Stats.resorces.money)
        elif choice == "2":
            Stats.Unit_Soldiers.sell()
        elif choice == "3":
            Stats.Unit_Soldiers.cancel()
    elif choice == "2":
        print("\n1. Buy 2.Sell 3.Cancel")
        choice = input()
        # Buy Heavy
        if choice == "1":
            Stats.Unit_Heavy.buy(Stats.resorces.money)
        if choice == "2":
            Stats.Unit_Heavy.sell()
        if choice == "3":
            Stats.Unit_Heavy.cancel()
    elif choice == "3":
        print("\n1. Buy 2.Sell 3.Cancel")
        choice = input()
        # Buy Heavy
        if choice == "1":
            Stats.Unit_Tanks.buy(Stats.resorces.money)
        if choice == "2":
            Stats.Unit_Tanks.sell()
        if choice == "3":
            Stats.Unit_Tanks.cancel()
