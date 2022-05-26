from machine_ressources import resources, MENU


def print_report(resource):
    water = resource["water"]
    milk = resource["milk"]
    coffee = resource["coffee"]
    money = resource["money"]

    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def calculate():
    nb_quarters = int(input("How many quarters?: "))
    nb_dimes = int(input("How many dimes ?: "))
    nb_nickels = int(input("How many nickels ?: "))
    nb_penny = int(input("How many penny ?: "))
    total = nb_quarters*0.25 + nb_dimes*0.1 + nb_nickels*0.05 + nb_penny*0.01
    return total


def reduction(coffee):
    resources["water"] -= coffee["ingredients"]["water"]
    resources["coffee"] -= coffee["ingredients"]["coffee"]
    resources["milk"] -= coffee["ingredients"]["milk"]
    resources["money"] += coffee["cost"]


def compare_resources(coffee):
    result = True
    if coffee["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
        result = False
    elif coffee["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
        result = False
    elif coffee["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
        result = False
    return result


continues = True
while continues:
    choice = input("What would you like? (espresso/latte/cappuccino)")

    if choice == "report":
        print_report(resources)
    elif choice == "off":
        continues = False
        print("Good Bye")
    else:
        drink = MENU[choice]
        enough_resource = compare_resources(drink)

        if enough_resource:
            reduction(drink)
            change = calculate() - drink["cost"]
            if change > 0:
                print(f"Here is {change}$ change")
                print(f"Here is your {choice}, Enjoy it ☕ ")
            else:
                print("Sorry there is not enough money")
