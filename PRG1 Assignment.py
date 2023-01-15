'''
Student name: Leong Kai En, Matthew
Student ID: S10204010C
Class: P09/T09
Date: 9 August 2021
'''
import random

#Lists
option_list = ["3. See remaining buildings", "4. See current score", "5. Save game", "0. Exit to main menu"]

#To count the number of remaining building
building_list = ["HSE","HSE","HSE","HSE","HSE","HSE","HSE","HSE",\
                 "BCH","BCH","BCH","BCH","BCH","BCH","BCH","BCH",\
                 "SHP","SHP","SHP","SHP","SHP","SHP","SHP","SHP",\
                 "FAC","FAC","FAC","FAC","FAC","FAC","FAC","FAC",\
                 "HWY","HWY","HWY","HWY","HWY","HWY","HWY","HWY"]

SHP_build = ["HSE", "BCH", "SHP", "FAC", "HWY"] #Used for SHP score later on
SHP_build2 = ["HSE", "BCH", "SHP", "FAC", "HWY", " "] #Used for SHP score

grid = [ [' ', ' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' ', ' ']
         ]
#For input validation to ensure that the input is correct by first finding what are the acceptable options
potential_option = ['A1', 'A2', 'A3', 'A4', 
                    'B1', 'B2', 'B3', 'B4', 
                    'C1', 'C2', 'C3', 'C4', 
                    'D1', 'D2', 'D3', 'D4', 
                    'a1', 'a2', 'a3', 'a4',
                    'b1', 'b2', 'b3', 'b4', 
                    'c1', 'c2', 'c3', 'c4', 
                    'd1', 'd2', 'd3', 'd4']

max_row = len(grid) - 1
max_col = len(grid[0]) - 1


#------------------------------------------Define functions----------------------------------------#

def table():
    
    print("     A     B     C     D")
    print(" ","+-----+-----+-----+-----+")
    for row in range(1, max_row):
        print(' {}'.format(row), end = '') #End = '' used to place a space instead of going to a new line
        for column in range(1, max_col):
            print("| {:3} ".format(grid[row][column]), end = '')
        print('|')
        print(" ","+-----+-----+-----+-----+")
        

def ranNum():
    #Generating a random number which will be used to display 2 random buildings for the user to built
    index1 = random.randint(0, (len(building_list) -1))
    building1 = building_list[index1]

    
    index2 = random.randint(0, (len(building_list) -1))
    building2 = building_list[index2]

    list = [index1, index2]
    return list


def options(building_list, option_list):
    #Made use of the ranNum function to create 2 random building
    print("1. Build a {}".format(building_list[indexes[0]]))
    print("2. Build a {}".format(building_list[indexes[1]]))

    
    for i in range(len(option_list)):
        print(option_list [i])
        
        if i == 1: #Gap between current score and save game
            print()

def remaining_buildings():
    #Print the remaining number of building from the building list
    print()
    print("{:10s} {:15s}".format("Building", "Remaining"))
    print("{:10s} {:15s}".format("--------", "---------"))
    
    print("{:10s} {:<15}".format("HSE", building_list.count("HSE")))
    print("{:10s} {:<15}".format("FAC", building_list.count("FAC")))
    print("{:10s} {:<15}".format("SHP", building_list.count("SHP")))
    print("{:10s} {:<15}".format("HWY", building_list.count("HWY")))
    print("{:10s} {:<15}".format("BCH", building_list.count("BCH")))
    print()
        


def HighScores_load():
    file = open("HighScores.txt", "r")
    print(file.read())
    
    
    


def load():
    global Turn
    file = open("saveFile.txt","r")
    r = 0
    Turn = int(file.readline()) #Reading the first line of the file for the turn number
    for line in file:
        line = line.strip('\n') #Get rid of \n
        gameFile = line.split(',')
        
        for c in range (0,6):
            grid[r][c] = gameFile[c]
        r += 1

        if r == 6: #Stops the reading at row 6 as it is the last row that is needed
            break
        
    line = file.readline().strip('\n')    #Removes the \n from the file
    building_list_load = line.split(',')
    file.close()



def save():
    file = open("saveFile.txt","w")
    file.write(str(Turn) + "\n") #Saving the Turn number
    for r in range(0 , 6):
        position = ""
        for c in range(0, 6):
            position = position + grid[r][c] + ','
        file.write(position + '\n')
    file.close()

    

def score_BCH():
    score_BCH = 0
    score_BCH_list = []
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == "BCH":
                if c == 1 or c == 4: #IF BCH is in column A or D i.e. column 1 and 2
                    score_BCH += 3
                else:
                    score_BCH += 1

            if score_BCH > 0:        
                score_BCH_list.append(score_BCH)
                score_BCH = 0

    return score_BCH_list #Returning multiple values in the form of a list

def score_FAC():
    FAC = []
    num_FAC = 0
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == "FAC":
                num_FAC += 1
                
    if num_FAC <= 4:
        score_FAC = num_FAC * num_FAC

    else: 
        score_FAC = 16 + (num_FAC - 4)

    FAC.append(num_FAC)
    FAC.append(score_FAC)
    return FAC

def score_HSE(grid, score_HSE):
    score_HSE_List = []
    part_score = 0
    num_FAC = 0
    num_HSEnSHP = 0
    num_BCH = 0

    #CHECK IF len(grid) - 1 is correct
    for r in range(1, max_row):
        for c in range (1, max_col):
            if grid[r][c] == "HSE":

                #If adajacent is a Factory
                if grid[r - 1][c] == "FAC" or grid[r + 1][c] == "FAC"  or grid[r][c - 1] == "FAC"  or grid[r][c + 1] == "FAC" :
                    num_FAC += 1

                #If adajacent is house or shop    
                if grid[r - 1][c] == "HSE" or grid[r - 1][c] == "SHP":
                    num_HSEnSHP += 1

                if grid[r + 1][c] == "HSE" or grid[r + 1][c] == "SHP":
                    num_HSEnSHP += 1

                if grid[r][c - 1] == "HSE" or grid[r][c - 1] == "SHP":
                    num_HSEnSHP += 1

                if grid[r][c + 1] == "HSE" or grid[r][c + 1] == "SHP" :
                    num_HSEnSHP += 1

                #If adajaced is a beach
                if grid[r - 1][c] == "BCH":
                    num_BCH += 1

                if grid[r + 1][c] == "BCH":
                    num_BCH += 1

                if grid[r][c - 1] == "BCH":
                    num_BCH += 1

                if grid[r][c + 1] == "BCH":
                    num_BCH += 1

                #Calculating each score
                if num_HSEnSHP > 0:
                    part_score += num_HSEnSHP 

                if num_BCH > 0:
                    part_score += 2 * (num_BCH)

                #If next to Factory it is 1
                if num_FAC >= 1:
                    part_score = 1

                score_HSE_List.append(part_score)

                #Resetting back to 0
                part_score = 0
                num_FAC = 0
                num_HSEnSHP = 0
                num_BCH = 0

        
    return score_HSE_List                
    

def score_SHP():
    adj_list = []
    score_SHP_List = []
    for r in range(max_row):
        for c in range(max_col):
            if grid[r][c] == "SHP":

                adj_list.append(grid[r - 1][c])
                adj_list.append(grid[r + 1][c])
                adj_list.append(grid[r][c + 1])
                adj_list.append(grid[r][c - 1])
                
                #If adajacent grid is not complete
                if grid[r-1][c] == ' ' or grid[r+1][c] == ' ' or grid[r][c+1] == ' ' or grid[r][c-1] == ' ':
                    count = 5
                    for i in range(0, len(SHP_build)):
                        if SHP_build2[i] not in adj_list:
                            count -= 1
                        
                #If adajacent grid is completed
                else:
                    count = 4
                    for i in range(0, len(SHP_build)):
                        if SHP_build[i] not in adj_list:
                            count -= 1
                        
                score_SHP_List.append(count)
                adj_list = []

    return score_SHP_List
    

def score_HWY():
    score_HWY = []
    
    for r in range(0, len(grid)):
        for c in range(0, len(grid)):
            if grid[r][c] == "HWY":

                if grid[r][c-1] != 'HWY':
                    score = 0
                    while grid[r][c] == 'HWY':
                        score += 1
                        c += 1

                for p in range(score):
                    score_HWY.append(score)

    return score_HWY


def print_score():
    #Placed as its own variable to not be confused by all the brackets
    scoreB = score_BCH()
    scoreF = score_FAC()
    scoreH = score_HSE(grid,score_HSE)
    scoreS = score_SHP()
    scoreHWY = score_HWY()
            
    
    
            
    #Converting all the list to string
    #All functions return lists to return mulitple values
    scoreH_str = str(scoreH).strip("[]")

    #Replacing the , with + for all functions
    scoreH_str = scoreH_str.replace("," , " +")

    scoreS_str = str(scoreS).strip("[]")
    scoreS_str = scoreS_str.replace("," , " +")
    
    scoreHWY_str = str(scoreHWY).strip("[]")
    scoreHWY_str = scoreHWY_str.replace("," , " +")

    scoreB_str = str(scoreB).strip("[]")
    scoreB_str = scoreB_str.replace("," , " +")  

    Total_score = int(sum(scoreH)) + int(scoreF[1]) + int(sum(scoreS)) + int(sum(scoreHWY)) + int(sum(scoreB)) 

    #If there is no houses, it ensure it prints HSE: 0 = 0 instead of HSE:  = 0, similar for the rest
    
    if scoreH == []:
        print("HSE: 0")
    else:
        print("HSE: {} {} {}".format(scoreH_str, "=", sum(scoreH)))

    if scoreF[0] == 0:
        print("FAC: {}".format(scoreF[0]))
    else:
        print("FAC: {} = {}".format(scoreF[0], scoreF[1]))

    if scoreS == []:
        print("SHP: 0")
    else:
        print("SHP: {} {} {}".format(scoreS_str, "=", sum(scoreS)))

    if sum(scoreHWY) == 0:
        print("HWY: 0")
    else:
        print("HWY: {} {} {}".format(scoreHWY_str, "=", sum(scoreHWY)))

    if sum(scoreB) == 0:
        print("BCH: 0")
    else:
        print("BCH: {} {} {}".format(scoreB_str, "=", sum(scoreB)))

    
    print("Total score: {}".format(Total_score))
    return Total_score


    
        
#------------------------------------------Start Game----------------------------------------------#

#1. Display main menu
print("Welcome, mayor if Simp City!")
print("----------------------------")

print("1. Start new game")
print("2. Load saved game")
print("3. Show high scores")
print()
print("0. Exit")
choice = int(input("Your choice? ")) 

#1.1 Start New Game
Turn = 1
count = 1

while choice not in [1, 2, 3, 0]:
    print("The input is invalid, please try again")
    choice = int(input("Your choice? "))
    

if choice == 1:
    
    while Turn <= 16:
        print()
        print("Turn {}".format(Turn))
        table() #Printing the table
        indexes = ranNum() #Calling the random number for the random building option
        options(building_list, option_list) #Printing the options

        choice = int(input("Your choice? "))
        
        while choice not in [1, 2, 3, 4, 5, 0]:
        #^Input validation, make sure that the input is correct, will give them another try if wrong
            print("The input is invalid, please try again")
            choice = int(input("Your choice? "))
        
        if choice == 1:
            location = input("Build where? ")
            r = int(location[1]) #Getting the row number
            c = ord(location[0].upper()) - ord('A') + 1 #Returning a value from the letter

            #If the location is not within the grid, it will prompt to choose another location
            while location not in potential_option:
                print("The input is invalid, please try again")
                location = input("Build where? ")
                
            #To ensure that the place where the user wants to build is not already occupied
            while grid[r][c] != ' ':
                print("That location is already populated, please try another location")
                location = input("Build where? ")
                r = int(location[1]) 
                c = ord(location[0].upper()) - ord('A') + 1
            

        #Input validation, if firs t turn can build anywhere
            if Turn == 1:
                grid[r][c] = building_list[indexes[0]]
                building_list.pop(indexes[0])

        #Turn 2 onwards, must ensure that the buildings are placed correctly
            else:
                while True:
                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                        grid[r][c] = building_list[indexes[0]]
                        building_list.pop(indexes[0])
                        break
                    
                    else:
                        print()
                        print("You must build on squares that are connected to exitsting building")
                        print("Please try again")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1
                        
                        while location not in potential_option:
                            #Check if the location input is a valid one
                            print("The input is invalid, please try again")
                            location = input("Build where? ")

                        while grid[r][c] != ' ':
                            #Check if the place where the user wants to build is already occupied, if it is occupied, will be asked for another location
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1

            Turn += 1        

            
        elif choice == 2:
            location = input("Build where? ")
            r = int(location[1]) 
            c = ord(location[0].upper()) - ord('A') + 1

            while location not in potential_option:
                print("The input is invalid, please try again")
                location = input("Build where? ")

            while grid[r][c] != ' ':
                print("That location is already populated, please try another location")
                location = input("Build where? ")
                r = int(location[1]) 
                c = ord(location[0].upper()) - ord('A') + 1
                            

        #Input validation, if first turn can build anywhere
            if Turn == 1:
                grid[r][c] = building_list[indexes[1]]
                building_list.pop(indexes[1])

        #Turn 2 onwards, must ensure that the buildings are placed correctly
            else:
                while True:
                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                        grid[r][c] = building_list[indexes[1]]
                        building_list.pop(indexes[1])
                        break
                    
                    else:
                        print()
                        print("You must build on squares that are connected to exitsting building")
                        print("Please try again")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1

                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")
                            
                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1                                

            Turn += 1
            
        #End of the game
        if Turn > 16:
            print()
            print("Final layout of Simp City:")
            table()       
            print_score()
            
#----------------------------------------------Choice 3: See remaining building----------------------------------#
        elif choice == 3:
            remaining_buildings()
    
            while Turn <= 16:
                    print()
                    print("Turn {}".format(Turn))
                    table() #Printing the table
                    indexes = ranNum() #Calling the random number for the random building option
                    options(building_list, option_list) #Printing the options

                    choice = int(input("Your choice? "))
                    
                    while choice not in [1, 2, 3, 4, 5, 0]:
                    #^Input validation, make sure that the input is correct, will give them another try if wrong

                        print("The input is invalid, please try again")
                        choice = int(input("Your choice? "))
                    
                    if choice == 1:
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1

                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")

                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1
                        

                    #Input validation, if first turn can build anywhere
                        if Turn == 1:
                            grid[r][c] = building_list[indexes[0]]
                            building_list.pop(indexes[0])

                    #Turn 2 onwards, must ensure that the buildings are placed correctly
                        else:
                            while True:
                                #If statement below checks to ensure at least of the subsequent areas has a building in it
                                if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                    grid[r][c] = building_list[indexes[0]]
                                    building_list.pop(indexes[0])
                                    break
                                
                                else:
                                    print()
                                    print("You must build on squares that are connected to exitsting building")
                                    print("Please try again")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1
                                    
                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
                                    
                                    
                        Turn += 1        

                        
                    elif choice == 2:
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1

                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")

                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1
                                        

                    #Input validation, if first turn can build anywhere
                        if Turn == 1:
                            grid[r][c] = building_list[indexes[1]]
                            building_list.pop(indexes[1])

                    #Turn 2 onwards, must ensure that the buildings are placed correctly
                        else:
                            while True:
                                #If statement below checks to ensure at least of the subsequent areas has a building in it
                                if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                    grid[r][c] = building_list[indexes[1]]
                                    building_list.pop(indexes[1])
                                    break
                                
                                else:
                                    print()
                                    print("You must build on squares that are connected to exitsting building")
                                    print("Please try again")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
                                      
                                    
                        Turn += 1
                        
                    #End of the game
                    if Turn > 16:
                        print()
                        print("Final layout of Simp City:")
                        table()       
                        print_score()
            

                    elif choice == 3:
                        remaining_buildings()
                        while Turn <= 16:
                                print()
                                print("Turn {}".format(Turn))
                                table() #Printing the table
                                indexes = ranNum() #Calling the random number for the random building option
                                options(building_list, option_list) #Printing the options

                                choice = int(input("Your choice? "))
                                
                                while choice not in [1, 2, 3, 4, 5, 0]:
                                #^Input validation, make sure that the input is correct, will give them another try if wrong

                                    print("The input is invalid, please try again")
                                    choice = int(input("Your choice? "))
                                
                                if choice == 1:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1


                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[0]]
                                        building_list.pop(indexes[0])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[0]]
                                                building_list.pop(indexes[0])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1

                                                
                                    Turn += 1        

                                    
                                elif choice == 2:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
 

                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[1]]
                                        building_list.pop(indexes[1])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[1]]
                                                building_list.pop(indexes[1])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1

                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1
 

                                    Turn += 1
                                    
                                #End of the game
                                if Turn > 16:
                                    print()
                                    print("Final layout of Simp City:")
                                    table()       
                                    print_score()
                            
                    elif choice == 4:
                        print_score()

                        while Turn <= 16:
                                print()
                                print("Turn {}".format(Turn))
                                table() #Printing the table
                                indexes = ranNum() #Calling the random number for the random building option
                                options(building_list, option_list) #Printing the options

                                choice = int(input("Your choice? "))
                                
                                while choice not in [1, 2, 3, 4, 5, 0]:
                                #^Input validation, make sure that the input is correct, will give them another try if wrong

                                    print("The input is invalid, please try again")
                                    choice = int(input("Your choice? "))
                                
                                if choice == 1:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1


                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[0]]
                                        building_list.pop(indexes[0])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[0]]
                                                building_list.pop(indexes[0])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1

                                                
                                    Turn += 1        

                                    
                                elif choice == 2:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1

                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[1]]
                                        building_list.pop(indexes[1])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[1]]
                                                building_list.pop(indexes[1])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1

                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1                                                
                                                        

                                    Turn += 1
                                    
                                #End of the game
                                if Turn > 16:
                                    print()
                                    print("Final layout of Simp City:")
                                    table()       
                                    print_score()
                                            
                            
               
            


