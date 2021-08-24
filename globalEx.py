import time

def level_one():
    print("Welcome!Level One")

def start_game():
    print("Hello and welcome to the game")
    global name
    name = input("Please!Enter your name!")
    print(f"hello{name}")
    time.sleep(1)
    print(f"Would you like to play?[Y/N]:")
    choice = input("Please Enter your Choice")
    if choice == "Yes" or choice == "y" or choice == "yes" or choice == "Y":
        level_one()

start_game()