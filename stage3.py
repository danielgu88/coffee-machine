WATER_ONE_CUP = 200
MILK_ONE_CUP = 50
BEANS_ONE_CUP = 15

def cups_available(water, milk, beans):
    if water == 0 or milk == 0 or beans == 0:
        return 0

    cups_available = 0

    while True:
        if water - WATER_ONE_CUP >= 0 and milk - MILK_ONE_CUP >= 0 and beans - BEANS_ONE_CUP >= 0:
            cups_available += 1
            water -= WATER_ONE_CUP
            milk -= MILK_ONE_CUP
            beans -= BEANS_ONE_CUP
        else:
            break

    return cups_available

water = int(input("Write how many ml of water the coffee machine has:\n"))
milk = int(input("Write how many ml of milk the coffee machine has:\n"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups_needed = int(input("Write how many cups of coffee you will need:\n"))

cups_available = cups_available(water, milk, beans)

if cups_available == cups_needed:
    print("Yes, I can make that amount of coffee")
elif cups_available > cups_needed:
    print("Yes, I can make that amount of coffee (and even {} more than that)"
          .format(cups_available - cups_needed))
else:
    print("No, I can make only {} cups of coffee".format(cups_available))
