# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set empty order list.
order= {}


# Launchs the store and presents a greeting to the customer
print("Welcome to the variety food truck.")


place_order = True #Variable to keep the order loop running

while place_order:
    # Asks the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Creates a variable for the menu item number
    i = 1
    # Creates a dictionary to store the menu for later retrieval
    menu_items = {}

    # Prints the options to choose from menu headings
    for key in menu.keys():
        print(f"{i}: {key}")
        # Stores the menu category associated with its menu item number
        menu_items[i] = key
        # Adds 1 to the menu item number
        i += 1

    # Gets the customer's input
    menu_category = input("Type menu number: ")

    # Checks if the customer's input is a number
    if menu_category.isdigit():
        # Checks if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Saves the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Prints out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Prints out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Checks if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            #Asks customer to input for menu item number
            menu_item_number = input("Type menu item number: ")

            if menu_item_number.isdigit():

                if int(menu_item_number) in menu_items.keys():
                    # Stores the menu item name as a variable
                    item_name = menu_items[int(menu_item_number)]["Item name"]
                    # Asks the customer for the quantity of the menu item
                    quantity = input("How many would you like to order? ")
                    # Checks if the quantity is a number, sets default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    # Adds the item name, price, and quantity to the previously empty order list
                    order[item_name] = {
                        "Price": menu_items[int(menu_item_number)]["Price"],
                        "Quantity": quantity
                    }
                else:
                    print("You didn't select a menu option.")

        else:
            # Tells the customer they if didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tells the customer if they didn't select a number
        print("You didn't select a number.")

    while True:
        # Asks the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()

        match keep_ordering:
            case "y": #keep ordering
                break
            case "n": #complete order
                place_order = False 
                print("Thank you for your order.")
                break
            case _:
                print("Please try again, make sure to type (Y)es or (N)o.") 


# Prints out the customer's order
print("This is what we are preparing for you.\n")
print("Item name                | Price   | Quantity")
print("-------------------------|---------|----------")

for item_name, details in order.items():
    #Stores the dictionary items as variables
    price = details["Price"]
    quantity = details["Quantity"]
    # Calculates the number of spaces needed for formatting
    item_name_spaces = " " * (24 - len(item_name))
    price_spaces = " " * (6 - len(f"{price:.2f}"))
    
    # Prints the item name, price, and quantity
    print(f"{item_name}{item_name_spaces} | ${price:.2f}{price_spaces} | {quantity}")
print("----------------------------------------------")

#Calculating the cost of the order by multiplying the price by quantity for each item in the order list, then sum()
# and print the prices.
if order:
    total_price = sum(details["Price"] * details["Quantity"] for details in order.values())
    total_quantity = sum(details["Quantity"] for details in order.values())
    total_spaces = " " * (24 - len("Total:"))
    print(f"Total:{total_spaces} | ${total_price:.2f} | {total_quantity}")