#---------------------------------------Choice 4: See current score--------------------------------#           
        elif choice == 4:
            print_score()
            while Turn <= 16:
                print()
                print("Turn {}".format(Turn))
                table() #Printing the table
                indexes = ranNum() #Calling the random number for the random building option
                options(building_list, option_list) #Printing the options

                choice = int(input("Your choice? "))
                
                while choice not in [1, 2, 3, 4, 5, 0]:
                #^Input validation, make sure that the input is correct, will give them another try if wrong

                    print("The input is invalid, please try again")
                    choice = int(input("Your choice? "))
                
                if choice == 1:
                    location = input("Build where? ")
                    r = int(location[1]) 
                    c = ord(location[0].upper()) - ord('A') + 1

                    while location not in potential_option:
                        print("The input is invalid, please try again")
                        location = input("Build where? ")

                    while grid[r][c] != ' ':
                        print("That location is already populated, please try another location")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1   


                #Input validation, if first turn can build anywhere
                    if Turn == 1:
                        grid[r][c] = building_list[indexes[0]]
                        building_list.pop(indexes[0])

                #Turn 2 onwards, must ensure that the buildings are placed correctly
                    else:
                        while True:
                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                grid[r][c] = building_list[indexes[0]]
                                building_list.pop(indexes[0])
                                break
                            
                            else:
                                print()
                                print("You must build on squares that are connected to exitsting building")
                                print("Please try again")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1
                                
                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1  

                                
                    Turn += 1        

                    
                elif choice == 2:
                    location = input("Build where? ")
                    r = int(location[1]) 
                    c = ord(location[0].upper()) - ord('A') + 1

                    while location not in potential_option:
                        print("The input is invalid, please try again")
                        location = input("Build where? ")

                    while grid[r][c] != ' ':
                        print("That location is already populated, please try another location")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1


                #Input validation, if first turn can build anywhere
                    if Turn == 1:
                        grid[r][c] = building_list[indexes[1]]
                        building_list.pop(indexes[1])

                #Turn 2 onwards, must ensure that the buildings are placed correctly
                    else:
                        while True:
                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                grid[r][c] = building_list[indexes[1]]
                                building_list.pop(indexes[1])
                                break
                            
                            else:
                                print()
                                print("You must build on squares that are connected to exitsting building")
                                print("Please try again")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1

                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1
                                
                                        

                    Turn += 1
                    
                #End of the game
                if Turn > 16:
                    print()
                    print("Final layout of Simp City:")
                    table()       
                    print_score()
                    
                elif choice == 3:
                    remaining_buildings()
                    while Turn <= 16:
                        print()
                        print("Turn {}".format(Turn))
                        table() #Printing the table
                        indexes = ranNum() #Calling the random number for the random building option
                        options(building_list, option_list) #Printing the options

                        choice = int(input("Your choice? "))
                        
                        while choice not in [1, 2, 3, 4, 5, 0]:
                        #^Input validation, make sure that the input is correct, will give them another try if wrong

                            print("The input is invalid, please try again")
                            choice = int(input("Your choice? "))
                        
                        if choice == 1:
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1

                            while location not in potential_option:
                                print("The input is invalid, please try again")
                                location = input("Build where? ")

                            while grid[r][c] != ' ':
                                print("That location is already populated, please try another location")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1


                        #Input validation, if first turn can build anywhere
                            if Turn == 1:
                                grid[r][c] = building_list[indexes[0]]
                                building_list.pop(indexes[0])

                        #Turn 2 onwards, must ensure that the buildings are placed correctly
                            else:
                                while True:
                                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                        grid[r][c] = building_list[indexes[0]]
                                        building_list.pop(indexes[0])
                                        break
                                    
                                    else:
                                        print()
                                        print("You must build on squares that are connected to exitsting building")
                                        print("Please try again")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
                                        
                                        while location not in potential_option:
                                            print("The input is invalid, please try again")
                                            location = input("Build where? ")

                                        while grid[r][c] != ' ':
                                            print("That location is already populated, please try another location")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1

                                        
                            Turn += 1        

                            
                        elif choice == 2:
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1

                            while location not in potential_option:
                                print("The input is invalid, please try again")
                                location = input("Build where? ")

                            while grid[r][c] != ' ':
                                print("That location is already populated, please try another location")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1


                        #Input validation, if first turn can build anywhere
                            if Turn == 1:
                                grid[r][c] = building_list[indexes[1]]
                                building_list.pop(indexes[1])

                        #Turn 2 onwards, must ensure that the buildings are placed correctly
                            else:
                                while True:
                                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                        grid[r][c] = building_list[indexes[1]]
                                        building_list.pop(indexes[1])
                                        break
                                    
                                    else:
                                        print()
                                        print("You must build on squares that are connected to exitsting building")
                                        print("Please try again")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1

                                        while location not in potential_option:
                                            print("The input is invalid, please try again")
                                            location = input("Build where? ")

                                        while grid[r][c] != ' ':
                                            print("That location is already populated, please try another location")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1

               
                elif choice == 4:
                    print_score()

                    while Turn <= 16:
                            print()
                            print("Turn {}".format(Turn))
                            table() #Printing the table
                            indexes = ranNum() #Calling the random number for the random building option
                            options(building_list, option_list) #Printing the options

                            choice = int(input("Your choice? "))
                                
                            while choice not in [1, 2, 3, 4, 5, 0]:
                            #^Input validation, make sure that the input is correct, will give them another try if wrong

                                print("The input is invalid, please try again")
                                choice = int(input("Your choice? "))
                                
                            if choice == 1:
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1

                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1


                            #Input validation, if first turn can build anywhere
                                if Turn == 1:
                                    grid[r][c] = building_list[indexes[0]]
                                    building_list.pop(indexes[0])

                            #Turn 2 onwards, must ensure that the buildings are placed correctly
                                else:
                                    while True:
                                        #If statement below checks to ensure at least of the subsequent areas has a building in it
                                        if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                            grid[r][c] = building_list[indexes[0]]
                                            building_list.pop(indexes[0])
                                            break
                                            
                                        else:
                                            print()
                                            print("You must build on squares that are connected to exitsting building")
                                            print("Please try again")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1
                                                
                                            while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                            while grid[r][c] != ' ':
                                                print("That location is already populated, please try another location")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                Turn += 1        

                                    
                            elif choice == 2:
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1

                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                            #Input validation, if first turn can build anywhere
                                if Turn == 1:
                                    grid[r][c] = building_list[indexes[1]]
                                    building_list.pop(indexes[1])

                            #Turn 2 onwards, must ensure that the buildings are placed correctly
                                else:
                                    while True:
                                        #If statement below checks to ensure at least of the subsequent areas has a building in it
                                        if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                            grid[r][c] = building_list[indexes[1]]
                                            building_list.pop(indexes[1])
                                            break
                                            
                                        else:
                                            print()
                                            print("You must build on squares that are connected to exitsting building")
                                            print("Please try again")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1

                                            while location not in potential_option:
                                                print("The input is invalid, please try again")
                                                location = input("Build where? ")

                                            while grid[r][c] != ' ':
                                                print("That location is already populated, please try another location")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                                        

                                Turn += 1
                                    
                            #End of the game
                            if Turn > 16:
                                print()
                                print("Final layout of Simp City:")
                                table()       
                                print_score()
            
                
