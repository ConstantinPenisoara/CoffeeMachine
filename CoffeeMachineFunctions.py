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


def check_ingredients(available_resources, choice):
    """Checks if there are enough ingredients"""
    missing_ingredients_list = []
    for resource in available_resources:
        if available_resources[resource] < choice['ingredients'][resource]:
            missing_ingredients_list.append(resource)

    if len(missing_ingredients_list) == 0:
        return False
    else:
        return True


def which_ingredient(available_resources, choice):
    """Outputs which ingredient is missing"""
    if available_resources['water'] < choice['ingredients']['water']:
        return f"Sorry, there is not enough water."
    elif available_resources['milk'] < choice['ingredients']['milk']:
        return f"Sorry, there is not enough milk."
    elif available_resources['coffee'] < choice['ingredients']['coffee']:
        return f"Sorry, there is not enough coffee."


def inserted_sum():
    """Calculates how much money you inserted into the coffee machine"""
    inserted_quarters = float(input("How many quarters: "))
    inserted_dimes = float(input("How many dimes: "))
    inserted_nickles = float(input("How many nickles: "))
    inserted_pennies = float(input("How many pennies: "))
    my_sum = (inserted_quarters * QUARTERS + inserted_dimes * DIMES + inserted_nickles * NICKLES +
              inserted_pennies * PENNIES)
    return my_sum


def coffee_machine():
    money = 0
    turning_machine_off = False
    while not turning_machine_off:
        # ingredients_missing = False
        short_on_money = False
        selection = input("What would you like? (espresso/latte/cappuccino)")
        if selection == 'report':
            print(f"Water: {remaining_resources['water']}ml\nMilk: {remaining_resources['milk']}ml\n"
                  f"Coffee: {remaining_resources['coffee']}g\nMoney: ${money}")
        elif selection != 'off':
            my_choice = options[selection]
            if selection == 'espresso':
                my_choice['ingredients']['milk'] = 0
            ingredients_missing = check_ingredients(remaining_resources, my_choice)
            if ingredients_missing:
                print(which_ingredient(remaining_resources, my_choice))
            elif not ingredients_missing:
                total_sum = inserted_sum()
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
                print(f"Here is your {selection}. Enjoy!")
        elif selection == 'off':
            turning_machine_off = True


coffee_machine()
