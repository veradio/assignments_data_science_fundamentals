
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 14:14:40 2018

@author: Vera
"""
#Read the provided csv file and convert the data to a multidimensional list (list with lists)
import csv 

politicians = []


f = open("politicians.csv", "r")
for line in f:
    politicianlist = line.strip().split(",")
    politicians.append(politicianlist) 

#Print the contents of the list properly formatted with the index number 

index=0       
for row in politicians:
    index=index+1
    firstname=row[0]
    lastname=row[1]
    birthyear=row[2]
    politicalparty=row[3]
    print (str(index) + " | The party leader of the " +  politicalparty + " party is " + firstname + " " + lastname + " and is born in " + birthyear  + ".")

print ("  ") #empty space beceause it looks nice
#empty space beceause it looks nice
print("Total politicians in list is " + str(index))

print ("  ") #empty space beceause it looks nice


#Ask for four options: remove a person, add a person, save the database to csv or quit the program.



choosenoption = 0 #menu whileloop when is 0
print("if you want to remove a person type 1")
print("if you want to add a person type 2" )
print ("if you want to save: the database to csv type 3")
print ("if you want to quit the program type 4")


while choosenoption == 0: #menu whileloop when is 0

    choosenoption = int(input("Type your choise "))
#remove a person from list
    if choosenoption == 1:
        print ("remove a person") 
        del_politician = False 
        #whileloop because then the programm wont't end
        while del_politician is False:
            ask_del_politician = int(input("type the index number of the politican you would like to delete, number: ").strip())     
            del politicians[ask_del_politician]
            del_politician = True
        if del_politician is True:
            choosenoption = 0
            print ("What do you want to do next?")      
        else: 
           del_politician = False
           print("print try again")               

#add a person to the list    
    elif choosenoption == 2:
        print ("add a person")
        #‘Add a person’ should ask for the same four fields that also exist in the original CSV file and add those to the list.
        add_firstname = input("Fill in the first name of the politician you'd like to add. Firstname: ").split()
        add_lastname = input ("Fill in the last name of the politician you'd like to add. Lastname: ").split()
        add_birthyear = input("Fill in the year of birth of the politician you'd like to add. Birthyear: ").split()
        add_politicalparty= input("Fill in the political where the politician you'd like to add is the leader. Politicialparty: ").split()
        politicians.append (add_firstname + add_lastname + add_birthyear + add_politicalparty)
        
        print ("--")
        print ("You've added:")
        print (politicians[-1])
        
        print ("What do you want to do next?")   
        choosenoption = 0 #Go back to the menu while loop
        
    elif choosenoption == 3:
        print ("add database to csv")
        with open("politicians.csv","w", newline = "") as writefile:
            writer = csv.writer(writefile)
            writer.writerows(politicians)
            print("Saved")
            print ("What do you want to do next?")   
        choosenoption = 0   #Go back to the menu while loop 
    
    elif choosenoption == 4:
        #The program should indefinitely provide the four options again after an action is completed 
        #until the use chooses the 'quit the program' option.

        print ("quit the program")
        f.close()
        quit()
    
    else: 
        #wrong choise please try again  
        choosenoption = 0
        print ("your choise must be between 1 and 4, please try again:")















