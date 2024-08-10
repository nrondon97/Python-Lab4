#------------------------------------------------
# Program name – LoanQualifier_NayleneRondon.py
# Written by – Naylene Rondon
# Date – Began: 2/8/17
# Description of the program:
#Practice working with flowcharts, if statements,
#and loops.
#Qualification for a loan with a min of
#$30,000 and 2 years.
#------------------------------------------------

#Start
print("Do you qualify for a loan?")

#Control Loop Variable
try_again = "y" 

#Loop
while(try_again == "y"):

    #Input & Variables
    salary = float(input("\nWhat is your salary?" ))
    years_on_job = int(input("How many years have you been working at your current job? "))

    print("You entered " + str(salary) + " for your salary and " + str(years_on_job) + " years at your current job.") #Input check

    #First Decision
    if salary >= 30000:
        if years_on_job >= 2:   #Second Decision
            print("You qualify for the loan.") #Ouput if both values are true
        else:
            print("You must have been at your current job for at least two year to qualify.") #Output for false statement for second decision
    else:
        print("You must earn at least $30,000 per year to qualify.")  #Output for false statement for first decision
    try_again = input("\nDo you want to try again? (y/n)")
    
#End
