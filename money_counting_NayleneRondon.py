#------------------------------------------------
# Program name – money_counting_NayleneRondon.py
# Written by – Naylene Rondon
# Date – Began: 2/8/17
# Description of the program:
#Create a change-counting game that gets the
#user to enter the number of coins requires to
#make exact exactly one dollar.
#------------------------------------------------

#Start

#Variables
pennies = float(.01)
nickels = float(.05)
dimes = float(.10)
quarters = float(.25)

#Input
p_value = int(input("How many pennies do you have? "))
n_value = int(input("How many nickels do you have? "))
d_value = int(input("How many dimes do you have? "))
q_value = int(input("How many quarters do you have? "))

#Process
money = float((p_value * pennies) + (n_value * nickels) + (d_value * dimes) + (q_value * quarters))

#Decision
if money == 1:
    print("You have exactly $1.")
elif money > 1:
    print("You have $" + str(money)+". You have more than $1. ")
else:
    print("You have $" + str(money)+". You have less than $1. ")

#End
