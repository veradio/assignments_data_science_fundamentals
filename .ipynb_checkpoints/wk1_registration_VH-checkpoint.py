#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:34:24 2018

@author: Vera
"""

#Print a welcome statement when the program is run.
print ("welcome to this program")

myfirstname = "Vera" 
mylastname = "Hoogmoed".lower()


#fill in names
firstname = input ("Please fill in your firstname: ")

#Ask for first name of the user and return that with a welcoming message including that name 
print ("Welcome " + firstname + " ,hope you enjoy this platform")


#Ask for the last name of the user and check if the user’s last name is the same as your last name, 
#and if so, should mention that the user is a family member.

lastname = input ("Fill in your lastname? ").lower()
if lastname.lower() == mylastname.lower():
    print ("we are family")
else:
    print ("we are not family")
    

#birtday age calculation
yearnow = 2018

#Your social network is for people of 18 years or older so it should ask for the birth year of the user 
#and determine if they’re old enough for your social network. 
#If the user is not old enough it should give a warning message or exit the program. 

birthyear = input ("fill in your year of birth ")
birthyear = int(birthyear)

current_age = yearnow - birthyear

if current_age > 18:
   print ("your age is " + str(current_age) + ", that means you're old enough.")
else:
    print ("your age is " + str(current_age) + " I'm sorry, you got to go, bye!.")
    import time 
    time.sleep(5)
    exit()
    
#Your code should calculate the estimated value of the user for the advertisers of your social network. 
value = current_age * len(firstname) * birthyear / 1000
print ( "the value of" +firstname + "is " + str (value))


#questions based on age

#Ask for two more questions and give appropriate feedback. 
#What you ask in these two questions and what you answer is up to you.


if current_age <= 28:
   student = input ("are u still a student? Answer with Yes or No").lower()
   if student == "yes":
       print (firstname + "is a poor student, don't try to sell expensive stuff")
   else:
       print (firstname + "is already graduated, must be smart!") 
elif current_age > 28 and current_age <= 35:
    house = input ("do you own a house? answer with yes or no").lower()
    if house == "yes":
        print(firstname + " is maybe interested in a new couch")
    else:
        print ("maybe" + firstname + "is interested in a mortage")
elif current_age > 35 and current_age <= 45:
    baby = input("do you have kids?, Answer with yes or no").lower
    if baby == "yes" :
        print(firstname + "is maybe itnerested in buying dipers")
    else:
        print ("maybe" + firstname + "would be a cat mom?")
else: 
    print: "you're older then 45"


#Print a goodbye statement as the last thing it does

print ("good bye " + firstname + " See you soon!")