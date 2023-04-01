import os

from Menu import menu
import Stats
from Save_Load import load

def Play_Game():
    while Stats.Game:
        menu()

while Stats.Game:
    print("Welcome!\n1.New 2.Load 3.Exit")
    choice = input()

    if choice == "1":
        os.system('cls')
        print("New Game")
        Play_Game()
    elif choice == "2":
        print("Load Game")
        load()
        Play_Game()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Pick an option")

    os.system('cls')
