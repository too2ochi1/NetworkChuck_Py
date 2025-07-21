print("Hello and welcome to JasonBrew!!!!!")

name = input("What is your name?\n")
choice = input("Would you like Tea or Coffee?\n")
if (name == "Ben" or name == "Penny" or name == "Loki") and choice == "Tea":  #Apparently NetworkChuck-sensei determined Loki irredeemable, and also despises tea
    print("You're not welcome here " + name + ". Go away with your trashy " + choice + " taste!!")
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