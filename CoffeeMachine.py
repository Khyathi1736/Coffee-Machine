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

Money=0

def coins(user_input):
    global MENU,resources,Money    #to use global variables in function we need to first declare them like this.
    #if any ingredient is not available to make the input item
    if MENU[user_input]["ingredients"]["water"]>resources["water"]:
        print("Sorry,There is not enough water.")
    elif user_input!="espresso" and MENU[user_input]["ingredients"]["milk"]>resources["milk"] :
        print("Sorry,There is not enough milk.")
    elif MENU[user_input]["ingredients"]["coffee"]>resources["coffee"]:
        print("Sorry,There is not enough coffee.")
    else:
        print("Please input coins:")
        quarters=int(input("How many quarters?:"))
        dimes=int(input("How many dimes?:"))
        nickles=int(input("How many nickles?:"))
        pennies=int(input("How many pennies?:"))
        total=(quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
        cost=MENU[user_input]["cost"]
        Money+=cost
        change=total-cost
        change=round(change,2)  #to format float to print only upto 2 decimal places.
        if change<0:
            print("Sorry ther is not enough money.")
        else:
            resources["water"]=resources["water"]-MENU[user_input]["ingredients"]["water"]
            if user_input!="espresso":              #because espresso doesn't contain key named milk since it is not required.
                resources["milk"]=resources["milk"]-MENU[user_input]["ingredients"]["milk"]
            resources["coffee"]=resources["coffee"]-MENU[user_input]["ingredients"]["coffee"]
            print(f"Here is your ${change} in change.")
            print(f"Here is your {user_input},Enjoy pandgoww!")



while 1:
    user_input=input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input=="report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${Money}")
    elif user_input=="latte":
        coins(user_input)
    elif user_input=="espresso":
        coins(user_input)
    elif user_input=="cappuccino":
        coins(user_input)
    elif user_input=="off":
        exit()
    else:
        print("Enter correct input boshidikeee.......")



    
