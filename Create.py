import Stats

def Train():
    print(f"Create?\n1. Soldiers(To be trained: {Stats.Unit_Soldiers.process_amount})")
    choice = input()
    #Soldiers
    if choice == "1":
        print("\n1. Buy 2.Sell 3.Cancel")
        choice = input()
        #Buy Soldier
        if choice == "1":
            Stats.Unit_Soldiers.buy(Stats.Money)
        elif choice == "2":
            Stats.Unit_Soldiers.sell()
        elif choice == "3":
            Stats.Unit_Soldiers.cancel()