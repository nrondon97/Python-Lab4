#Purpose: Depicts a simple if statement determining if eligible to vote.
#2-Alternative Decision
#Date: 1/25/17
#Programmer: Naylene Rondon
#FileName: voting_NayleneRondon.py

#Start
print("Are you old enough to vote?")

#Variable
age = int(input("Enter your age: ")) #Input

#Decision
if age >= 18:
    print("You are old enough to vote.") #Output if True
    print("Have you registered yet?")
else:
    print("Sorry, you're too young to vote.") #Output if False
    print("Register when you become 18.")

#End
