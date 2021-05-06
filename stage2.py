WATER_ONE_CUP = 200
MILK_ONE_CUP = 50
BEANS_ONE_CUP = 15

cups = int(input("Write how many cups of coffee you will need:\n"))

s = ""

if cups > 1:
    s = "s"

print("For {} cup{} of coffee you will need:".format(cups, s))

water = WATER_ONE_CUP * cups
milk = MILK_ONE_CUP * cups
beans = BEANS_ONE_CUP * cups

print("{} ml of water".format(water))
print("{} ml of milk".format(milk))
print("{} g of coffee beans".format(beans))
