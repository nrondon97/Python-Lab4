#------------------------------------------------
# Program name – toppings_NayleneRondon.py
# Written by – Naylene Rondon
# Date – Began: 2/8/17
# Description of the program:
# Testing Multiple Lists
#------------------------------------------------

#Start

#Variables
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni",
                      "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

#Loop
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

#End
