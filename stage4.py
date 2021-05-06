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
    print("{} of money".format(money))

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

coffee_machine_state()

action = input("\nWrite action (buy, fill, take):\n")

if action == "buy":
    option = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n"))

    if option == 1:
        sell_one_espresso()
    elif option == 2:
        sell_one_latte()
    else:
        sell_one_cappuccino()

    print()
elif action == "fill":
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    print()
else:
    print("I gave you ${}\n".format(money))
    money -= money

coffee_machine_state()