#--------------------------------------Choice 5: Save Game-----------------------------------#
        elif choice == 5:
            save()
            print()
            print("Game saved!")
            break

#------------------------------------Choice 0: Exit to main menu------------------------------#
        elif choice == 0:
            print()
            print("Welcome, mayor if Simp City!")
            print("----------------------------")

            print("1. Start new game")
            print("2. Load saved game")
            print()
            print("0. Exit")
            choice = int(input("Your choice? "))

#Exiting the game from the main menu
elif choice == 0:
    exit()




#---------------------------------------For Load Game---------------------------------------------#

elif choice == 2:
    load()

    #To go to each row and column and remove the building from the building list to ensure
    #Remaining building shows and allows the correct number of buildings
    
    for r in range(max_row):
        for c in range(max_col):
            if grid[r][c] == 'HSE':
                building_list.remove("HSE")

            elif grid[r][c] == 'BCH':
                building_list.remove("BCH")

            elif grid[r][c] == 'SHP':
                building_list.remove("SHP")

            elif grid[r][c] == 'FAC':
                building_list.remove("FAC")

            elif grid[r][c] == 'HWY':
                building_list.remove("HWY")
                
    while Turn <= 16:
        print()
        print("Turn {}".format(Turn))
        table() #Printing the table
        indexes = ranNum() #Calling the random number for the random building option
        options(building_list, option_list) #Printing the options

        choice = int(input("Your choice? "))
        
        while choice not in [1, 2, 3, 4, 5, 0]:
        #^Input validation, make sure that the input is correct, will give them another try if wrong
            print("The input is invalid, please try again")
            choice = int(input("Your choice? "))
        
        if choice == 1:
            location = input("Build where? ")
            r = int(location[1]) 
            c = ord(location[0].upper()) - ord('A') + 1

            #If the location is not within the grid, it will prompt to choose another location
            while location not in potential_option:
                print("The input is invalid, please try again")
                location = input("Build where? ")
                

            while grid[r][c] != ' ':
                print("That location is already populated, please try another location")
                location = input("Build where? ")
                r = int(location[1]) 
                c = ord(location[0].upper()) - ord('A') + 1
            

        #Input validation, if firs t turn can build anywhere
            if Turn == 1:
                grid[r][c] = building_list[indexes[0]]
                building_list.pop(indexes[0])

        #Turn 2 onwards, must ensure that the buildings are placed correctly
            else:
                while True:
                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                        grid[r][c] = building_list[indexes[0]]
                        building_list.pop(indexes[0])
                        break
                    
                    else:
                        print()
                        print("You must build on squares that are connected to exitsting building")
                        print("Please try again")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1
                        
                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")

                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1

            Turn += 1        

            
        elif choice == 2:
            location = input("Build where? ")
            r = int(location[1]) 
            c = ord(location[0].upper()) - ord('A') + 1

            while location not in potential_option:
                print("The input is invalid, please try again")
                location = input("Build where? ")

            while grid[r][c] != ' ':
                print("That location is already populated, please try another location")
                location = input("Build where? ")
                r = int(location[1]) 
                c = ord(location[0].upper()) - ord('A') + 1
                            

        #Input validation, if first turn can build anywhere
            if Turn == 1:
                grid[r][c] = building_list[indexes[1]]
                building_list.pop(indexes[1])

        #Turn 2 onwards, must ensure that the buildings are placed correctly
            else:
                while True:
                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                        grid[r][c] = building_list[indexes[1]]
                        building_list.pop(indexes[1])
                        break
                    
                    else:
                        print()
                        print("You must build on squares that are connected to exitsting building")
                        print("Please try again")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1

                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")
                            
                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1                                

            Turn += 1
            
        #End of the game
        if Turn > 16:
            print()
            print("Final layout of Simp City:")
            table()       
            print_score()
            
