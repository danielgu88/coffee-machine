water = 400
milk = 540
beans = 120
cups = 9
money = 550

ESPRESSO_WATER = 250
ESPRESSO_BEANS = 16
ESPRESSO_MONEY = 4

LATTE_WATER = 350
LATTE_MILK = 75
LATTE_BEANS = 20
LATTE_MONEY = 7

CAPPUCCINO_WATER = 200
CAPPUCCINO_MILK = 100
CAPPUCCINO_BEANS = 12
CAPPUCCINO_MONEY = 6

DRINK_CUPS = 1

def coffee_machine_state():
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(beans))
    print("{} of disposable cups".format(cups))
    print("${} of money".format(money))

def check_resources(option):
    if option == "1":
        check_espresso()
    elif option == "2":
        check_latte()
    else:
        check_cappuccino()

def check_espresso():
    if water - ESPRESSO_WATER >= 0 and beans - ESPRESSO_BEANS >= 0 and cups - DRINK_CUPS >= 0:
        print("I have enough resources, making you a coffee!\n")
        sell_one_espresso()
    else:
        if water < ESPRESSO_WATER:
            print("Sorry, not enough water!\n")

        if beans < ESPRESSO_BEANS:
            print("Sorry, not enough beans!\n")

        if cups < DRINK_CUPS:
            print("Sorry, not enough cups!\n")

def check_latte():
    if water - LATTE_WATER >= 0 and milk - LATTE_MILK >= 0 \
            and beans - LATTE_BEANS >= 0 and cups - DRINK_CUPS >= 0:
        print("I have enough resources, making you a coffee!\n")
        sell_one_latte()
    else:
        if water < LATTE_WATER:
            print("Sorry, not enough water!\n")

        if milk < LATTE_MILK:
            print("Sorry, not enough milk!\n")

        if beans < LATTE_BEANS:
            print("Sorry, not enough beans!\n")

        if cups < DRINK_CUPS:
            print("Sorry, not enough cups!\n")

def check_cappuccino():
    if water - CAPPUCCINO_WATER >= 0 and milk - CAPPUCCINO_MILK >= 0 \
            and beans - CAPPUCCINO_BEANS >= 0 \
            and cups - DRINK_CUPS >= 0:
        print("I have enough resources, making you a coffee!\n")
        sell_one_cappuccino()
    else:
        if water < CAPPUCCINO_WATER:
            print("Sorry, not enough water!\n")

        if milk < CAPPUCCINO_MILK:
            print("Sorry, not enough milk!\n")

        if beans < CAPPUCCINO_BEANS:
            print("Sorry, not enough beans!\n")

        if cups < DRINK_CUPS:
            print("Sorry, not enough cups!\n")

def sell_one_espresso():
    global water, beans, cups, money

    water -= ESPRESSO_WATER
    beans -= ESPRESSO_BEANS
    cups -= DRINK_CUPS
    money += ESPRESSO_MONEY

def sell_one_latte():
    global water, milk, beans, cups, money

    water -= LATTE_WATER
    milk -= LATTE_MILK
    beans -= LATTE_BEANS
    cups -= DRINK_CUPS
    money += LATTE_MONEY

def sell_one_cappuccino():
    global water, milk, beans, cups, money

    water -= CAPPUCCINO_WATER
    milk -= CAPPUCCINO_MILK
    beans -= CAPPUCCINO_BEANS
    cups -= DRINK_CUPS
    money += CAPPUCCINO_MONEY

action = ""

while action != "exit":
    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        option = input("\nWhat do you want to buy? 1 - espresso,"
                       " 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if option in ["1", "2", "3"]:
            check_resources(option)
        else:
            print()

    elif action == "fill":
        water += int(input("\nWrite how many ml of water do you want to add:\n"))
        milk += int(input("Write how many ml of milk do you want to add:\n"))
        beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()
    elif action == "take":
        print("\nI gave you ${}\n".format(money))
        money -= money
    elif action == "remaining":
        print()
        coffee_machine_state()
        print()
