print("Hello and welcome to JasonBrew!!!!!")

name = input("What is your name?\n")

if name == "Ben":
    print("You're not welcome here. Go away")
    exit()
else:
    print("Hello " + name + ", thanks for coming in today.")
    print("""Here's our menu:
        1. Black Coffee
        2. Latte
        3. Cafe Mocha""")

    drink = input("What would you like to drink?\n")

    price = 500

    print("Alright then, " + drink + " costs #" + str(price) + " per cup.")

    number = input("How many cups would you be needing?\n")

    total_cost = int(number) * price

    print("That'd be a total of #" + str(total_cost) )
    print("Here you go, enjoy your " + number + " cups of "+ drink + "!")