#----------------------------------------------Choice 3: See remaining building----------------------------------#
        elif choice == 3:
            remaining_buildings()
    
            while Turn <= 16:
                    print()
                    print("Turn {}".format(Turn))
                    table() #Printing the table
                    indexes = ranNum() #Calling the random number for the random building option
                    options(building_list, option_list) #Printing the options

                    choice = int(input("Your choice? "))
                    
                    while choice not in [1, 2, 3, 4, 5, 0]:
                    #^Input validation, make sure that the input is correct, will give them another try if wrong

                        print("The input is invalid, please try again")
                        choice = int(input("Your choice? "))
                    
                    if choice == 1:
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1

                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")

                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1
                        

                    #Input validation, if first turn can build anywhere
                        if Turn == 1:
                            grid[r][c] = building_list[indexes[0]]
                            building_list.pop(indexes[0])

                    #Turn 2 onwards, must ensure that the buildings are placed correctly
                        else:
                            while True:
                                #If statement below checks to ensure at least of the subsequent areas has a building in it
                                if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                    grid[r][c] = building_list[indexes[0]]
                                    building_list.pop(indexes[0])
                                    break
                                
                                else:
                                    print()
                                    print("You must build on squares that are connected to exitsting building")
                                    print("Please try again")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1
                                    
                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
                                    
                                    
                        Turn += 1        

                        
                    elif choice == 2:
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1

                        while location not in potential_option:
                            print("The input is invalid, please try again")
                            location = input("Build where? ")

                        while grid[r][c] != ' ':
                            print("That location is already populated, please try another location")
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1
                                        

                    #Input validation, if first turn can build anywhere
                        if Turn == 1:
                            grid[r][c] = building_list[indexes[1]]
                            building_list.pop(indexes[1])

                    #Turn 2 onwards, must ensure that the buildings are placed correctly
                        else:
                            while True:
                                #If statement below checks to ensure at least of the subsequent areas has a building in it
                                if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                    grid[r][c] = building_list[indexes[1]]
                                    building_list.pop(indexes[1])
                                    break
                                
                                else:
                                    print()
                                    print("You must build on squares that are connected to exitsting building")
                                    print("Please try again")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
                                      
                                    
                        Turn += 1
                        
                    #End of the game
                    if Turn > 16:
                        print()
                        print("Final layout of Simp City:")
                        table()       
                        print_score()
            

                    elif choice == 3:
                        remaining_buildings()
                        while Turn <= 16:
                                print()
                                print("Turn {}".format(Turn))
                                table() #Printing the table
                                indexes = ranNum() #Calling the random number for the random building option
                                options(building_list, option_list) #Printing the options

                                choice = int(input("Your choice? "))
                                
                                while choice not in [1, 2, 3, 4, 5, 0]:
                                #^Input validation, make sure that the input is correct, will give them another try if wrong

                                    print("The input is invalid, please try again")
                                    choice = int(input("Your choice? "))
                                
                                if choice == 1:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1


                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[0]]
                                        building_list.pop(indexes[0])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[0]]
                                                building_list.pop(indexes[0])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1

                                                
                                    Turn += 1        

                                    
                                elif choice == 2:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
 

                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[1]]
                                        building_list.pop(indexes[1])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[1]]
                                                building_list.pop(indexes[1])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1

                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1
 

                                    Turn += 1
                                    
                                #End of the game
                                if Turn > 16:
                                    print()
                                    print("Final layout of Simp City:")
                                    table()       
                                    print_score()
                            
                    elif choice == 4:
                        print_score()

                        while Turn <= 16:
                                print()
                                print("Turn {}".format(Turn))
                                table() #Printing the table
                                indexes = ranNum() #Calling the random number for the random building option
                                options(building_list, option_list) #Printing the options

                                choice = int(input("Your choice? "))
                                
                                while choice not in [1, 2, 3, 4, 5, 0]:
                                #^Input validation, make sure that the input is correct, will give them another try if wrong

                                    print("The input is invalid, please try again")
                                    choice = int(input("Your choice? "))
                                
                                if choice == 1:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1


                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[0]]
                                        building_list.pop(indexes[0])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[0]]
                                                building_list.pop(indexes[0])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1

                                                
                                    Turn += 1        

                                    
                                elif choice == 2:
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                                    while location not in potential_option:
                                        print("The input is invalid, please try again")
                                        location = input("Build where? ")

                                    while grid[r][c] != ' ':
                                        print("That location is already populated, please try another location")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1

                                #Input validation, if first turn can build anywhere
                                    if Turn == 1:
                                        grid[r][c] = building_list[indexes[1]]
                                        building_list.pop(indexes[1])

                                #Turn 2 onwards, must ensure that the buildings are placed correctly
                                    else:
                                        while True:
                                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                                grid[r][c] = building_list[indexes[1]]
                                                building_list.pop(indexes[1])
                                                break
                                            
                                            else:
                                                print()
                                                print("You must build on squares that are connected to exitsting building")
                                                print("Please try again")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1

                                                while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                                while grid[r][c] != ' ':
                                                    print("That location is already populated, please try another location")
                                                    location = input("Build where? ")
                                                    r = int(location[1]) 
                                                    c = ord(location[0].upper()) - ord('A') + 1                                                
                                                        

                                    Turn += 1
                                    
                                #End of the game
                                if Turn > 16:
                                    print()
                                    print("Final layout of Simp City:")
                                    table()       
                                    print_score()
                                            
                            
               
            


