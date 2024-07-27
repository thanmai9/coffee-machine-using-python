import time

# Initialize initial quantities
milk = 50       #millilitres
coffee = 50     #grams
sugar = 50      #grams
water = 500    #milliliters
cups = 10       #number of cups
money_earned = 0 #rupees

# Define coffee recipes
latte = {
    "price": 150,
    "milk": 5,
    "sugar": 10,
    "coffee": 15,
    "water": 100
}

cappuccino = {
    "price": 100,
    "milk": 12,
    "sugar": 15,
    "coffee": 20,
    "water": 150
}

espresso = {
    "price": 70,
    "milk": 0,
    "sugar": 20,
    "coffee": 30,
    "water": 50
}

def make_coffee(recipe, ask_sugar=True):
    global milk, sugar, coffee, water, cups, money_earned

     # Get user input for denominations
    ten = int(input("Enter number of 10 rs note:\n"))
    twenty = int(input("Enter number of 20 rs note:\n"))
    fifty = int(input("Enter number of 50 rs note:\n"))
    hundred = int(input("Enter number of 100 rs note:\n"))
    two_hundred = int(input("Enter number of 200 rs note:\n"))

    # Calculate total amount
    total = ten * 10 + twenty * 20 + fifty * 50 + hundred * 100 + two_hundred * 200

    if total >= recipe["price"]:
        if milk >= recipe["milk"] and coffee >= recipe["coffee"] and sugar >= recipe["sugar"] and water >= recipe["water"] and cups >= 1:
            # Check if the user wants to specify sugar amount
            if ask_sugar:
                sugar_preference = input("Do you want to specify the amount of sugar? (yes/no):\n").lower()
                if sugar_preference == "yes":
                    sugar_amount = int(input("Enter the amount of sugar (in grams) you want in your coffee:\n"))
                    if sugar_amount > sugar:
                        print("Insufficient sugar.")
                        return
                else:
                    sugar_amount = recipe["sugar"]
            else:
                sugar_amount = recipe["sugar"]

            change = total - recipe["price"]
            milk -= recipe["milk"]
            coffee -= recipe["coffee"]
            sugar -= sugar_amount
            water -= recipe["water"]
            cups -= 1
            money_earned += recipe["price"]
            print("Preparing your coffee....")
            time.sleep(3)
            print("Here is your coffee:\n")
            print("Change left =", change,"\n")
        else:
            print("Resources not sufficient to make the coffee :(")
    else:
        print("Not enough amount entered :(")
        
def custom_coffee():
    global milk, sugar, coffee, water, cups, money_earned

    print("Creating a Custom Coffee:")
    custom_price = 350
    custom_milk = int(input("Enter the amount of milk (in ml):\n"))
    custom_sugar = int(input("Enter the amount of sugar (in grams):\n"))
    custom_coffee = int(input("Enter the amount of coffee (in grams):\n"))
    custom_water = int(input("Enter the amount of water (in ml):\n"))
    
     # Get user input for denominations
    ten = int(input("Enter number of 10 rs note:\n"))
    twenty = int(input("Enter number of 20 rs note:\n"))
    fifty = int(input("Enter number of 50 rs note:\n"))
    hundred = int(input("Enter number of 100 rs note:\n"))
    two_hundred = int(input("Enter number of 200 rs note:\n"))

    # Calculate total amount
    total = ten * 10 + twenty * 20 + fifty * 50 + hundred * 100 + two_hundred * 200

    if milk >= custom_milk and coffee >= custom_coffee and sugar >= custom_sugar and water >= custom_water and cups >= 1:
        change = total - custom_price
        milk -= custom_milk
        coffee -= custom_coffee
        sugar -= custom_sugar
        water -= custom_water
        cups -= 1
        money_earned += custom_price
        print("Preparing your custom coffee....")
        time.sleep(3)
        print("Here is your custom coffee:\n")
        print("Change left =", change)
    else:
        print("Resources not sufficient to make the custom coffee :(") 


def report():
    global milk, sugar, coffee, water, cups
    print("Milk left =", milk," ml")
    print("Sugar left =", sugar," grams")
    print("Coffee left =", coffee," grams")
    print("Water left =", water," ml")
    print("Cups left =", cups)
    print("Money earned is", money_earned,"Rs.\n")

def refill():
    global milk, sugar, coffee, water, cups
    s = int(input("Enter the amount of sugar (in grams) to refill:\n"))
    c = int(input("Enter the amount of coffee (in grams) to refill:\n"))
    m = int(input("Enter the amount of milk (in ml) to refill:\n"))
    w = int(input("Enter the amount of water (in ml) to refill:\n"))
    cu = int(input("Enter the number of cups to refill:\n"))
    milk += m
    coffee += c
    sugar += s
    water += w
    cups += cu

def coffee_machine():
    while True:
        print("Price of Latte is 150Rs.\nPrice of Cappuccino is 100Rs.\nPrice of Espresso is 70Rs.\nPrice of Custom Coffee is 300Rs.\n")
        user_choice = input("Enter among the below options:\n1. Latte\n2. Cappuccino\n3. Espresso\n4. Custom Coffee\n5. Report\n6. Refill\n7. Exit\n\n")
        if user_choice == "1":
            make_coffee(latte)
        elif user_choice == "2":
            make_coffee(cappuccino)
        elif user_choice == "3":
            make_coffee(espresso)
        elif user_choice == "4":
           custom_coffee()
        elif user_choice == "5":
            report()
        elif user_choice == "6":
            refill()
        elif user_choice == "7":
            print("Exiting the coffee machine.")
            break
        else:
            print("Invalid choice, please try again.\n")

# Start the coffee machine
coffee_machine()