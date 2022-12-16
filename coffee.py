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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO: 1 print report of all coffee matchine recources.
def is_recource_sufficient(order_ingredients):
    """Check and confirm is the available resources are enough"""
    is_enough = True
    for item in order_ingredients:
       if order_ingredients[item] >= resources[item]:
           print(f"sorry there is no enough {item}")

           is_enough=False

       return is_enough
def process_coins():
    print("Insert coins: ")
    total = int(input("how many quarters?: "))* 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, cost_of_drink):
    """return true when the payment is accepted and false is insufficient"""
    if money_received >= cost_of_drink:
        change = round(money_received- cost_of_drink, 2)
        print(f"Here is your balance:  ${change}")
        global money
        money +=cost_of_drink
        return True
    else:
        print("Insufficient funds: Money refunded.")
        return False
def make_coffee(drink_name, order_ingredients):
    """reduce the required ingredients from the resources to make coffee"""
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"All done: Here is your {drink_name}")
    
is_on= True
while is_on:
 choice =input("What type of coffee would you like?(latte/espresso/cappuccino):")
 if choice =="off":
     is_on = False
 elif choice =="report":
    print(f"water:{resources['water']} ml")
    print(f"milk:{resources['milk']}ml")
    print(f"coffee:{resources['coffee']}g")
    print(f"money: ${money}")
 else:
     drink = MENU[choice]
     if is_recource_sufficient(drink["ingredients"]):
         payment = process_coins()
         if  is_transaction_successful(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])