#---------------------------------------Choice 4: See current score--------------------------------#           
        elif choice == 4:
            print_score()
            while Turn <= 16:
                print()
                print("Turn {}".format(Turn))
                table() #Printing the table
                indexes = ranNum() #Calling the random number for the random building option
                options(building_list, option_list) #Printing the options

                choice = int(input("Your choice? "))
                
                while choice not in [1, 2, 3, 4, 5, 0]:
                #^Input validation, make sure that the input is correct, will give them another try if wrong

                    print("The input is invalid, please try again")
                    choice = int(input("Your choice? "))
                
                if choice == 1:
                    location = input("Build where? ")
                    r = int(location[1]) 
                    c = ord(location[0].upper()) - ord('A') + 1

                    while location not in potential_option:
                        print("The input is invalid, please try again")
                        location = input("Build where? ")

                    while grid[r][c] != ' ':
                        print("That location is already populated, please try another location")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1   


                #Input validation, if first turn can build anywhere
                    if Turn == 1:
                        grid[r][c] = building_list[indexes[0]]
                        building_list.pop(indexes[0])

                #Turn 2 onwards, must ensure that the buildings are placed correctly
                    else:
                        while True:
                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                grid[r][c] = building_list[indexes[0]]
                                building_list.pop(indexes[0])
                                break
                            
                            else:
                                print()
                                print("You must build on squares that are connected to exitsting building")
                                print("Please try again")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1
                                
                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1  

                                
                    Turn += 1        

                    
                elif choice == 2:
                    location = input("Build where? ")
                    r = int(location[1]) 
                    c = ord(location[0].upper()) - ord('A') + 1

                    while location not in potential_option:
                        print("The input is invalid, please try again")
                        location = input("Build where? ")

                    while grid[r][c] != ' ':
                        print("That location is already populated, please try another location")
                        location = input("Build where? ")
                        r = int(location[1]) 
                        c = ord(location[0].upper()) - ord('A') + 1


                #Input validation, if first turn can build anywhere
                    if Turn == 1:
                        grid[r][c] = building_list[indexes[1]]
                        building_list.pop(indexes[1])

                #Turn 2 onwards, must ensure that the buildings are placed correctly
                    else:
                        while True:
                            #If statement below checks to ensure at least of the subsequent areas has a building in it
                            if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                grid[r][c] = building_list[indexes[1]]
                                building_list.pop(indexes[1])
                                break
                            
                            else:
                                print()
                                print("You must build on squares that are connected to exitsting building")
                                print("Please try again")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1

                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1
                                
                                        

                    Turn += 1
                    
                #End of the game
                if Turn > 16:
                    print()
                    print("Final layout of Simp City:")
                    table()       
                    print_score()
                    
                elif choice == 3:
                    remaining_buildings()
                    while Turn <= 16:
                        print()
                        print("Turn {}".format(Turn))
                        table() #Printing the table
                        indexes = ranNum() #Calling the random number for the random building option
                        options(building_list, option_list) #Printing the options

                        choice = int(input("Your choice? "))
                        
                        while choice not in [1, 2, 3, 4, 5, 0]:
                        #^Input validation, make sure that the input is correct, will give them another try if wrong

                            print("The input is invalid, please try again")
                            choice = int(input("Your choice? "))
                        
                        if choice == 1:
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1

                            while location not in potential_option:
                                print("The input is invalid, please try again")
                                location = input("Build where? ")

                            while grid[r][c] != ' ':
                                print("That location is already populated, please try another location")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1


                        #Input validation, if first turn can build anywhere
                            if Turn == 1:
                                grid[r][c] = building_list[indexes[0]]
                                building_list.pop(indexes[0])

                        #Turn 2 onwards, must ensure that the buildings are placed correctly
                            else:
                                while True:
                                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                        grid[r][c] = building_list[indexes[0]]
                                        building_list.pop(indexes[0])
                                        break
                                    
                                    else:
                                        print()
                                        print("You must build on squares that are connected to exitsting building")
                                        print("Please try again")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1
                                        
                                        while location not in potential_option:
                                            print("The input is invalid, please try again")
                                            location = input("Build where? ")

                                        while grid[r][c] != ' ':
                                            print("That location is already populated, please try another location")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1

                                        
                            Turn += 1        

                            
                        elif choice == 2:
                            location = input("Build where? ")
                            r = int(location[1]) 
                            c = ord(location[0].upper()) - ord('A') + 1

                            while location not in potential_option:
                                print("The input is invalid, please try again")
                                location = input("Build where? ")

                            while grid[r][c] != ' ':
                                print("That location is already populated, please try another location")
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1


                        #Input validation, if first turn can build anywhere
                            if Turn == 1:
                                grid[r][c] = building_list[indexes[1]]
                                building_list.pop(indexes[1])

                        #Turn 2 onwards, must ensure that the buildings are placed correctly
                            else:
                                while True:
                                    #If statement below checks to ensure at least of the subsequent areas has a building in it
                                    if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                        grid[r][c] = building_list[indexes[1]]
                                        building_list.pop(indexes[1])
                                        break
                                    
                                    else:
                                        print()
                                        print("You must build on squares that are connected to exitsting building")
                                        print("Please try again")
                                        location = input("Build where? ")
                                        r = int(location[1]) 
                                        c = ord(location[0].upper()) - ord('A') + 1

                                        while location not in potential_option:
                                            print("The input is invalid, please try again")
                                            location = input("Build where? ")

                                        while grid[r][c] != ' ':
                                            print("That location is already populated, please try another location")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1

               
                elif choice == 4:
                    print_score()

                    while Turn <= 16:
                            print()
                            print("Turn {}".format(Turn))
                            table() #Printing the table
                            indexes = ranNum() #Calling the random number for the random building option
                            options(building_list, option_list) #Printing the options

                            choice = int(input("Your choice? "))
                                
                            while choice not in [1, 2, 3, 4, 5, 0]:
                            #^Input validation, make sure that the input is correct, will give them another try if wrong

                                print("The input is invalid, please try again")
                                choice = int(input("Your choice? "))
                                
                            if choice == 1:
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1

                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1


                            #Input validation, if first turn can build anywhere
                                if Turn == 1:
                                    grid[r][c] = building_list[indexes[0]]
                                    building_list.pop(indexes[0])

                            #Turn 2 onwards, must ensure that the buildings are placed correctly
                                else:
                                    while True:
                                        #If statement below checks to ensure at least of the subsequent areas has a building in it
                                        if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                            grid[r][c] = building_list[indexes[0]]
                                            building_list.pop(indexes[0])
                                            break
                                            
                                        else:
                                            print()
                                            print("You must build on squares that are connected to exitsting building")
                                            print("Please try again")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1
                                                
                                            while location not in potential_option:
                                                    print("The input is invalid, please try again")
                                                    location = input("Build where? ")

                                            while grid[r][c] != ' ':
                                                print("That location is already populated, please try another location")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                Turn += 1        

                                    
                            elif choice == 2:
                                location = input("Build where? ")
                                r = int(location[1]) 
                                c = ord(location[0].upper()) - ord('A') + 1

                                while location not in potential_option:
                                    print("The input is invalid, please try again")
                                    location = input("Build where? ")

                                while grid[r][c] != ' ':
                                    print("That location is already populated, please try another location")
                                    location = input("Build where? ")
                                    r = int(location[1]) 
                                    c = ord(location[0].upper()) - ord('A') + 1

                            #Input validation, if first turn can build anywhere
                                if Turn == 1:
                                    grid[r][c] = building_list[indexes[1]]
                                    building_list.pop(indexes[1])

                            #Turn 2 onwards, must ensure that the buildings are placed correctly
                                else:
                                    while True:
                                        #If statement below checks to ensure at least of the subsequent areas has a building in it
                                        if grid[r-1][c] != ' ' or grid[r+1][c] != ' ' or grid[r][c-1] != ' ' or grid[r][c+1] != ' ':
                                            grid[r][c] = building_list[indexes[1]]
                                            building_list.pop(indexes[1])
                                            break
                                            
                                        else:
                                            print()
                                            print("You must build on squares that are connected to exitsting building")
                                            print("Please try again")
                                            location = input("Build where? ")
                                            r = int(location[1]) 
                                            c = ord(location[0].upper()) - ord('A') + 1

                                            while location not in potential_option:
                                                print("The input is invalid, please try again")
                                                location = input("Build where? ")

                                            while grid[r][c] != ' ':
                                                print("That location is already populated, please try another location")
                                                location = input("Build where? ")
                                                r = int(location[1]) 
                                                c = ord(location[0].upper()) - ord('A') + 1
                                                
                                                        

                                Turn += 1
                                    
                            #End of the game
                            if Turn > 16:
                                print()
                                print("Final layout of Simp City:")
                                table()       
                                print_score()
            
                
#--------------------------------------Choice 5: Save Game-----------------------------------#
        elif choice == 5:
            save()
            print()
            print("Game saved!")
            break

#------------------------------------Choice 0: Exit to main menu------------------------------#
        elif choice == 0:
            print()
            print("Welcome, mayor if Simp City!")
            print("----------------------------")

            print("1. Start new game")
            print("2. Load saved game")
            print()
            print("0. Exit")
            choice = int(input("Your choice? "))

#Exiting the game from the main menu
elif choice == 0:
    exit()


    


#------------------------------------Show high score-------------------------------------#
elif choice == 3:
    HighScores_load()

