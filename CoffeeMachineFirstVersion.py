MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

options = MENU.copy()
remaining_resources = resources.copy()
money = 0
turning_machine_off = False
while not turning_machine_off:
    ingredients_missing = False
    short_on_money = False
    selection = input("What would you like? (espresso/latte/cappuccino)")
    if selection == 'report':
        print(f"Water: {remaining_resources['water']}ml\nMilk: {remaining_resources['milk']}ml\n"
              f"Coffee: {remaining_resources['coffee']}g\nMoney: ${money}")
    elif selection != 'off':
        my_choice = options[selection]
        if selection == 'espresso':
            my_choice['ingredients']['milk'] = 0
        for key in remaining_resources:
            if remaining_resources[key] < my_choice['ingredients'][key]:
                print(f"Sorry, there is not enough {key}.\n")
                ingredients_missing = True
        if not ingredients_missing:
            inserted_quarters = float(input("How many quarters: "))
            inserted_dimes = float(input("How many dimes: "))
            inserted_nickles = float(input("How many nickles: "))
            inserted_pennies = float(input("How many pennies: "))
            total_sum = (inserted_quarters * QUARTERS + inserted_dimes * DIMES + inserted_nickles * NICKLES +
                         inserted_pennies * PENNIES)
            if total_sum < my_choice['cost']:
                print("Sorry, that is not enough money. Money refunded.")
                short_on_money = True
            elif total_sum > my_choice['cost']:
                change = total_sum - my_choice['cost']
                print("Here is ${:.2f}".format(change))
        if not ingredients_missing and not short_on_money:
            for key in remaining_resources:
                remaining_resources[key] = remaining_resources[key] - my_choice['ingredients'][key]
            money += my_choice['cost']
            print(f"Here is your {selection}. Enjoy")
    elif selection == 'off':
        turning_machine_off = True

    # print(remaining_resources, money)
