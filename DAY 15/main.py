from data import MENU,resources

collected_money = 0.0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


def run_inventory(selected_coffee):
    global collected_money
    global water
    global milk
    global coffee
    
    collected_money += selected_coffee["cost"]
    
    if "water" in selected_coffee["ingredients"]:
        water -= selected_coffee["ingredients"]["water"]
        
    if "milk" in selected_coffee["ingredients"]:
        milk -= selected_coffee["ingredients"]["milk"]
    
    if "coffee" in selected_coffee["ingredients"]:
        coffee -= selected_coffee["ingredients"]["coffee"]
    
def unit_of_measure(ingredient):
    if ingredient == "water":
        return "ml"
    elif ingredient == "milk":
        return "ml"
    elif ingredient == "coffee":
        return "g"
    else:
        return ""
    
def check_if_enough_resources(ingredients):
    is_enough = True
    
    for key in ingredients:
        if is_enough:
            if key == "water":
                is_enough = (water >= ingredients[key])
            elif key == "milk":
                is_enough = (milk >= ingredients[key])
            elif key == "coffee":
                is_enough = (coffee >= ingredients[key])  
                     
    return is_enough

def calculate_coins(quarter, dime, nickel, penny):
    return (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penny * 0.01)

def main():
    
    global water
    global milk
    global coffee
    global collected_money
    
    selection = input("What would you like? (espresso/latte/cappuccino): ")

    if selection != "off":

        if selection == "report":
            print(f"Water: {water}{unit_of_measure('water')}")
            print(f"Milk: {milk}{unit_of_measure('milk')}")
            print(f"Coffee: {coffee}{unit_of_measure('coffee')}")
            print(f"Money: ${collected_money}")
            
        elif selection == "espresso" or selection == "latte" or selection == "cappuccino":
            
            if check_if_enough_resources(MENU[selection]["ingredients"]):
                
                coffee_cost = MENU[selection]["cost"]
                
                print("Please insert coins.")
                quarter_count = int(input("How many quarters?: "))
                dime_count = int(input("How many dimes?: "))
                nickel_count = int(input("How many nickels?: "))
                penny_count = int(input("How many pennies?: "))
                
                total_inserted_coins = calculate_coins(quarter_count, dime_count, nickel_count, penny_count)
                
                if total_inserted_coins >= coffee_cost:
                   
                    total_change = total_inserted_coins - coffee_cost
                    
                    if total_change > 0:
                        print(f"Here is ${round(total_change, 2)} dollars in change.")
                        
                    print(f"Here is your {selection}. Enjoy!")
                    
                    run_inventory(MENU[selection])
                    
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough ingredients.")       
        main()           
                     
main()            